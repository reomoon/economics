import requests
import os
from dotenv import load_dotenv

# .env 파일에서 API 키를 가져옴
load_dotenv()

# .env 파일에서 news_key API 변수를 지정
news_api_key = os.getenv('news_key')

def fetch_news():
    # 월스트리트 저널에서 기사 가져오기
    NEWS_URL = f"https://newsapi.org/v2/top-headlines?sources=the-wall-street-journal&language=en&apiKey={news_api_key}"

    response = requests.get(NEWS_URL)
    news_data = response.json()

    # 최신 기사 1개 선택
    if "articles" in news_data and len(news_data["articles"]) > 0:
        article = news_data["articles"][0]
        news_title = article.get("title", "제목 없음")
        news_content = article.get("description", "내용 없음")
        news_url = article.get("url", "#")
        news_image = article.get("urlToImage", None)

        return news_title, news_content, news_url, news_image
    else:
        return None, None, None, None

# 테스트 실행
news_title, news_content, news_url, news_image = fetch_news()
print(f"🔹 제목: {news_title}")
print(f"📌 내용: {news_content}")
print(f"🔗 원문: {news_url}")
print(f"대표 이미지: {news_image}")
