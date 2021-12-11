# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 13:23:48 2021

@author: USER
"""

print('Hello world')
No1='Hello'
No2=' '
No3='world'
print(No1+No2+No3)
No4=12345
print(str(No4))
No5='Hello-world'
print(No5.split('-'))
print(No1.rjust(10,'0'))
print(No1.ljust(10,' '))
print(No1.zfill(5))
print(No5.startswith('H'))
print(No1.startswith('h'))
print(No1.upper())
print(No1.lower())

import datetime
#import time
today=datetime.date.today()
todaydetail=datetime.datetime.today()
print('------------------------')
print(today)
print(todaydetail)
print('------------------------')
print(today.year)
print(today.month)
print(today.day)
print(todaydetail.year)
print(todaydetail.month)
print(todaydetail.day)
print(todaydetail.hour)
print(todaydetail.minute)
print(todaydetail.second)
print(todaydetail.microsecond)

#time.sleep(2)
print('------------------------')
print(todaydetail.second)

print('------------------------')
print(today.isoformat())
print(todaydetail.strftime('%Y/%m/%d %H:%M:%S'))
print('%sd'%(todaydetail.day))

def get_today():
    value=[today.year,today.month,today.day]
    return value

test=get_today()
print(test)
print(test[1])
print(test[2])
test.append(3)
print(test)




