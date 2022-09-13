import pymysql


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



