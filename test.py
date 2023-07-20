import requests
import resolution


# 用于存储API返回的上下文
class gpt:
    def send_request(self,messages):
        # 设置代理服务器的地址和端口
        proxies = {
            "http": "http://127.0.0.1:7890",
            "https": "http://127.0.0.1:7890"
        }
        # ChatGPT API的URL
        url = "https://api.openai.com/v1/chat/completions"
        # ChatGPT API的访问密钥
        api_key = "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"
        # 请求参数
        parameters = {
                      "model": "gpt-3.5-turbo", #gpt-3.5-turbo-0301
                      "messages":messages# [{"role": "user", "content": context}]
                    }
        # 请求头
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        # 发送请求
        response = requests.post(url, headers=headers, json=parameters, proxies=proxies)

        # 解析响应
        if response.status_code == 200:
            data = response.json()
            text = data["choices"][0]["message"]

            return text
        else:
            print(response)
            return "Sorry, something went wrong."

    def get_answer(self, user_input):
        user_message={"role": "user", "content": user_input}
        # 发送API请求
        response = self.send_request(user_message)
        # 输出API返回内容
        print("ChatBot：",response)
            
if __name__ == '__main__':

    coordinates = [(1,1), (2,5), (5,6), (8,3)]
    target_coordinates = [(1,3), (9,5), (4,6), (3,9)]
    prompt = resolution.generate_message().generate_prompt(coordinates, target_coordinates)
    
    user_message={"role": "user", "content": prompt}
    gpt().get_answer(user_message)
    
    
    

   }'