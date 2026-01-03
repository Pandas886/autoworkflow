import requests

# 目标URL
url = "https://cloudstudio.net/api/billing/activityTask/SIGN_IN_2025Q3/_reward"

# 请求头
headers = {
    "accept": "application/json",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "origin": "https://cloudstudio.net",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://cloudstudio.net/user-center",
    "sec-ch-ua": '"Microsoft Edge";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "traceparent": "00-657ce2855bf8323872ea464f4f38c54d-660ca8c905de87b9-01",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36 Edg/143.0.0.0",
    "x-requested-with": "XMLHttpRequest",
    "x-xsrf-token": "460945652"
}

# Cookies（重要：请替换为你自己的有效会话cookie）
cookies = {
    "cloudstudio-session-team": "wx",
    "cloudstudio-session": "362c4433-9032-48ba-9e78-ca559c3fcbd5.49c81efb-1f66-4147-8efa-e4909f6a0f23.2ecef21e-51f8-4ce4-91d4-340d1277407f"
}

# 发送POST请求（content-length: 0 表示无请求体）
try:
    response = requests.post(url, headers=headers, cookies=cookies, timeout=10)
    
    # 打印响应信息
    print(f"状态码: {response.status_code}")
    print(f"响应头: {response.headers.get('content-type')}")
    print(f"响应内容: {response.text}")
    
    # 如果返回JSON格式
    if response.status_code == 200:
        try:
            json_data = response.json()
            print(f"JSON数据: {json_data}")
        except ValueError:
            print("响应不是有效的JSON格式")

except requests.exceptions.RequestException as e:
    print(f"请求发生错误: {e}")
