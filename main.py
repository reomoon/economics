from fetch_news import fetch_news
from summarize_news import summarize_news

# 뉴스 목록 가져오기
news_list = fetch_news()

# 각 뉴스에 대해 요약하고 출력
for news_title, news_content, news_url, news_image in news_list:
    # GPT-4로 요약
    news_summary = summarize_news(news_title, news_content)

    # 결과 출력
    print(f"🔹 제목: {news_title}")
    print(f"📌 요약: {news_summary}")
    print(f"🔗 원문: {news_url}")
    print(f"대표 이미지: {news_image}")
    print("\n" + "="*80 + "\n")
