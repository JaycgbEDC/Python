import pymysql


db = pymysql.connect(host = "localhost", user = "root", password = "2000lixiao", port = 3306, db = "spiders")
cursor = db.cursor()

# # 创建数据库spiders
# cursor.execute("create database spiders default character set utf8mb4")

# # 创建学生表，并写入值
# sql1 = '''
#     create table if not exists students(
#     id varchar(255) not null,
#     name varchar(255) not null,
#     age int not null,
#     primary key (id)
#     )
# '''
# cursor.execute(sql1)

# # 插入数据法1：
# sql2 = '''
#     insert into students(id, name, age) values(%s, %s, %s)
# '''
# id, user, age = "2018", "kribe", 20
# # 异常机制保证数据的一致性
# try:
#     cursor.execute(sql2, (id, user, age))
#     db.commit()
# except:
#     db.rollback()

# # 插入数据法2（推荐, 包含了更新）：
# data = {
#     "id": "2023",
#     "name": "wike",
#     "age": 23
# }
# table = "students"
# keys = ', '.join(data.keys())
# values = ', '.join(['%s'] * len(data))
# sql3 = f'''
#     insert into {table}({keys}) values({values}) on duplicate key update
# '''
# update = ', '.join([f"{key} = %s" for key in data])  # 若主键存在则执行更新操作
# sql3 += update
# try:
#     if cursor.execute(sql3, tuple(data.values()) * 2):
#         print("sucessful")
#         db.commit()
# except:
#     print("failed")
#     db.rollback()

# # 删除数据：
# table = "students"
# conditions = "age > 21"
# sql4 = f'''
#     delete from {table} where {conditions}
# '''
# try:
#     cursor.execute(sql4)
#     db.commit()
# except:
#     db.rollback()

# 查询数据：
sql5 = '''
    select * from students where age >= 20
'''
try:
    cursor.execute(sql5)
    print(f"Count: {cursor.rowcount}")  # 查询结果的条数
    row = cursor.fetchone()  # 取一条数据，cursor移到下一行；也可用fetchall取所有
    while row:
        print(f"Row: {row}")
        row = cursor.fetchone()
except:
    print("error")

db.close()