import pymysql


def select(sql):

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