from fetch_news import fetch_news
from summarize_news import summarize_news

# 뉴스 목록 가져오기
news_list = fetch_news()

# 각 뉴스에 대해 요약하고 출력
summarized_news_list = []

# 각 뉴스에 대해 요약
for news_title, news_content, news_url, news_image in news_list:
    # GPT-4로 요약
    news_summary = summarize_news(news_title, news_content)
    summarized_news_list.append(news_summary)

# 모든 요약된 내용 합치기
all_summaries = "\n".join(summarized_news_list)

# 모든 요약을 다시 한 번 GPT-4로 요약하기
final_summary = summarize_news("전체 뉴스 요약", all_summaries)

# 최종 요약 출력
print(f"🔹 전체 요약: {final_summary}")
