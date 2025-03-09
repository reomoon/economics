import requests
import os
from dotenv import load_dotenv

# .env 파일에서 API 키를 가져옴
load_dotenv()

# .env 파일에서 news_key API 변수를 지정
news_api_key = os.getenv('news_key')

def fetch_news():
    # 월스트리트 저널에서 기사 가져오기
    NEWS_URL = f"https://newsapi.org/v2/top-headlines?category=business&language=en&pageSize=5&apiKey={news_api_key}"

    response = requests.get(NEWS_URL)
    news_data = response.json()

    news_list = []

    if "articles" in news_data and len(news_data["articles"]) > 0:
        for article in news_data["articles"]:
            news_title = article.get("title", "제목 없음")
            
            # `description` 필드를 기본으로 사용하고, `content`가 있으면 추가
            description = article.get("description", "")
            content = article.get("content", "")

            # description이 있으면 기본값으로 사용하고, content가 있으면 추가
            if content and content not in description:
                news_content = f"{description} {content}"
            else:
                news_content = description

            news_url = article.get("url", "#")
            news_image = article.get("urlToImage", None)

            news_list.append((news_title, news_content, news_url, news_image))

    return news_list

# 뉴스 가져오기
news_list = fetch_news()

# ✅ 출력 확인
for news_title, news_content, news_url, news_image in news_list:
    print(f"🔹 제목: {news_title}")
    print(f"📌 내용: {news_content}")  # ✅ 더 많은 내용 가져오기 가능
    print(f"🔗 원문: {news_url}")
    print(f"대표 이미지: {news_image}")
    print("\n" + "="*80 + "\n")
