import requests
import ssl
ssl_version = ssl.PROTOCOL_TLSv1_2  # 使用TLSv1.2协议
def get_chatgpt_response(prompt):
    # 替换下面的API_ENDPOINT和API_KEY为你自己的ChatGPT API的URL和密钥
    API_ENDPOINT = "https://api.openai.com/v1/engines/davinci/completions"
    API_KEY = "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"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    data = {
        "prompt": prompt,
        "max_tokens": 100
    }

    # 设置代理
    proxies = {
        "http": "http://127.0.0.1:7890",
        "https": "http://127.0.0.1:7890"
    }

    response = requests.post(API_ENDPOINT, json=data, headers=headers, proxies=proxies)

    if response.status_code == 200:
        data = response.json()
        return data['choices'][0]['text']
    else:
        return f"Error: {response.status_code}, {response.text}"



user_input = "nihao"

response = get_chatgpt_response(user_input)
print("ChatGPT:", response)