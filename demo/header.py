from getTicket import *
import time

startTime=str(int(time.time()*1000))
# token = "ecd164b3-8984-4d0f-83e3-0a9ec39c9c3d"
# week=13

week=input("当前是第几周：")
token = input("输入token:")
optionUrl="skl.hdu.edu.cn/api/paper/new?type=0&week=13&startTime="+startTime
getUrl="skl.hdu.edu.cn/api/paper/new?type=0&week="+str(week)+"&startTime="+startTime
postUrl="skl.hdu.edu.cn/api/paper/save"
postMsg=''

optionHeader={
    "Host": "skl.hdu.edu.cn",
    "Access-Control-Request-Method": "GET",
    "Origin": "https://skl.hduhelp.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6303005d)",
    "Access-Control-Request-Headers": "x-auth-token",
    "Accept": "*/*",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://skl.hduhelp.com/?type=1",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "Connection": "close",
}


getHeader = {
    "Host": "skl.hdu.edu.cn",
    "Accept": "application/json, text/plain, */*",
    "X-Auth-Token": token,
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6303005d)",
    "Origin": "https://skl.hduhelp.com",
    "Skl-Ticket":getTicket(),
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://skl.hduhelp.com/?type=1",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "Connection": "close",
}

postHeader={
    "Host": "skl.hdu.edu.cn",
    "Content-Length": str(len(postMsg)),
    "Accept": " application/json, text/plain, */*",
    "X-Auth-Token": token,
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6303005d)",
    "Origin": "https://skl.hduhelp.com",
    "Content-Type": "application/json;charset=UTF-8",
    "Skl-Ticket": getTicket(),
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://skl.hduhelp.com/?type=1",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,e,n-US;q=0.8,en;q=0.7",
    "Connection": "close",
}

def updateGetSklHeader():
    getHeader['Skl-Ticket']= getTicket()

def updatePostSklHeader():
    postHeader['Skl-Ticket']= getTicket()

def updatePostContentLength(msgPost):
    postHeader["Content-Length"]=len(msgPost)