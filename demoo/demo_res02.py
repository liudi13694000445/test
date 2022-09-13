import json
import requests
from tools import SSH_select

u = "http://hapi.test.hualiantv.com/user/loginByCode"
d = {"mobile": "13694000445",
        "code": "0000",
        "platform": "h5"}

res = requests.post(url=u, data=d)
a = json.dumps(json.loads(res.text), indent=4, ensure_ascii=False)  # 使用json包转换返回结果的展示
# print(a)
assert res.status_code == 200
print(200)
assert json.loads(res.text).get("errno") == 0
print(0)
assert json.loads(res.text)["errmsg"] == "请求成功"
print("6666")

sql_ssh = "select * from user where rid = '{}" .format(d.get("mobile"))
o = SSH_select(sql_ssh)
# print(o)
assert o != 0
print("999")
