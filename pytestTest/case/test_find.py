import json
import requests
import os, sys
import pytest
sys.path.append(os.getcwd())
from utils.tokentools import save_token, read_token
from utils.dbtools import SSH_select


# def test_01_login():
#     u = "http://hapi.test.hualiantv.com/user/loginByCode"
#     d = {"mobile": "13694000445",
#          "code": "0000",
#          "platform": "h5"}
#     res = requests.post(url=u, data=d)
#     res_json = json.dumps(json.loads(res.text), indent=4, ensure_ascii=False)
#     assert res.status_code == 200
#     assert json.loads(res.text).get("errno") == 0
#     assert json.loads(res.text).get("errmsg") == "请求成功"
#     sql_ssh = "select * from user where rid = '{}'".format(d.get("mobile"))
#     assert len(SSH_select(sql_ssh)) != 0
#     token = json.loads(res.text)["data"]["user"]["token"]
#     save_token(res)
#     return token


def test_02_find():
    uids = []
    u = "http://live.test.hualiantv.com/publicRoomV2/RecommendAnchor/"
    p = {"token": read_token()}
    res = requests.get(url=u, params=p)
    res_json = json.dumps(json.loads(res.text), indent=4, ensure_ascii=False)
    a = json.loads(res.text)
    b = json.loads(res.text)["data"]["list"]
    for c in b:
        uids.append(c["uid"])
    print(uids)
    sql_ssh = "SELECT * from user_destroy_ub_bak where uid in %s" % str(tuple(uids))
    print(sql_ssh)
    assert len(SSH_select(sql_ssh)) == 0
    sql_ssh = "SELECT * from user_destroy_his where uid in %s" % str(tuple(uids))
    assert len(SSH_select(sql_ssh)) == 0
    sql_ssh = "select source from user where uid in %s" % str(tuple(uids))
    assert sql_ssh != "destroy"
