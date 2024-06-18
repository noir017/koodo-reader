from openai import OpenAI
api_key = "AIzaSyBd1FAwmC3ZBVi8xyg4OKBx58bb1GOqGDg"
model = "gemini-1.5-pro-latest"

BASE_URL = "https://llmapi.ultrasev.com/v2/gemini"

client = OpenAI(base_url=BASE_URL, api_key=api_key)
response = client.chat.completions.create(
    model=model,
    messages=[
        {"role": "system", "content": "You are a helpful assistant。"},
        {"role": "user", "content": "what is the meaning of life?"}
    ],
)
print(response.choices[0].message.content)