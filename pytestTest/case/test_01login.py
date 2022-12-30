import json
import requests
import os, sys
import pytest
sys.path.append(os.getcwd())
from utils.tokentools import userTest_saveToken, anchorTest_saveToken, user_saveToken, anchor_saveToken
from utils.dbtools import SSH_select
import hashlib


#  测试环境用户登陆
def test_01_testUserLogin():
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
    userTest_saveToken(res)
    return token


#  测试环境主播登陆
def test_02_testAnchorLogin():
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
    anchorTest_saveToken(res)
    return token


#  线上用加密password方法
def after_md5(pwd):
    """实现md5加密"""
    # 实例化md5
    vmd5 = hashlib.md5()
    # 对原文进行md5加密运算
    vmd5.update(pwd.encode('utf-8'))
    # 输出密文
    return vmd5.hexdigest()


password = after_md5('123456')
# print(password)


#  线上环境用户登陆
def test_03_userLogin():
    u = "http://passport.test.hualiantv.com/user/login"
    d = {"guid": "38d034286665f2042589460bed6ecc5d",
         "time": "1672309999",
         "rand": "1608060452",
         "netspeed": "0",
         "dui": "1F1F1DF9-48DC-41CA-ACCE-A3F3BEF9BFEA",
         "sv": "16.1.1",
         "smid": "1F1F1DF9-48DC-41CA-ACCE-A3F3BEF9BFEA",
         "channel": "Apple",
         "lng": "0.000000",
         "version": "1.11.20",
         "clientip": "",
         "deviceid": "1F1F1DF9-48DC-41CA-ACCE-A3F3BEF9BFEA",
         "platform": "ios",
         "ios_bundleid": "com.huayin.hualian",
         "product": "hualian",
         "lat": "0.000000",
         "network": "Wi-Fi",
         "model": "iPhone10,1",
         "deviceModel": "iPhone8",
         "sm_deviceid": "2019051615024550a43d5731e76e3386a37936d4beb3eb0169de22de2862c7",
         "no_sign": "1",
         "mobile": "13694000445",
         "password": "%s" % password}
    res = requests.post(url=u, data=d)
    res_json = json.dumps(json.loads(res.text), indent=4, ensure_ascii=False)
    # print(res_json)
    assert res.status_code == 200
    assert json.loads(res.text).get("errno") == 0
    sql_ssh = "select * from user where rid = '{}'".format(d.get("mobile"))
    assert len(SSH_select(sql_ssh)) != 0
    token = json.loads(res.text)["data"]["token"]
    user_saveToken(res)
    return token
"""
活动，游戏中奖率，压测
注册登陆（三方登陆），私信  上下麦 弹幕，（付费弹幕，查库）。首页，动态页，
error_num


收送礼，加解密

"""