from random import *
def getTicket():
    t1 = "".join([choice("0123456789ABCDEF") for i in range(8)])
    t2 = "".join([choice("0123456789ABCDEF") for i in range(4)])
    t3 = "".join([choice("0123456789ABCDEF") for i in range(4)])
    t4 = "".join([choice("0123456789ABCDEF") for i in range(4)])
    t5 = "".join([choice("0123456789ABCDEF") for i in range(12)])
    # ticket = t1+'-'+t2+'-'+t3+'-'+t4+'-'+t5

    sep=(t1,t2,t3,t4,t5)
    str='-'
    ticket=str.join(sep)
    # print(ticket)
    return ticket

getTicket()