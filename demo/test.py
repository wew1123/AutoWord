import json
import time

import urllib3
import xlsxwriter

from getTicket import *

# set get rounds
ticket=""
get_rounds = 20
# define sleeptime
time_pause = 0
time_pause_end = 0
# to init
startTime = int(time.time() * 100)
url_op_get = 'skl.hdu.edu.cn/api/paper/new?type=0&week=13&startTime=' + str(startTime)
url_post = 'skl.hdu.edu.cn/api/paper/save'
# these are headers
header_option = {
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

header_get = {
    "Host": "skl.hdu.edu.cn",
    "Accept": "application/json, text/plain, */*",
    # "X-Auth-Token": "3791a7dc-d2b2-417b-8ef0-6ab2ad84f5f2",
    "X-Auth-Token": "ecd164b3-8984-4d0f-83e3-0a9ec39c9c3d",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6303005d)",
    "Origin": "https://skl.hduhelp.com",
    "Skl-Ticket": ticket,
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://skl.hduhelp.com/?type=1",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "Connection": "close",
}

header_post = {
    "Host": "skl.hdu.edu.cn",
    "Accept": " application/json, text/plain, */*",
    "X-Auth-Token": "3791a7dc-d2b2-417b-8ef0-6ab2ad84f5f2",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6303005d)",
    "Origin": "https://skl.hduhelp.com",
    "Content-Type": "application/json;charset=UTF-8",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://skl.hduhelp.com/?type=1",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,e,n-US;q=0.8,en;q=0.7",
    "Connection": "close",
    "Content-Length": "0",
}

header_RightAnswer = {
    "Host": "skl.hdu.edu.cn",
    "Accept": "application/json, text/plain, */*",
    "X-Auth-Token": "3791a7dc-d2b2-417b-8ef0-6ab2ad84f5f2",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6303005d)",
    "Origin": "https://skl.hduhelp.com",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://skl.hduhelp.com/?type=1",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "Connection": "close",
}


def solveit(round_):
    method = 'OPTION'
    http = urllib3.PoolManager()
    r0 = http.request(method=method,
                      url=url_op_get,
                      headers=header_option,
                      )
    method = 'GET'
    header_get['Skl-Ticket']=getTicket()
    r1 = http.request(method=method,
                      url=url_op_get,
                      headers=header_get,
                      )
    time.sleep(time_pause)
    ans = json.loads(r1.data.decode('utf-8'))
    # print(ans['paperId'])
    # print(ans['list'])
    # this confirm that the ans works
    paperId = ans['paperId']
    list = []
    input = ''
    ret = {}
    for i in range(0, 100):
        list.append({'input': 'A', 'paperDetailId': ans['list'][i]['paperDetailId']})
        # print(list[i])

    ret = {
        'paperId': paperId,
        'list': list,
    }
    # print(ret)
    params = bytes(json.dumps(ret), 'utf-8')
    # print(params)
    method = 'POST'
    header_post['Content-Length'] = len(params)
    solve_post = http.request(
        method=method,
        body=params,
        headers=header_post,
        url=url_post,
    )
    print('solve post!')
    # now,get the right answer
    method = 'GET'
    url_RightAnswer = "skl.hdu.edu.cn/api/paper/detail?paperId=" + paperId
    r3 = http.request(method=method,
                      url=url_RightAnswer,
                      headers=header_RightAnswer,
                      )
    Myneed = json.loads(r3.data.decode('utf-8'))
    print(Myneed)
    save = []
    for i in range(0, 100):
        q = 'answer' + Myneed['list'][i]['answer']
        # print(Myneed['list'][i]['title']+":"+Myneed['list'][i][q])
        # save[Myneed['list'][i]['title']]=Myneed['list'][i][q]
        save.append({
            'paperDetailId': Myneed['list'][i]['paperDetailId'],
            'title': Myneed['list'][i]['title'],
            'answer': Myneed['list'][i][q],
            'ans': Myneed['list'][i]['answer'],
            'answerA': Myneed['list'][i]['answerA'],
            'answerB': Myneed['list'][i]['answerB'],
            'answerC': Myneed['list'][i]['answerC'],
            'answerD': Myneed['list'][i]['answerD'],
        })
    # i def a functiom,so i don't need pandas antmore
    # f = open('Database.xlsx', 'rb')
    # data_ = pandas.read_excel(f)
    # columns = data_.shape[0]

    # when writing,xlsxwriter will replace the orign sheet,so drop it

    for i in range(0, 100):
        # print(save[i]['paperDetailId'] + ':{' + save[i]['title'] + ':' + save[i]['answer'] + '}' + save[i]['ans'])
        worksheet.write('A' + str(i + counts*100 + 2), save[i]['paperDetailId'])
        worksheet.write('B' + str(i + counts*100 + 2), save[i]['title'])
        worksheet.write('C' + str(i + counts*100 + 2), save[i]['answer'])
        worksheet.write('D' + str(i + counts*100 + 2), save[i]['ans'])
        for j in ['E', 'F', 'G', 'H']:
            worksheet.write(j + str(i + counts*100 + 2), save[i]['answer' + chr(ord(j) - 4)])

    # f.close
    # print('columns:' + str(columns))
    print('done' + str(round_))
    time.sleep(time_pause_end)


def select_base(basement_):
    global workbook, worksheet
    workbook_ = xlsxwriter.Workbook('DatabaseOut' + str(basement_ + 8) + '.xlsx')  # build file
    worksheet = workbook_.add_worksheet('question')  # build sheet ,and name it as question
    worksheet.write('A1', 'paperId')
    worksheet.write('B1', 'title')
    worksheet.write('C1', 'answer')
    worksheet.write('D1', 'ans')
    worksheet.write('E1', 'answerA')
    worksheet.write('F1', 'answerB')
    worksheet.write('G1', 'answerC')
    worksheet.write('H1', 'answerD')
    return workbook_


column = 0
counts = 0
f = select_base(int(column / 10))
while column < get_rounds:
    # if column % 10 == 0 and column != 0:
    #     f.close()
    #     f = select_base(int(column / 10))
    try:
        solveit(counts)
        counts = counts + 1
        column = column+1
    except Exception as r:
        print('未知错误 %s' % r)
        time.sleep(time_pause_end)
    # except:
    #     print('round:'+str(round)+'failed!')
    #     pass

f.close()
