import http.client

## 脚本用于zeabur网站7天试用延长

# 接口1
conn = http.client.HTTPSConnection("gateway.zeabur.com")

payload = "{\"operationName\":\"CheckIn\",\"variables\":{},\"query\":\"mutation CheckIn {\\n  checkIn\\n}\"}"

headers = {
    'authority': "gateway.zeabur.com",
    'accept': "*/*",
    'accept-language': "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    'authorization': "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJ6ZWFidXIiLCJqdGkiOiI2NGI4ZTZiNTc1YjkyNTQ4MjYyMWRkZWQxNjg5ODM5Mjg2IiwiaWF0IjoxNjg5ODM5Mjg2LCJzdWIiOiI2NGI4ZTZiNTc1YjkyNTQ4MjYyMWRkZWQiLCJmcm9tIjoiemVhYnVyIiwic2NvcGUiOiJhbGwifQ.sCxg-xwEdCUr3lNuJXV6wLBcXctFlFnf25sgEf4coiM",
    'content-type': "application/json",
    'origin': "https://dash.zeabur.com",
    'referer': "https://dash.zeabur.com/",
    'sec-ch-ua': 'Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': "?0",
    'sec-ch-ua-platform': "Windows",
    'sec-fetch-dest': "empty",
    'sec-fetch-mode': "cors",
    'sec-fetch-site': "same-site",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0",
    'Accept-Encoding': "deflate, gzip"
    }

conn.request("POST", "/graphql", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

## 接口2
# url = 'https://gateway.zeabur.com/graphql'
# headers = {
#     'authority': 'gateway.zeabur.com',
#     'accept': '*/*',
#     'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
#     'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJ6ZWFidXIiLCJqdGkiOiI2NGI4ZTZiNTc1YjkyNTQ4MjYyMWRkZWQxNjg5ODM5Mjg2IiwiaWF0IjoxNjg5ODM5Mjg2LCJzdWIiOiI2NGI4ZTZiNTc1YjkyNTQ4MjYyMWRkZWQiLCJmcm9tIjoiemVhYnVyIiwic2NvcGUiOiJhbGwifQ.sCxg-xwEdCUr3lNuJXV6wLBcXctFlFnf25sgEf4coiM',
#     'content-type': 'application/json',
#     'origin': 'https://dash.zeabur.com',
#     'referer': 'https://dash.zeabur.com/',
#     'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     'sec-fetch-dest': 'empty',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-site': 'same-site',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'
# }
#
# data = {
#     'operationName': 'GetProfile',
#     'variables': {},
#     'query': 'query GetProfile {\n  me {\n    _id\n    language\n    avatarURL\n    username\n    agreedAt\n    discount {\n      amountOff\n      id\n      name\n      percentOff\n      __typename\n    }\n    bannedReason\n    name\n    emailPreference\n    email\n    lastCheckedInAt\n    discordID\n    paymentMethod {\n      ... on Card {\n        type\n        brand\n        last4\n        __typename\n      }\n      ... on Alipay {\n        type\n        __typename\n      }\n      __typename\n    }\n    subscription {\n      plan\n      nextBillingAt\n      __typename\n    }\n    currency\n    __typename\n  }\n}'
# }
#
# response = requests.post(url, headers=headers, json=data)
#
# print(response.text)
