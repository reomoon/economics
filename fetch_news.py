import requests
import os
from dotenv import load_dotenv
from datetime import datetime
from yfinance import Ticker

# .env 파일에서 API 키를 가져옴
load_dotenv()

# .env 파일에서 news_key API 변수를 지정
news_api_key = os.getenv('news_key')

# .env 파일에서 Alpha Vantage key API 변수를 지정
alpha_vantage_api_key = os.getenv('alpha_vantage_key')

def fetch_stock_news():
    """NewsAPI에서 미국 주식 관련 뉴스 가져오기"""
    NEWS_URL = f"https://newsapi.org/v2/everything?q=stock&language=en&sortBy=publishedAt&pageSize=10&apiKey={news_api_key}"

    response = requests.get(NEWS_URL)
    news_data = response.json()

    news_list = []
    if "articles" in news_data:
        for article in news_data["articles"]:
            title = article.get("title", "제목 없음")
            description = article.get("description", "내용 없음")
            url = article.get("url", "#")
            
            # 기사 제목에서 랜덤하게 종목명 추출 (단순 매칭)
            possible_stocks = ["TSLA", "AAPL", "MSFT", "GOOGL", "NVDA", "AMZN"]
            matched_stock = random.choice(possible_stocks) if any(stock in title for stock in possible_stocks) else "Random"

            # ✅ 튜플 대신 딕셔너리 저장
            news_list.append({
                "stock": matched_stock,
                "title": title,
                "description": description,
                "url": url
            })
    
    return news_list  # ✅ 딕셔너리 리스트 반환
