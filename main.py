import urllib3

http = urllib3.PoolManager()

r1=http.request(
    method='GET',
    url='baidu.com',
)

print(r1.data)
