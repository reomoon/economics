import openai
import os
from dotenv import load_dotenv
from fetch_news import fetch_news   

# .env 파일에서 API 키를 가져옴
load_dotenv()

# .env 파일에서 openai_key 변수를 지정
openai_api_key = os.getenv('openai_key')
openai.api_key = openai_api_key

def summarize_news(news_title, news_content):
    if not news_title or news_title.strip() == "" or not news_content or news_content.strip() == "":
        return "❗ 뉴스 제목 또는 내용이 없습니다."

    # GPT-4 모델로 번역 및 요약 요청
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an assistant that summarizes news articles."},
            {"role": "user", "content": f"다음 제목과 내용을 한국어로 번역하고, 간단하게 요약한 후 아래 내용을 포함하도록 해줘:\n\n제목: {news_title}\n내용: {news_content}\n\n1. 주식 지수 동향 (다우, S&P, 나스닥 등)\n2. 하락/상승 요인\n3. 주요 ETF 동향"}
        ],
        temperature=0.5,  # 창의성 조정
        # max_tokens=200,  # 토큰 수 제한으로 길이 제어
    )

    # 결과 반환
    return response['choices'][0]['message']['content']

# fetch_news 함수에서 가져온 뉴스 제목과 내용
news_title, news_content, news_url, news_image = fetch_news()

# 뉴스 기사를 가져오고 요약하기
news_list = fetch_news()

for news_title, news_content, news_url, news_image in news_list:
    # 뉴스 요약하기
    news_summary = summarize_news(news_title, news_content)

    # 출력 결과
    print(f"✅ 제목: {news_title}")
    print(f"✅ 대표 이미지: {news_image}")
    print(f"✅ 요약 내용: {news_summary}")
    print(f"✅ 뉴스 원문 링크: {news_url}")
    print("\n" + "="*80 + "\n")