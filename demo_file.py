import pymysql

# def mysql():

db = pymysql.connect(host="rm-2ze61bh4321555111.mysql.rds.aliyuncs.com", user="root", password="poiuy)(*&^123", db="chengdu_password")
cursor = db.cursor()
print(cursor)