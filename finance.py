import openai       # OpenAI API 사용     
import yfinance as yf
from fetch_news import fetch_stock_news
from datetime import datetime
from googletrans import Translator # 구글번역
from dotenv import load_dotenv
import os

# .env 파일에서 API 키를 가져옴
load_dotenv()
# .env 파일에서 news_key API 변수를 지정
openai_api_key = os.getenv('openai_key')

# OpenAI API 키 설정
if openai_api_key is None:
    raise ValueError("API 키가 .env 파일에서 로드되지 않았습니다.")
openai.api_key = openai_api_key  # API 키 설정

# 주요 지수 티커
indices = {
    "NASDAQ": "^IXIC",
    "Dow Jones": "^DJI"
}

# 주요 지수 데이터 가져오기
index_data = {}
for name, symbol in indices.items():
    ticker = yf.Ticker(symbol)
    data = ticker.history(period="2d")  # 2일치 데이터 가져오기

    if len(data) < 2:  # 데이터가 충분하지 않은 경우
        index_data[name] = ("데이터 없음", "데이터 없음")
    else:
        latest_price = round(data["Close"].iloc[-1], 2)  # 최신 종가 (소수점 2자리)
        previous_price = round(data["Close"].iloc[-2], 2)  # 전일 종가
        percent_change = round((latest_price - previous_price) / previous_price * 100, 2)  # 등락률

        trend_symbol = "📈" if latest_price > previous_price else "📉"  # 상승/하락 아이콘
        index_data[name] = (latest_price, f"{trend_symbol} 전일 대비 {percent_change}%")  # ✅ 튜플 저장

# 📊 주요 지수 데이터 출력
print(f"\n[{datetime.now().strftime('%Y-%m-%d')}] 주요 지수 동향")
for name, (price, percent) in index_data.items():  # ✅ 튜플 언패킹 사용
    print(f"{name}: {price}, {percent}")

# 뉴스 가져오기
news_list = fetch_stock_news()

# OpenAI를 사용한 뉴스 분석 함수
def analyze_news_with_openai(news_title, news_content):
    prompt = f"Analyze the following news article and summarize the stock market trend, rising factors, and falling factors:\n\n{news_title}\n\n{news_content}"
    prompt = f"한글로 번역해서 요약 분석결과를 추가해줘{prompt}\n\n---\n\nSummary:"  # 결과 요약 부분 추가
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # 또는 최신 GPT 모델(GPT-3.5-turbo) 사용
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=200,
        temperature=0.5
    )

    # 응답에서 분석 결과 추출                                         
    analysis = response['choices'][0]['message']['content'].strip()
    return analysis

# 주식 뉴스 출력
print("\n📌 최신 주식 뉴스 분석:")
if not news_list:
    print("❌ 관련 뉴스가 없습니다.")
else:
    for news in news_list[:5]:  # 최신 뉴스 5개 출력
        title = news['title']
        description = news['description']

        # OpenAI API로 뉴스 분석
        analysis = analyze_news_with_openai(title, description)

        print(f"\n📌 {title}")
        print(f"   {description}")
        print(f"   🔗 {news['url']}")
        print(f"   📝 분석 결과: {analysis}")