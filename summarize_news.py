import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

def summarize_news(news_text):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "Summarize the news article in 3-5 sentences."},
                  {"role": "user", "content": news_text}]
    )
    return response["choices"][0]["message"]["content"]
