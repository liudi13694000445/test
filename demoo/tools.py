# -*- coding:utf-8 -*-
import pymysql
from sshtunnel import SSHTunnelForwarder


def chaxun(sql_chaxun):
    db = pymysql.connect(host="127.0.0.1",
                         user="root",
                         password="12345678",
                         db="test")
    cursor = db.cursor()
    cursor.execute(sql_chaxun)
    result = cursor.fetchall()
    db.close()
    return result


def commit(sql_commit):
    db = pymysql.connect(host="127.0.0.1",
                         user="root",
                         password="12345678",
                         db="test")
    cursor = db.cursor()
    cursor.execute(sql_commit)
    db.commit()
    db.close()
    return True


def SSH_select(sql_ssh):
    with SSHTunnelForwarder(
            ('39.105.70.142', 22),  # 指定ssh登录的跳转机的address，端口号
            ssh_username="liudi",  # 跳转机的用户名
            ssh_pkey="/Users/huafang/.ssh/id_rsa",  # 私钥路径
            ssh_private_key_password="",  # 跳转机的用户密码
            remote_bind_address=(
            'rm-2ze61bh4321555111.mysql.rds.aliyuncs.com', 3306)) as server:  # mysql服务器的address，端口号
        db = pymysql.connect(host='127.0.0.1',  # 此处必须是是127.0.0.1
                             port=server.local_bind_port,
                             user='root',  # 数据库用户名
                             passwd='poiuy)(*&^123',  # 数据库密码
                             db='chengdu_passport'  # 数据库名称
                             )

        cursor = db.cursor()
        # 使用 execute()  方法执行 SQL 查询
        cursor.execute(sql_ssh)

        # 使用 fetchone() 方法获取单条数据.
        data = cursor.fetchall()

        # print(data)
        # 关闭数据库连接
        cursor.close()
        return data
