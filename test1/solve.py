import urllib3
import time
import json

startTime = int(time.time()*1000)

url_op_get = 'skl.hdu.edu.cn/api/paper/new?type=0&week=13&startTime=' + str(startTime)
url_post = 'skl.hdu.edu.cn/api/paper/save'

http = urllib3.PoolManager()

method="OPTIONS"
header_option={
"Host": "skl.hdu.edu.cn",
"Access-Control-Request-Method": "GET",
"Origin": "https://skl.hduhelp.com",
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63040026)",
"Access-Control-Request-Headers": "skl-ticket,x-auth-token",
"Accept": "*/*",
"Sec-Fetch-Site": "cross-site",
"Sec-Fetch-Mode": "cors",
"Sec-Fetch-Dest": "empty",
"Referer": "https://skl.hduhelp.com/",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
"Connection": "close",
}

header_get={
"Host": "skl.hdu.edu.cn",
"Accept": "application/json, text/plain, */*",
"X-Auth-Token": "ecd164b3-8984-4d0f-83e3-0a9ec39c9c3d",
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63040026)",
"Origin": "https://skl.hduhelp.com",
"Skl-Ticket": "hello hdu-helper!",
"Sec-Fetch-Site": "cross-site",
"Sec-Fetch-Mode": "cors",
"Sec-Fetch-Dest": "empty",
"Referer": "https://skl.hduhelp.com/",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
"Connection": "close",

}

r0 = http.request(method=method,
                  url=url_op_get,
                  headers=header_option,
                  )
r_get = http.request(method='GET',
                  url=url_op_get,
                  headers=header_get,
                  )
print(r0.__dict__)
print('\n')
print(dir(r_get))
# print(r0['data'])
print('\n')
print(r_get._body)
print('\n')
print(dir(r_get.read))
print('\n')
print(r_get.msg)
print('\n')
print(r_get.data)