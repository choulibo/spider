{ "_id" : null,
  "name" : [
            { "_id" : ObjectId("5bcd7ec6ac9ecbe3ea7fcceb"), "name" : "郭靖", "hometown" : "蒙古", "age" : 20, "gender" : true },
            { "_id" : ObjectId("5bcd7ec6ac9ecbe3ea7fccec"), "name" : "⻩蓉", "hometown" : "桃花岛", "age" : 18, "gender" : false },
            { "_id" : ObjectId("5bcd7ec6ac9ecbe3ea7fcced"), "name" : "华筝", "hometown" : "蒙古", "age" : 18, "gender" : false },
            { "_id" : ObjectId("5bcd7ec6ac9ecbe3ea7fccee"), "name" : "⻩药师", "hometown" : "桃花岛", "age" : 40, "gender" : true },
            { "_id" : ObjectId("5bcd7ec6ac9ecbe3ea7fccef"), "name" : "段誉", "hometown" : "⼤理", "age" : 16, "gender" : true },
            { "_id" : ObjectId("5bcd7ec6ac9ecbe3ea7fccf0"), "name" : "段王爷", "hometown" : "⼤理", "age" : 45, "gender" : true },
            { "_id" : ObjectId("5bcd7ec6ac9ecbe3ea7fccf1"), "name" : "洪七公", "hometown" : "华⼭", "age" : 18, "gender" : true }
          ]
}


db.te.aggregate({$match:{age:{$gt:20}}})

db.te.aggregate(
  {$match:{age:{$gte:18}}
  {$group:{_id:"$gender",counter:{$sum:1}}}
)
