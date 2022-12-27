import json
import requests
import os, sys
import pytest
sys.path.append(os.getcwd())
from utils.tokentools import user_saveToken, anchor_saveToken
from utils.dbtools import SSH_select


def test_01_userLogin():
    u = "http://hapi.test.hualiantv.com/user/loginByCode"
    d = {"mobile": "13944443595",
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
    user_saveToken(res)
    return token


def test_02_anchorLogin():
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
    anchor_saveToken(res)
    return token
"""
活动，游戏中奖率，压测
注册登陆（三方登陆），私信  上下麦 弹幕，（付费弹幕，查库）。首页，动态页，
error_num


收送礼，加解密

"""