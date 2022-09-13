import pymysql

db = pymysql.connect(host="127.0.0.1",  # 地址
                     user="root",  # 用户名
                     password="12345678",  # 密码
                     db="test")  # 需要连接的库

cursor = db.cursor()  # 获取游标=查询窗口

sql = "select * from user"  # sql语句
cursor.execute(sql)  # 执行sql语句

result = cursor.fetchall()  # 得到返回结果
print(result)

db.close()  # 关闭
