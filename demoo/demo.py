import requests

url="https://admin-cpa.test.hualiantv.com/userCenter/me"
data = {"nackname":56,
        "username": 56,
        "role_type": 0}

res = requests.post(url=url, data=data)
v
print(res.text)