import json
import requests
import os, sys
import pytest
sys.path.append(os.getcwd())
from utils.tokentools import user_readToken, userTest_readToken, anchor_readToken, anchorTest_readToken
from utils.dbtools import SSH_select


def test_01_userTestFind():
    print("user")
    uids = []
    u = "http://live.test.hualiantv.com/publicRoomV2/RecommendAnchor/"
    p = {"token": userTest_readToken()}
    res = requests.get(url=u, params=p)
    res_json = json.dumps(json.loads(res.text), indent=4, ensure_ascii=False)
    a = json.loads(res.text)
    if len(a["data"]) != 0:
        b = json.loads(res.text)["data"]["list"]
        for c in b:
            uids.append(c["uid"])
        print(uids)
        sql_ssh = "SELECT * from user_destroy_ub_bak where uid in (%s)" % ",".join(uids)
        print(sql_ssh)
        assert len(SSH_select(sql_ssh)) == 0
        sql_ssh = "SELECT * from user_destroy_his where uid in (%s)" % ",".join(uids)
        assert len(SSH_select(sql_ssh)) == 0
        sql_ssh = "select source from user where uid in (%s)" % ",".join(uids)
        assert sql_ssh != "destroy"
    else:
        return


def test_02_anchorTestFind():
    print("anchor")
    uids = []
    u = "http://live.test.hualiantv.com/publicRoomV2/RecommendAnchor/"
    p = {"token": anchorTest_readToken()}
    res = requests.get(url=u, params=p)
    res_json = json.dumps(json.loads(res.text), indent=4, ensure_ascii=False)
    a = json.loads(res.text)
    if len(a["data"]) != 0:
        b = json.loads(res.text)["data"]["list"]
        for c in b:
            uids.append(c["uid"])
        print(uids)
        sql_ssh = "SELECT * from user_destroy_ub_bak where uid in (%s)" % ",".join(uids)
        print(sql_ssh)
        assert len(SSH_select(sql_ssh)) == 0
        sql_ssh = "SELECT * from user_destroy_his where uid in (%s)" % ",".join(uids)
        assert len(SSH_select(sql_ssh)) == 0
        sql_ssh = "select source from user where uid in (%s)" % ",".join(uids)
        assert sql_ssh != "destroy"
    else:
        return


def test_03_userFind():
    print("anchor")
    uids = []
    u = "http://live.hualiantv.com/publicRoomV2/RecommendAnchor/"
    p = {"token": anchorTest_readToken()}
    res = requests.get(url=u, params=p)
    res_json = json.dumps(json.loads(res.text), indent=4, ensure_ascii=False)
    a = json.loads(res.text)
    print(a)
    if len(a["data"]) != 0:
        b = json.loads(res.text)["data"]["list"]
        for c in b:
            uids.append(c["uid"])
        print(uids)
        sql_ssh = "SELECT * from user_destroy_ub_bak where uid in (%s)" % ",".join(uids)
        print(sql_ssh)
        # assert len(SSH_select(sql_ssh)) == 0
        # sql_ssh = "SELECT * from user_destroy_his where uid in (%s)" % ",".join(uids)
        # assert len(SSH_select(sql_ssh)) == 0
        # sql_ssh = "select source from user where uid in (%s)" % ",".join(uids)
        # assert sql_ssh != "destroy"
    else:
        return


def test_04_anchorFind():
    print("anchor")
    uids = []
    u = "http://live.hualiantv.com/publicRoomV2/RecommendAnchor/"
    p = {"token": anchorTest_readToken()}
    res = requests.get(url=u, params=p)
    res_json = json.dumps(json.loads(res.text), indent=4, ensure_ascii=False)
    a = json.loads(res.text)
    if len(a["data"]) != 0:
        b = json.loads(res.text)["data"]["list"]
        for c in b:
            uids.append(c["uid"])
        print(uids)
        sql_ssh = "SELECT * from user_destroy_ub_bak where uid in (%s)" % ",".join(uids)
        print(sql_ssh)
        # assert len(SSH_select(sql_ssh)) == 0
        # sql_ssh = "SELECT * from user_destroy_his where uid in (%s)" % ",".join(uids)
        # assert len(SSH_select(sql_ssh)) == 0
        # sql_ssh = "select source from user where uid in (%s)" % ",".join(uids)
        # assert sql_ssh != "destroy"
    else:
        return
