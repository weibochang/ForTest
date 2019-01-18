#redis 与 python的交互
#sudo pip3 install redis

#python 与 redis 交互获得的内容都是二进制编码的内容，想要正常显示一般需要解码 如：print(result.decode('utf8'))

#from redis import *
import redis
import time

#创建链接(两种链接方式)
redis_conn = redis.StrictRedis(host='localhost',port='6379',db=1)
#redis_conn = redis.Redis()

#字符串的操作
# string
#操作的类型：set,setex,mset,append,get,mget,key
def do_string():
     #存入单个
     name = '常'
     age = 18
     redis_conn.set(name,age)
     #存入多个值
    #  redis_conn.mset({'1804':'26','1805':'39'})
     #取出对应的数据
    #  result = redis_conn.get('age')
    #  print(result.decode('utf8'))    #取出的 数据是二进制的格式，取出数据是需要转码  result.decode('utf8')  解码
    #  a = result.decode('utf8')
    #  print(type(a))
    #  #取多个值
    #  result = redis_conn.mget(['1804','1804'])
    #  print(result)
     #设置过期时间
    #  result = redis_conn.setex('1804',30,'new')
    #  print(result)  # 返回一个 boolean值
     #拼接
    #  result = redis_conn.append('1805','new')
    #  print(result)   #返回 追加之后的总长度
     #查看某个键对应长度的
    #  result = redis_conn.strlen('1805')
    #  print(result)   #返回对应键的长度
     #删除key
    #  result = redis_conn.delete('1805')  #可以删除多个键
    #  print(result)  #返回 0 或 1 
   

# #keys
# #操作的类型：exists,type,delete,expire,getrange,ttl
# def do_key():
#     #pattern = '*'  表示正则
#     # keys = redis_conn.keys()  #获取数据库中所有的（符合条件）的键,返回的是一个列表的类型,可以传入一个正则表示式
#     # print(keys)
    
#     # #判断某个键是否存在
#     # result = redis_conn.exists('zas')
#     # print(result)

#     # #判断值的类型
#     # result = redis_conn.type('age')
#     # print(result)

#     # #设置过期时间
#     # result = redis_conn.expire('age',30)
#     # print(result)

#     # #查看存活时间
#     # result = redis_conn.ttl('age')
#     # print(result)

#     #指定
#     result = redis_conn.getrange('name',3,5)
#     print(result)

# #哈希操作
# #hash
# #操作的类型：hset,hmset,hkeys,hget,hmget,hvals,hdel

# # def do_hast():
# #     #设置键对应  单个域
# #     # result = redis_conn.hset('info','height','178')
# #     # print(result)       #返回 0 或 1

# #     #设置键的对应 多个域
# #     # result = redis_conn.hmset('class',{'1804':36,'1805':35,'1806':32})
# #     # print(result)

# #     #设置 键对应 一个域，当这个域不存在是有效
# #     # result = redis_conn.hsetnx('class','1809','999')
# #     # print(result)   #返回一个 0 或者 1 的数字，0 表示不成功，1 表示成功

# #     # #获取 对应的hash键下的所有的 字段的名称
# #     # result = redis_conn.hkeys('class')
# #     # print(result)     #返回一个列表
    
# #     #获取 对应的 键 下面的所有的 field所对应的值
# #     # result = redis_conn.hvals('class')
# #     # print(result)   #返回一个列表

# #     #获取键 单个域的值
# #     # result = redis_conn.hget('class','1804')
# #     # print(result.decode('utf8'))

# #     #获取键下面 多个域的值
# #     # result = redis_conn.hmget('class','1804','1805')
# #     # print(result)       #返回一个列表

# #     #获取 键 下面的所有值
# #     # result = redis_conn.hgetall('class')
# #     # print(result)    #返回一个 字典 类型的数据，显示field和数据

# #     #删除键的一个或者多个field
# #     #删除单个field
# #     # result = redis_conn.hdel('class','1804')
# #     # print(result)
# #     #删除多个field
# #     # result = redis_conn.hdel('class','1804','1805')
# #     # print(result)   #返回删除的个数

# #     #判断 键 下面的field是否存在
# #     # result = redis_conn.hexists('class','1806')
# #     # print(result)       #返回一个boolean值

# #     #给hash中指定 域 的 值，增加指定的数字（一般是数字类型的）
# #     # result = redis_conn.hincrby('class','1804',100)
# #     # print(result)   #返回 增加 以后的值

# #     #给hash中指定的域的值增加给定的浮点数
# #     # result = redis_conn.hincrbyfloat('class','1804',100)
# #     # print(result)

# #     #获取 hash 里所有字段的数量
# #     # result = redis_conn.hlen('class')
# #     # print(result)

# #     #获取 hash 里面指定的 field 的长度
# #     # result = redis_conn.hstrlen('class','1809')
# #     # print(result)      #返回一个指定field下面的数据的长度，如果指定的内容不存在，返回0

# #队列的操作
# #list
# #操作的类型：lpush,rpush.linsert,lrange,lset,lrem 

# def do_list():
# #     从队列的 左边 入队 一个或者多个元素（先插入的在后面）
# #     result = redis_conn.lpush('lkey','1','2','3','4','5')
# #     print(result)  #返回  队列的内容总个数

# #     从队列的 右边 入队 一个或者多个元素（先插入的在前面）
# #     result = redis_conn.lpush('lkey','1','2','3','4','5')
# #     print(result)   #返回  队列的内容总个数

# #     从队列的 左边入队一个或者多个元素（先插入的在后面）！仅队列存在是有效
# #     result = redis_conn.lpushx('lkey','1','2','3','4','5')
# #     print(result)  #返回  队列的内容总个数 ，如果不存在会(empty list or set)

# #     从队列的 右边 入队 一个或者多个元素（先插入的在前面）！仅队列存在是有效
# #     result = redis_conn.lpushx('lkey','1','2','3','4','5')
# #     print(result)   #返回  队列的内容总个数，如果不存在会(empty list or set)

# #     从 队列中 指定返回的元素
# #     result = redis_conn.lrange('lkey',0,-1)
# #     print(result)   #返回一个列表

# #     从队列 中删除一个元素
# #     result = redis_conn.lrem('lkey','5','3') #lrem key count value
# #     print(result)   #返回 你删除的数量

# #     设置队列里面的一个元素的值(lset key index value)
# #     result = redis_conn.lset('lkey',3,888)
# #     print(result)     #返回一个boolean类型的值

# #     设置 要留下的 内容清单（用的是下标，有头有尾）
# #     result = redis_conn.ltrim('lkey',0,3)
# #     print(result)    #返回一个boolean类型的值

# #     从队列的 右边 弹出一个队列的元素
# #     result = redis_conn.rpop('lkey')
# #     print(result.decode('utf8'))   #返回 被弹出去的数据 ，弹出以后队列中将不在存在

# #     从队列的 左边 弹出一个队列的元素
# #     result = redis_conn.lpop('lkey')
# #     print(result.decode('utf8'))   #返回 被弹出去的数据 ，弹出以后队列中将不在存在

# #     删除 列表中的最后一个元素，将其追加到另一个列表中
# #     result = redis_conn.rpoplpush('k','lkey')
# #     print(result)  #返回 从列表中弹出的值

# #     删除并获得 列表中的第一个元素，或者是阻塞，直到有一个可用的
# #     result = redis_conn.blpop('k','2')  #blpop key [key key...] timeout
# #     result = redis_conn.blpop(['k','lkey'],'2')
# #     print(result)   #返回一个元组 (b'k', b'3')，前面是key，后面是显示的第一条数据, 如果指定了 单个键，没有删除内容后，会在设置的timeout时间过后显示None（timeout为0，表示永久的阻塞，直到有一个值可用）, 如果指定了 多个键，则会按照指定的顺序，第一个键的内容没有之后会自动的从下一个键开始执行，直到没有内容，返回None或永久阻塞，直到有一个值可用

# #     弹出列表最后的的值，将它推到另一个列表的开头，并返回它，或者阻塞，直到有一个可用的
# #     result = redis_conn.brpoplpush('k','lkey','0')
# #     print(result)   #返回弹出的内容

# #     通过 索引 获取一个元素
# #     result = redis_conn.lindex('k','2')
# #     print(result)   #返回根据索引找到的值

# #     在列表中的 另一个元素之前 插入 插入一个指定的元素 linsert key before/after pivot(指定数) value(要插入的数)
#     # result = redis_conn.linsert('k','before','i','999')
#     # print(result)   #返回 插入后列表内容的总数



# # 集合(无序集合)


# # 操作的类型：sadd,smembers,srem

def do_set():
    #添加一个或者多个元素到 集合中
    # result = redis_conn.sadd('skey','a','b','c','d','e','f')
    # print(result)    #返回 你插入的数目

    #获取集合里面元素的数量
    # result = redis_conn.scard('skey')
    # print(result)     #返回 集合里面的内容总数

    #获取队列 不存在的元素
    result = redis_conn.sdiff('skey','sk')
    print(result)   # 返回你指定第一个键，第二个键里面不存在的内容


#集合(有序集合)
#zset
#操作的类型：zadd,zrange,zrangebyscore,zscore,zrank

#事物的操作
def do_pipeline():
    pipe = redis_conn.pipeline()
    #开启事物
    pipe.multi()
    #存值
    pipe.set('big',1000)
    pipe.lpush('list',(1,2,3,4,5,6,7,8,9,0))
    pipe.hset('student','name','xxx')
    time.sleep(30)
    #提交
    pipe.execute()

#订阅发布
def sub_scribe():
    result = redis_conn.pubsub()
    result.subscribe('1804')  #订阅频道
    result.parse_response() #返回 [b'subscribe', b'1804', 1]   类型，订阅的对象，订阅的数量  *从发布/订阅命令解析响应
    redis_conn.publish('1804','1804的今天不用上课了')
    print(result.parse_response())
    print('等待消息')

    # return sub_scribe()
    # while True:
    #     print(result.parse_response())  #监听 频道 发布的消息
def publish():
    #发布频道消息
    redis_conn.publish('1804','1804的今天不用上课了')
    











if __name__ == '__main__':
    # do_string()
    # do_key()
    #do_pipeline()
    sub_scribe()
    publish()
    sub_scribe()
    # do_hast()
    # do_list()
    # do_set()