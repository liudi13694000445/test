import json
import requests

"""
    get方法
        headers：定制请求头（headers），例如：content-type = application/x-www-form-urlencoded
        params：用于传递测试接口所要用的参数，这里我们用python中的字典形式（key：value）进行参数的传递。post请求这个参数为data
        timeout：设置接口连接的最大时间（超过该时间会抛出超时错误）
"""
url = "https://admin-cpa.test.hualiantv.com/belong/getList"
result = requests.get(url)  #
a = json.loads(result.text)  # 把json字符串转换成python数据类型
# print(json.dumps(a, indent=4, ensure_ascii=False))  # indent：输出的缩紧。ensure_ascii=False：不使用ascii格式，dumps方法必须传python数据类型
#
# print("-" * 50)
"""
    post方法
"""
u = "http://activity.test.hualiantv.com/midAutumnDay/home"
d = {"token": "YmICYlyzY0eNClFVKQ--JxfABjualujj4bd5"}
res = requests.post(url=u, data=d)
ac = json.loads(res.text)
b = json.dumps(ac, indent=4, ensure_ascii=False)
print(b)


# login
url = "http://hapi.test.hualiantv.com/user/loginByCode"
data = {"mobile": "13694000445",
        "code": "0000",
        "platform": "h5"}