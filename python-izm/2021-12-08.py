# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 14:45:33 2021

@author: USER
"""

print('1234\n3456')

import os
 
 
PROJECT_DIR = 'C:¥python-izm'
SETTINGS_FILE = 'settings.ini'
 
print(os.path.join(PROJECT_DIR, SETTINGS_FILE))
print(os.path.join(PROJECT_DIR, 'settings_dir', SETTINGS_FILE))

for value in 'Hello','goodevening':
    print(value)
    
No1=['A','B','C']
No2=('a','b','c')

for x in range(0,3):
    print(x,No1[x],No2[x])

print('\n')

counter=0
while counter<10:
    counter += 1
    print(counter)

counter=0

while True:
    counter += 1
    print(counter)
    if counter == 10:
        break

for x in range(100):
    if x % 10 !=0 :
        continue
    print(x)
list1=[] 
list2=[]
for x in range(10):
   list1.append(x)
   list2.append(str(x+10))
   print('list1は%d、list2は%s'%(list1[x],list2[x]))

def exception_test(value_1,value_2):
    
    print('---------------')
    result=0
    
    try:
        result=value_1+value_2
    except:
        print('計算不可')
        raise
    finally:
        print('計算完了')
        print('------------------')
    
    return result

print(exception_test(100,200))
print(exception_test(100,'200'))

try:
    print(exception_test(100,200))
    print(exception_test(100,'200'))
except:
    print('エラー発生')
finally:
    print('計算終了')
   
    
