
import requests
import json
import sys
import time
import numpy as np

# 用global记录，输入微信小程序的信息
appid="wxc070fd9e95fc5fd8"
secretid="5570f1b0b96e2e54ecd10016d2205bd6"

# 小程序云服务器id环境
env=""


# 一些基本的访问地址
urlBase = [
    # 获取token的地址
    'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s',
    # 导入数据库
    'https://api.weixin.qq.com/tcb/databasemigrateimport?access_token=',
    # 下载文件
    'https://api.weixin.qq.com/tcb/batchdownloadfile?access_token=',
    # 上传文件
    'https://api.weixin.qq.com/tcb/uploadfile?access_token=',
    # 添加数据到库
    'https://api.weixin.qq.com/tcb/databaseadd?access_token',
    # 修改数据到库
    'https://api.weixin.qq.com/tcb/databaseupdate?access_token=',
]


def findMyAccessToWxCloud():
    # appid:str,secretid:str 原本想传参的，但是还是global吧
    # 获取keyToken，时限为2h

    res=requests.get(urlBase[0]%(appid,secretid))
    res.encoding='utf-8'
    pyObj=json.loads(res.text)
    if pyObj.get('errcode'):
        print('connection fail, please review your info') 
        # sys.error('errcode: '+pyObj.get('errmsg'))
    else:
        print('successfully get key')
        accesskey=pyObj.get('access_token')
        return accesskey
    pass


def packMyData(baseName:str,pos:list,pic:np.array,safty=True):
    # 把数据打包好成dict，附加补充详细、必要信息

    # 是否观测到火情
    if safty:
        status="status: 1,"
    else:
        status="status: 0,"
    

    # 打包时间信息和地理信息
    gratitude="gratitude: [%s,%s],"%(str(pos[0]),str(pos[1]))
    myTime="time: %s,"%(time.asctime( time.localtime(time.time()) ))

    dataStr=status+gratitude+myTime

    myobj={
    "env":env,
    # query代表数据库操作语句，将记录加入数据库必须要化为语句指令
    "query": "db.collection(%s).add({data:[{%s}]})" %(baseName,dataStr)
    },

    return myobj


def uploadToDataCollection(accesskey:str, resData:dict):
    # 这里还是要传key进来的，然后数据包也是需要的，可以不用压缩成json,注意要有目标的位置信息

    # 将数据打包好，传进来的参数运用上面的函数
    Data=json.dumps(resData)

    # 尝试上传
    res=requests.post(urlBase[4]+accesskey,data=Data)
    res.encoding='utf-8'
    pyObj=json.loads(res.text)
    if pyObj.get('errcode'):
        print('connection fail, please review your info') 
        # sys.error('errcode: '+pyObj.get('errmsg'))
    else:
        print('successfully update')
        return
    pass


def upPicToBase(accesskey:str, pic:np.array, baseName='picBase'):
    # 将图片保存为数据，上传到数据库

    # 还没有写好！

    # 将opencv读取的图像又np数组作为参数导入，再变更为list，打包至json
    dic={
        ""
    }
    dic['picData']=pic.tolist()
    pack=json.dumps(dic)

    res=requests.post(urlBase[4]+accesskey,data=pack)
    res.encoding='utf-8'
    pyObj=json.loads(res.text)
    if pyObj.get('errcode'):
        print('connection fail, please review your info') 
        # sys.error('errcode: '+pyObj.get('errmsg'))
    else:
        print('successfully update')
        return
    pass


def getUpdateFileUrl(accessKey:str,myPath:str,upPath:str):
    # 要是想让微信上看到图片就要用这个

    dic={
        "env": env,
        "path": upPath
    }
    pack=json.dumps(dic)

    # 获取临时url
    res=requests.post(urlBase[3]+accessKey,data=pack)
    res.encoding='utf-8'
    pyObj=json.loads(res.text)
    if pyObj.get('errcode'):
        print(pyObj.get('errcode')+' connection fail,cannot get url') 
        # sys.error('errcode: '+pyObj.get('errmsg'))
        pass
    else:
        print('successfully get url')
        url=pyObj.get('url')
    
    return url


def updateFile(url:str,myPath:str):

    # 打开相应的文件地址
    file = open(myPath)
    # 使用临时url，微信云服务器只能这样
    requests.post(url,data=file.read(),headers={'Content-Type':'pic/jpeg'})
    pass