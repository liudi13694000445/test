import requests

"""
    requests.request.post方法
"""
u = "http://hapi.test.hualiantv.com/user/loginByCode"
d = {"mobile": "13694000445",
        "code": "0000",
        "platform": "h5"}

res = requests.request("post", url=u, data=d)
print(res.text)

print("_" * 50)
"""
    requests.request.get方法
"""
url = "https://admin-cpa.test.hualiantv.com/belong/getList"
respones = requests.request("get", url=url)
print(respones.text)