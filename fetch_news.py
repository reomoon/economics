import requests

def fetch_news():
    API_KEY = "YOUR_NEWS_API_KEY"
    NEWS_URL = f"https://newsapi.org/v2/top-headlines?category=business&language=en&apiKey={API_KEY}"

    response = requests.get(NEWS_URL)
    news_data = response.json()

    # 최신 기사 1개 선택
    article = news_data["articles"][0]
    news_title = article["title"]
    news_content = article["description"]  # 기사 내용
    news_url = article["url"]
    news_image = article["urlToImage"]  # 대표 이미지

    return news_title, news_content, news_url, news_image
