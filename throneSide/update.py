from linkkit import linkkit
import time
import json


# 连接阿里云
def on_connect(session_flag, rc, userdata):
    print("on_connect:%d,rc:%d,userdata:" % (session_flag, rc))
    pass

# 取消连接阿里云
def on_disconnect(rc, userdata):
    print("on_disconnect:rc:%d,userdata:" % rc)

def on_subscribe_topic(mid, granted_qos, userdata):#订阅topic
    print("on_subscribe_topic mid:%d, granted_qos:%s" %
          (mid, str(','.join('%s' % it for it in granted_qos))))
    pass

# 接收云端的数据
def on_topic_message(topic, payload, qos, userdata):
    #print("on_topic_message:" + topic + " payload:" + str(payload) + " qos:" + str(qos))
    # 不知道为什么下行的数据是“123”，设备端的接收到的数据却是b:"123"
    # 所以我在这里用了一个切片去处理数据
    print("阿里云上传回的数值是:",str(payload)[2:-1])
    pass

# 终止订阅云端数据
def on_unsubscribe_topic(mid, userdata):
    print("on_unsubscribe_topic mid:%d" % mid)
    pass

# 发布消息的结果，判断是否成功调用发布函数
def on_publish_topic(mid, userdata):
    print("on_publish_topic mid:%d" % mid)

# 设置连接参数，方法为“一机一密”型
lk = linkkit.LinkKit(
    host_name="cn-shanghai",# 填自己的host_name，华东地区填cn-shanghai
    product_key="***",# 填自己的product_key
    device_name="***",# 填自己的device_name
    device_secret="***")# 填自己的device_secret


# 注册接收到云端数据的方法
lk.on_connect = on_connect
# 注册取消接收到云端数据的方法
lk.on_disconnect = on_disconnect
# 注册云端订阅的方法
lk.on_subscribe_topic = on_subscribe_topic
# 注册当接受到云端发送的数据的时候的方法
lk.on_topic_message = on_topic_message
# 注册向云端发布数据的时候顺便所调用的方法
lk.on_publish_topic = on_publish_topic
# 注册取消云端订阅的方法
lk.on_unsubscribe_topic = on_unsubscribe_topic

# 连接阿里云的函数（异步调用）
lk.connect_async()
# 因为他是他是异步调用需要时间所以如果没有这个延时函数的话，他就会出现not in connected state的错误
time.sleep(2)
# 订阅这个topic，不需要写prodect_key和device_name
rc, mid = lk.subscribe_topic(lk.to_full_topic("user/get"))
a=input("你想要将什么数值传到阿里云上去？")
# 调用数据上传的函数，将string类的a上传到阿里云上去
rc, mid = lk.publish_topic(lk.to_full_topic("user/update"), str(a))