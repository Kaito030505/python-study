# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 10:48:59 2021

@author: USER
"""

def test_func():
    print('call test_func')
 
test_func()

def test_func(num_1,num_2,oprn):
    if oprn==1:
        print('足し算')
        print(num_1+num_2)
    elif oprn==2:
        print('引き算')
        print(num_1-num_2)
    elif oprn==3:
        print('掛け算')
        print(num_1*num_2)
    elif oprn==4:
        print('割り算')
        print(num_1/num_2)
    else:
        print('不明')

test_func(100,10,3)
test_func(100,10,4)

class Testclass:
    def test_method():
        print('call test_method')
        
print(test_func)
print(Testclass.test_method)

print(type(Testclass.test_method))
print(type(test_func))
    
t=Testclass()
print(t.test_method)    

def test_func2(code,name,*args):
    print(code,name)
    print(args)
    
test_func2(100,'python-izm','JP','US')

def test_func3(**kwargs):
    print(kwargs)
 
test_func3(code=100, name='python-izm')

def test_func4(code, name, kana, *args, **kwargs):
    print(code, name, kana)
    print(args)
    print(kwargs)
 
test_func4(
    100, 'python-izm', 'パイソンイズム',
    'JP', 'US', 
    email='xxxx', city='Tokyo'
)