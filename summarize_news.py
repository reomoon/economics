import openai
import os
from dotenv import load_dotenv

# .env 파일에서 API 키를 가져옴
load_dotenv()

# .env 파일에서 openai_key 변수를 지정
openai.api_key = os.getenv('oepnai_key')

def summarize_news(news_text):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "Summarize the news article in 3-5 sentences."},
                  {"role": "user", "content": news_text}]
    )
    return response["choices"][0]["message"]["content"]
