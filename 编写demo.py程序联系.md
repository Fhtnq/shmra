新建一个demo.py文件，在PyCham中创建环境
lines_maxlenth = 0
line_numbers = 1
hh_in = open(“demo.py”,“r”).readlines()
hh_out = open(“demo_new.py”, “w”) # 运行生成一个demo_new.py文件
for i in hh_in:
if(lines_maxlenth < len(i)): #寻找最长语句行长度
lines_maxlenth = len(i)
for i in hh_in:
i = i.ljust(lines_maxlenth+1).replace(’\n’,’ ’) + str(line_numbers) + “\n”
line_numbers += 1 # 每行行号增加
hh_out.write(i)

![](https://img-blog.csdnimg.cn/2020111908114286.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl81MTc3NTc5MQ==,size_16,color_FFFFFF,t_70#pic_center)
![在这里插入图片描述](https://img-blog.csdnimg.cn/2020111908132579.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl81MTc3NTc5MQ==,size_16,color_FFFFFF,t_70#pic_center)


