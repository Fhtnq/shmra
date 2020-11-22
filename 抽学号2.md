

```python
keys = [1,2,3,4]
values = ['张三','李四','王五','赵六']
# 创建字典
students = {}
i=0
for key in keys:
    students[key]=values[i]
printed(students)
```


```python
#创建一个字典students, key是学号，value是姓名
#学生信息在students.csv文件里，从文件中读取并保存到字典

#打开students.csv文件
file = open(r'C:\Users\Administrator\Desktop\students.csv','r')
```


```python
#读取文件内容
lines = file.readlines()
```


```python
#抽取每行的学号和姓名，保存到字典
students = {}0
for line in lines:
    #print(type(line))
    #print(lines.split(','))
    tmp_list = line.split(',')
    #xuehao = line.split[0]
    #xingming = line.split[1]
    xuehao = tmp_list[0]
    xingming = tmp_list[1]
    students[xuehao] = xingming
    
print(students)
```


```python
# 从学号中随机抽取N个学号
import random
#random.smple([1,2,3,4],2)


num = int(input("输入你要抽取的人数："))
#如何把字典中的key（学号）取成列表
#students.keys()
#random.sample(students.keys(),1)
xuehao_list = random.sample(students.keys(),num)

xuehao_list
```


```python
# 根据随机抽取的学号，打印输出对应的姓名
for xuehao in xuehao_list:
    print(students[xuehao])
```


```python
# 整合代码（运行时记得删除）
%%writefile chouxuehao.py
#创建一个字典students, key是学号，value是姓名
#学生信息在students.csv文件里，从文件中读取并保存到字典

#打开students.csv文件
file = open(r'C:\Users\Administrator\Desktop\students.csv','r')
#读取文件内容
lines = file.readlines()
#抽取每行的学号和姓名，保存到字典
students = {}
for line in lines:
    #print(type(line))
    #print(lines.split(','))
    tmp_list = line.split(',')
    #xuehao = line.split[0]
    #xingming = line.split[1]
    xuehao = tmp_list[0]
    xingming = tmp_list[1]
    students[xuehao] = xingming
    
print(students)
# 从学号中随机抽取N个学号
import random
#random.smple([1,2,3,4],2)


num = int(input("输入你要抽取的人数："))
#如何把字典中的key（学号）取成列表
#students.keys()
#random.sample(students.keys(),1)
xuehao_list = random.sample(students.keys(),num)

xuehao_list
# 根据随机抽取的学号，打印输出对应的姓名
for xuehao in xuehao_list:
    print(students[xuehao])
```
Writing chouxuehao.py(运行成功时显示)
