from tools import chaxun, commit

q = input(":")
w = input(":")
e = input(":")

sql_commit = "insert into user value ({}, '{}', {})".format(q, w, e)
r = commit(sql_commit)
if r is True:

    t = chaxun("select name from user order by id desc limit 1")
    print(t)
    print("okokkok!")
    if t == w:
        print("okokok")
    else:
        print("323232")
else:
    print("nononno!")


sql_chaxun = "select * from user"
a = chaxun(sql_chaxun)
print(a)
