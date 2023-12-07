import requests
import time
import json

refresh_token = "20505a7ec3bb4f8a9a9c960b170fab27"

data = requests.post("https://auth.aliyundrive.com/v2/account/token",
                     data=json.dumps({
                         "grant_type": "refresh_token",
                         "refresh_token": refresh_token
                     }),
                     headers={'Content-Type': 'application/json'})
data = json.loads(data.text)
access_token = data['access_token']
phone = data["user_name"]

access_token2 = 'Bearer ' + access_token

# data2 = requests.post("https://member.aliyundrive.com/v1/activity/sign_in_list",
#                       data=json.dumps({"_rx-s": "mobile"}),
#                       headers={"Authorization": access_token2})


import requests

url = 'https://member.aliyundrive.com/v2/activity/sign_in_list'
headers = {
    'authority': 'member.aliyundrive.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'authorization': access_token2,
    'content-type': 'application/json',
    'origin': 'https://www.aliyundrive.com',
    'referer': 'https://www.aliyundrive.com/',
    'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
    'x-canary': 'client=web,app=adrive,version=v4.9.0',
    'x-device-id': 'Bhc8HTyO5FYCASvP1F28INZe',
    'x-signature': 'a5a761c8f52fc2345d01b4eda1d2d4820f5dd997feeca12b361c8f1551dddde05f32d5bae8f39df24caa29a26039a55895b4e2bdbd1d17fb39cdc9f42ac77b8400'
}

data = {}

data2 = requests.post(url, headers=headers, json=data)


data2 = json.loads(data2.text)
signin_count = data2['result']['signInCount']

time.sleep(3000)

# data3 = requests.post(
#     "https://member.aliyundrive.com/v1/activity/sign_in_reward?_rx-s=mobile",
#     data=json.dumps({"signInDay": signin_count}),
#     headers={"Authorization": access_token2})


import requests

url = 'https://member.aliyundrive.com/v1/activity/sign_in_reward'
headers = {
    'authority': 'member.aliyundrive.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'authorization': access_token2,
    'content-type': 'application/json',
    'origin': 'https://www.aliyundrive.com',
    'referer': 'https://www.aliyundrive.com/',
    'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
    'x-canary': 'client=web,app=adrive,version=v4.9.0',
    'x-device-id': 'Bhc8HTyO5FYCASvP1F28INZe',
    'x-signature': '6bfc1bf7580312218e99c8365f19d88972ab6d8ff3ec6dc4b43809d652e3ecdc4e814cb9cf74c156c08b335548ec2eba9571000e3c9a2395a1226e2df590b56000'
}


data3 = requests.post(url, headers=headers, json={
    'signInDay': '1'
})


data3 = json.loads(data3.text)

print("签到成功，本月累计签到", signin_count, "天")
print("本次签到获得", data3["result"]["name"], "，", data3["result"]["description"])
