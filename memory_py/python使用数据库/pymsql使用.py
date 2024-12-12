import pymysql

conn = pymysql.connect(
    user='root',
    passwd='root',
    host='127.0.0.1',
    database='bysq',
    port=3306,
    autocommit=True
)

home417 = conn.cursor()#必须先使用cursor() 游标之后才可以使用数据库操作

home417.execute('select * from home417;')


result = home417.fetchall()
print(result)

home417.execute("insert into home417 values('zx',666,'扣')")

home417.close()
conn.close()