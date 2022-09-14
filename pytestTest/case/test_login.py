import json
import requests
import os, sys
sys.path.append(os.getcwd())
from utils.dbtools import SSH_select
from utils.tokentools import save_token, read_token


def test_01_login():
    u = "http://hapi.test.hualiantv.com/user/loginByCode"
    d = {"mobile": "13694000445",
         "code": "0000",
         "platform": "h5"}
    res = requests.post(url=u, data=d)
    res_json = json.dumps(json.loads(res.text), indent=4, ensure_ascii=False)
    assert res.status_code == 200
    assert json.loads(res.text).get("errno") == 0
    assert json.loads(res.text).get("errmsg") == "请求成功"
    sql_ssh = "select * from user where rid = '{}'".format(d.get("mobile"))
    assert len(SSH_select(sql_ssh)) != 0
    token = json.loads(res.text)["data"]["user"]["token"]
    save_token(res)
    return token


def test_02_lupin():
    u = "http://hapi.test.hualiantv.com/user/loginByCode"
    d = {"mobile": "13694000445",
         "code": "0000",
         "platform": "h5"}
    res = requests.post(url=u, data=d)
    res_json = json.dumps(json.loads(res.text), indent=4, ensure_ascii=False)
    assert res.status_code == 200
    assert json.loads(res.text).get("errno") == 0
    assert json.loads(res.text).get("errmsg") == "请求成功"
    sql_ssh = "select * from user where rid = '{}'".format(d.get("mobile"))
    assert len(SSH_select(sql_ssh)) != 0
    print(read_token())

