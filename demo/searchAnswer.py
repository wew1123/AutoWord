import pandas as pd
import numpy as np
import random
import string
#先读入xlwx中的所有信息
#title,ans分别为列A和列C
#使用title中寻找答案
data = pd.read_excel('DatabaseOut.xlsx',sheet_name="question",usecols=[0,2])
# target = 'mess'

def getAnswerDict():
    answer={}
    for i in range(0,data.shape[0]):
        answer[data.title[i]]=data.ans[i]
    return answer

def searchAnswer(target,answerDict):

    if target in answerDict.keys():
        return answerDict[target]
    else:
        return random.choice('ABCD')

