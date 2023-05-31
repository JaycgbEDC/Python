import pymongo


# 连接mongodb
client = pymongo.MongoClient(host = "localhost", port = 27017)

# 指定数据库(若不存在，则自动创建)
db = client.test

# 指定集合(若不存在，则自动创建)
collection = db.students

# # 插入文档
# student = {
#     "id": "2015",
#     "name": "wike",
#     "age": 15,
#     "gender": "male"
# }
# student1 = {
#     "id": "2018",
#     "name": "bob",
#     "age": 18,
#     "gender": "female"
# }
# student2 = {
#     "id": "2023",
#     "name": "kribe",
#     "age": 23,
#     "gender": "male"
# }
# student3 = {
#     "id": "2023",
#     "name": "jorge",
#     "age": 23,
#     "gender": "female"
# }
# result1 = collection.insert_one(student)  # 插入单条数据
# result2 = collection.insert_many([student1, student2, student3])  # 插入多条数据
# print(result1.inserted_id)
# print(result2.inserted_ids)

# # 查询文档（可用正则表达式）
# result3 = collection.find_one({"name": "wike"})  # 查询单一文档
# print(result3)
# results = collection.find({"age": 23})  # 查询多个文档
# for result in results:
#     print(result)

# # 计数
# count = collection.count_documents({"age": {"$gt": 17}})
# print(count)

# # 排序
# results = collection.find().sort("name", pymongo.DESCENDING)
# print([result["name"] for result in results])

# 偏移

# # 更新法一：更新一条数据
# condition = {"name": "wike"}
# result = collection.update_one(condition, {"$set": {"name": "wikkke"}})
# print(result)
# print(result.matched_count, result.modified_count)

# # 更新法二：更新所有满足条件数据
# condition = {"age": {"$gt": 15}}
# result = collection.update_many(condition, {"$inc": {"age": 1}})  # 所有大于15的文档，年龄加1
# print(result)
# print(result.matched_count, result.modified_count)

# 删除
result1 = collection.delete_one({"name": "wikkke"})
print(result1)
print(result1.deleted_count)
result2 = collection.delete_many({"age": {"$lt": 30}})
print(result1.deleted_count)