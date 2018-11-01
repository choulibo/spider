### MongoDB 高级查询

#### 数据查询

- db.col.find({查询条件})
- db.col.findOne({查询条件})   # 返回一条
- db.col.find({查询条件}).pretty()  # pretty() 更加人性化的显示数据

##### 1. 比较运算符

- 等于: 默认是等于判断
- 小于:$lt (less than)
- 小于等于:$lte (less than equal)
- 大于:$gt (greater than)
- 大于等于:$gte (greater than equal)
- 不等于: $ne 

##### 2.逻辑运算符

- and: 在json中写多个条件即可,用都好隔开;

  `and :{name:"",age:""} 此时name和age表示and的逻辑`

- or: 使用$or ,值是数组,数组中每个元素为json

  ```Python
  db.stu.find({$or:[{age:{$gt:18}},{gender:fasle}]})      # 查询年龄大于18,或性别为false的学生
  ```

##### 3.范围运算符

- 使用$in ,$nin 判断是否为某个数组中

  ```python
  db.stu.find({age:{$in:[18,28,38]}})  # 查询年龄为18,28 的学生
  ```

##### 4.正则表达式

- 使用// 或$regex编写正则表达式

  ```Python
  db.products.find({sku:/^abc/})  # 查询sku以abc开头的数据
  db.products.find({sku:{$regex:"789$"}})   # 查询sku中以789结尾的数据
  ```

##### 6.skip( ) 和 limit( ) 方法

- limit()方法:用于读取指定数量的文档

  ```python
  db.col.find().limit(2)   # 查询2条数据
  ```

- skip()方法:用于跳过指定数量的文档

  ```Python
  db.stu.find().skip(2)   # 跳过2条数据
  # 同时使用
  db.stu.find().limit().skip()
  # 或
  db.stu.find().skip().limit()  # 先使用skip后使用limit效率更高
  ```

##### 7.投影

- 在查询到的返回结果中,只选择必要的字段

  `db.clo.find({ },{ 字段名称:1,....})`   值1 表示显示,0 表示不显示,对于_id列默认是显示的,如果不显示,设置值0

  ```python
  db.stu.find({ },{_id:0,gender:1})  # gender 显示,_id不显示
  ```

##### 8.排序

- 方法sort() 用于对集合进行排序

  `db.clo.find().sort({ 字段:1,....})`

  ```Python
  db.stu.find().sort({ gnder:-1,age:1})  # 根据性别升序,再根据年龄降序
  ```

  ##### 9.统计个数

- count() 用于统计结果集中文文档条数

  `db.clo.find({ 条件 }).count({ 条件 })或db.col.count({ 条件 })`

  ```Python
  db.stu.find({gender:true}).count()  # 统计男性数
  db.stu.count({age:{$gt:20},gender:true})   # 统计年龄大于20岁的男性
  ```

##### 10.消除重复

- distinct() 方法对数据进行去重

  `db.clo.distinct('去重字段',{条件})`

  ```Python
  db.stu.distinct('hometown',{age:{$gt:18}})  # 根据hometown去重,并且年龄大于18岁的数据
  ```

##### 11.自定义查询

- mongo 的shell 是一个js的执行环境,使用$where后面写一个函数,返回满足条件的数据

  ```js
  db.stu.find({
      $where:function(){
          // 查询年龄大于30 的学生
          return this.age>30;
      }
  })
  ```

### mongodb的聚合操作

聚合(aggregate)是基于数据处理的聚合管道,每个文档通过一个由多个阶段(stage)组成的管道,可以对每个阶段的管道进行分组,过滤等功能,然后经过一系列的处理,输出响应的结果.

语法:db.clo.aggegrate({管道:{表达式}},...)

#### 常用的管道

- $group: 将集合中的文档分组,可以统计结果;

  ```js
  db.stu.aggegrate(
  	($group:
  		{
  			_id:"$gender",
  			counter:{$sum:1}
  		}
  	)
  )
  ```

  - 其中,db_name.aggregate() 是语法,所有的管道命令都需要写在其中;
  - _id 表示分组的依据,表示根据那个字段进行分组;
  - counter:{$sum:1} 表示用表达式处理文档输出
  - 特别注意**_id:null** 表示不指定分组的字段,即统计整个文档

- $match: 过滤数据,只能输出符合条件的文档;

  对数据进行过滤,能够在聚合操作中使用的命令,和find区别是$match可以把结果交给下一个管道处理,而find不行

  ```js
  // 查询年龄大于20 的学生
  db.te.aggregate(
      {$match:{$gt:20}},
  )
  
  // 查询年龄大于20 的男女学生的人数
  db.stu.aggregate(
       {$match:{age:{$gt:20}}
       {$group:{_id:"$gender",counter:{$sum:1}}}
       )
  ```

- $projects: 修改输入文档的结构,如重命名,增加,删除字段.创建计算结果;

  ```js
  //  查询学生的年龄、姓名，仅输出年龄姓名
  db.stu.aggregate(
       {$project:{_id:0,name:1,age:1}}
       )
  
  // 查询男女人数,输出人数
  db.stu.aggregate(
       {$group:{_id:"$gender",counter:{$sum:1}}}
       {$project:{_id:0,counter:1}}
       )
  ```

- $sort: 将输入的文档排序后输出;

  ```js
  //查询学生信息，按照年龄升序
  db.stu.aggregate({$sort:{age:1}})
  ```

- $limit: 限制聚合管道返回的文档数;

- $skip: 跳过指定数量的文档,返回余下的文档;

  - 同时使用时先使用skip在使用limit ,效率更高

    ```js
    // 统计男女生人数，按照人数升序，返回第二条数据
    db.stu.aggregate(
         {$group:{_id:"$gender",counter:{$sum:1}}},
         {$sort:{counter:-1}},
         {$skip:1},
         {$limit:1}
     )
    ```

#### 常用表达式

 表达式:处理输入的文档并输出  语法:表达式: ' **$列名** '  常用表达式

- $sum : 计算总和,$sum:1 表示一倍计数;

- $avg : 计算平均值;

- $min : 获取最小值;

- $max : 获取最大值;

- $push : 在结果中插入值到一个数组中;

   **数据透视**

  ​	正常情况在统计的不同性别的数据的时候，需要知道所有的name，需要逐条观察，如果通过某种方式把所有的name放到一起，那么此时就可以理解为数据透视

  ```js
  // 统计不同性别的学生 
  db.te.aggregate(
       {$group:
           {
               _id:null,
               name:{$push:"$name"}
           }
       }
   )
  ```

  ```js
  // 将整个文档放入数组中 
  db.te.aggregate(
       {$group:
           {
               _id:null,
               name:{$push:"$$ROOT"}
           }
       }
   )
  ```

### Mongodb索引

#### mongodb 的索引的作用

-  加快查询速度
- 进行数据的去重

#### mongodb 的创建

- db.clo.ensureIndex({属性:1})  , 1 表示升序,-1 表示降序
- db.clo.createIndex({属性:1})

#### 索引的查看

db.col.getIndexes()  # 查看索引

#### 创建唯一索引

- db.clo.createIndex({属性:1},{"unique":true})  # 创建唯一索引

#### 删除索引

db.col.dropIndex({"索引名称":1})

#### 建立复合索引

- 在进行数据去重的时候，可能用一个字段来保证数据的唯一性，这个时候可以考虑建立复合索引来实现。
- 建立复合索引:db.colensureIndex({字段1:1,字段2:1})
- 根据需要选择是否建立唯一索引
- 索引字段是升序还是降序在单个索引的情况下不影响查询速度,但是带复合索引的条件下会有影响

### Mongodb的备份和恢复

#### 备份

备份的语法: mongodump -h dbhost -d dbname -o dbdirrectory       # 从数据库到本地

- -h : 服务器地址,也可以指定端口号
- -d : 需要备份的数据库名
- -0 : 备份的数据存放位置,此目录中存放的备份出来的数据   实例 :mongodump -h 192.168.196.128:27017 -d test1 -o ~/Desktop/test1bak

####  恢复

恢复的语法: mongorestore -h dbhost -d dbname --dir dbdirectory    # 从本地到数据库

- -h : 服务器的地址
- -d : 需要恢复的数据库实例
- --dir : 备份数据所在位置 实例:mongorestore -h 192.168.196.128:27017 -d test2 --dir ~/Desktop/test1bak/test1

### Mongodb和Python的交互

使用pymongo模块: pip install pymongo

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 18-10-23  @Author:libo  @FileName: 01_try_pymongo.py

from pymongo import MongoClient

# db = MongoClient().test18
# db.insert_many(i["name"]:)
client = MongoClient()
collections = client['test18']['t1']

# -----------------------------------------
# 插入一条数据
# client = MongoClient(host="127.0.0.1",port=27017)
#
# collection = client['test17']['t1']
# 创建一个db变量
# 通过.来获取数据库,方便在终端执行
# db = MongoClient().test17
# # 使用db变量.集合名.方法来操作数据库
# db.user.insert_many({"userbame": "zhangsan", "password": "zhansan123"})
# ret = db.user# for i in ret:
#     print(i)

# -----------------------------------------
# # 插入多条数据
# # db = MongoClient().test18
# # db.insert_many(i["name"]:)
# client = MongoClient()
# collections = client['test18']['t1']
# # temp_list = [{"_id":i,"py_{}".format(i)} for i in range(100)]
# temp_list = [{"name": "py{}".format(i)} for i in range(20)]
# ret = collections.insert_many(temp_list)
#
# t = collections.find_one({"name":"py17"})
# # # for r in ret:
# # print(ret)
# print(t)

# -----------------------------------------

# # 更新一条数据
# ret = collections.update_one({"name":"py17"},{"$set":{"name":"py170"}})
#
# t = collections.find_one({"name":"py170"})
# print(t)

# -----------------------------------------
# 更新多条数据
# ret = collections.update_many({"name": "py170"}, {"$set": {"name": "pyy170"}})
#
# t = collections.find()
# for ty in t:
#     print(ty)


# # 删除1条数据
# ret = collections.delete_one({"name": "pyy170"})
#
# t = collections.find()
# for ty in t:
#     print(ty)

# 删除多条数据
ret = collections.delete_many({"name": "py0"})

t = collections.find()
for ty in t:
    print(ty)
```

