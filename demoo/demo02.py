import pymysql


def select(sql):  # 查询

    db = pymysql.connect(host="127.0.0.1",
                         user="root",
                         password="12345678",
                         db="test")

    cursor = db.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    db.close()
    return result


a = select("select * from user")
print(a)


def commit(xiugai):  # 修改、增加、删除
    db = pymysql.connect(host="127.0.0.1",
                         user="root",
                         password="12345678",
                         db="test")
    cursor = db.cursor()
    cursor.execute(xiugai)
    db.commit()
    db.close()
    return True


# xiugai = "insert into user value (11, '王麻子', 3)"
# b = commit(xiugai)
# print(b)