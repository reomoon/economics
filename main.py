from fetch_news import fetch_news
from summarize_news import summarize_news

# 뉴스 가져오기
news_title, news_content, news_url, news_image = fetch_news()

# GPT-4로 요약
news_summary = summarize_news(news_content)

# 결과 출력
print(f"🔹 제목: {news_title}")
print(f"📌 요약: {news_summary}")
print(f"🔗 원문: {news_url}")
print(f"대표 이미지: {news_image}")
