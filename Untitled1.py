#!/usr/bin/env python
# coding: utf-8

# In[ ]:


lst = eval(input('请输入列表lst:'))
    请输入列表lst:'1','1','2','3','3'
list1=set(lst)
print(list1)                     
    {'1', '2', '3'}
    
lst。。。接受列表输入。
输入列表，输出不带重复数字的列表

dict = {'fhz': '27', 'ljd': '28', 'hyx': '4'}  
print("dict['fhz']:",dict['fhz'])
    dict['fhz']: 27
dict1 = {'key1': '27', 'key2': '28', 'key3': '4'}  
dict2 = {'value1': 'fhz','value2': 'ljd','value': 'hyx'}
import random
print("dict1['key1']:",dict['key1'])
字符串的创建
str1 = 'hello'
str2 = "world"
str3 = """ni hao"""
字符串的查询
str1[0:6:2]
    'hlo'
str1[-3:-1]
  'll'
字符串的删除
#str1.replace
str4 = ' ',join([strl,strl2])
str4
str4.split(' ')   #split可把字符串拆成字符
print('')
str5 = 'hello\n'
print(str5.strip())     #strip可删除分隔符
f = open('test.txt', 'w'）   #建立一个链接
f.write("hello world\n")      #已在内存中运行
f.write("I'm here")
f.close()    #执行
f = open('test.txt','r'）
f.read(1)
lines = f.readlines()        #逐行读入
lines

