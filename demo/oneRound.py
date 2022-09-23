import json
import time
import urllib3
from header import *
from searchAnswer import *

http = urllib3.PoolManager()
#生成http
optionReturn= http.request(method='OPTIONS',url=optionUrl,headers=optionHeader)
# print("optionReturn data:+"+str(optionReturn.data.decode('utf-8'))+'\n')
#option请求
getReturn= http.request(method='GET',url=getUrl,headers=getHeader)
# print("getReturn data:+"+str(getReturn.data.decode('utf-8'))+'\n')
#get请求
input=''
ans = json.loads(getReturn.data.decode('utf-8'))
#ans是将返回的json字符串变成的一个字典
#ans字典里有一个属性为list，list是一个列表，这个列表里面有100个字典，分别对应100个papaerDetailld的题目信息
#list中的每个字典的格式

paperId=ans['paperId']
List=ans['list']
#将请求的返回数据存在变量中
#List[i][paperDetailId],List[i][title],List[i][answerA],List[i][answerB],List[i][answerC],List[i][answerD]

#下面要产出post的数据过去
postList=[]
i=0
answerDict = getAnswerDict()
#postList是要post过去的数据，这里给每个单词找到对应的答案存到input中去
for _ in List:
    time.sleep(0)
    input = searchAnswer(_['title'],answerDict)
    postList.append({'input': input, 'paperDetailId': _['paperDetailId']})

postMsg={
    "paperId" : paperId,
    "list": postList,
}

jsonDumpsPostMsg= bytes(json.dumps(postMsg), 'utf-8')
#jsonDumps
#{
#   paperId
#   list[
#       {
#           paperDetailId: xxxxxxxxxxx
#           input: 'A'
#       }
#
#       {
#           paperDetailId: xxxxxxxxxxx
#           input: 'B'
#       }
#
#       ]

updatePostContentLength(jsonDumpsPostMsg)
postReturn = http.request(method='POST',
                          url=postUrl,
                          headers=postHeader,
                          body=jsonDumpsPostMsg)


