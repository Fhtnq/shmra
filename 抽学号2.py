#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().run_cell_magic('writefile', 'chouxuehao.py', '#创建一个字典students, key是学号，value是姓名\n#学生信息在students.csv文件里，从文件中读取并保存到字典\n\n#打开students.csv文件\nfile = open(r\'C:\\Users\\Administrator\\Desktop\\students.csv\',\'r\')\n#读取文件内容\nlines = file.readlines()\n#抽取每行的学号和姓名，保存到字典\nstudents = {}\nfor line in lines:\n    #print(type(line))\n    #print(lines.split(\',\'))\n    tmp_list = line.split(\',\')\n    #xuehao = line.split[0]\n    #xingming = line.split[1]\n    xuehao = tmp_list[0]\n    xingming = tmp_list[1]\n    students[xuehao] = xingming\n    \nprint(students)\n# 从学号中随机抽取N个学号\nimport random\n#random.smple([1,2,3,4],2)\n\n\nnum = int(input("输入你要抽取的人数："))\n#如何把字典中的key（学号）取成列表\n#students.keys()\n#random.sample(students.keys(),1)\nxuehao_list = random.sample(students.keys(),num)\n\nxuehao_list\n# 根据随机抽取的学号，打印输出对应的姓名\nfor xuehao in xuehao_list:\n    print(students[xuehao])')

