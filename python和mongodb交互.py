#python和mongodb的交互
#　ｐip3 install pymongo

import pymongo
from bson.objectid import ObjectId
#import  +++++++++++++++++++++++++++

#创建mongo客户端的链接
mongoConn=pymongo.MongoClient('localhost',27017)  #端口号必须会ｉｎｔ类型的
#第二种链接方式 >>
#mongoConn=pymongo.MongoClient('mongodb://localhost:27017')

###有用户登录的连接方式：   mongConn = pymongo.MongoClient('mongodb://user:')+++++++++++++++++++++++++++++++

####操作数据库下的集合

#首先拿到数据库
#user_db = mongoConn.数据库名称
user_db = mongoConn.jobs
#第二种拿到数据库的方法
#user_db = mongoConn['jobs']

#获取数据库下要操作的集合
user_col = user_db.jobdesc
#获取数据库下要操作的集合的第二种方式
#user_col = user_db['jobdesc']

#文档的操作
#增
def add_data():
    document = {
        'name' : '李荣',
        'age':'20',
        'gender' : '男',
        'class' : '1804'
    }
    document1 = {
        'name' : '李华',
        'age':'20',
        'gender' : '男',
        'class' : '1804'
    }
    #result = user_col.insert(document) #插入单条 user_col.insert_one(document)
    result1 = user_col.insert([document,document1])  #插入多条  user_col.inset_many([document,document1])
    #print(result)   #返回插入数据对应的id
    print(result1)    #返回插入数据对应的id，返回的是一个列表，包含多个内容的id
    
#add_data()

#改
def update_data():
    result = user_col.update({'name':'李华'},{'$set':{'name':'++++++++++++'}})  #默认是 修改第一条 命令行中的更新全文档 result = user_col.update({'name':'李华'},{'$set':{'name':'++++++++++++'}},{multi:true})
    #result1 = user_col.update({'name':'李华'},{'name':'--------------'})   #全文档跟新，替换内容
    #更新全部的对应条件的全部内容
    #result2 = user_col.update_many({'name':'李华'},{'$set':{'name':'++++++++++++'}})   #更新全部的内容，

    #使用save更新
    result = user_col.save({"_id:Object('5b836dc441248b27d997dc13')",'name':'++++++++++++'})  #使用id的时候，要导入一个bson格式的模块 ，这个也是全文当更新
    print(result)
#update_data()

#查
def select():
    #find查询，会返回一个cursor 对象，要拿到数据就要遍历这个对象
    result = user_col.find_one({'name':'李荣'})   #只返回一条
    result = user_col.find({'name':'李荣'}) #返回全部，需要用到下面的遍历
    #print(result)
    #print([i for i in result])

    #跳过和限制查询
    result  = user_col.find({}).limit(4).skip(2).sort('age',-1)  #通过单个排序
    result  = user_col.find({}).limit(4).skip(2).sort([('age',-1),('name',1)])     +++++++++++++++++++++++++++++++
    print([i for i in result])

#select()

#删除
def drop():
    #删除一条
    result = user_col.delete_one({})
    result = user_col.remove({},multi:False)   #删除一条
    #删除多条
    result = user_col.delete_many({})
    result = user_col.remove({})
