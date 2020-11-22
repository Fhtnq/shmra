

```python
#打开并读取文件  
file = open(r'C:\Users\21033\Desktop\Walden.txt','r')
lines = file.readlines()
```


```python
#要把每行拆成单词、
words = []

for line in lines:
    #print(line.split(" "))
    tmp_list = line.split(" ")
    for word in tmp_list:
    #words.append(tmp_list)
        words.append(word.replace(',','').replace(',','').replace('"','').replace(':','').lower)
words
```


```python
# 对words中每一个元素计算它出现的个数
# 把统计结果保存到字典中，字典的key是单词，value是单词出现的次数
words.count = {}
word_set = set(words)
#for word in words:
for word in word_set:
    count_num = words.count(word)  #重复取单词太耗时间所以加入set
    word_count[word] = count_num
    
word_count
```


```python
# 对 word_count字典进行排序，按照出现的次数（value）进行降序排序 
sorted(word_count.items(),key=lambdn item: item[1],reverse=True)

#word_count.items()
```


```python
# 整合代码输出py文件（运行时先把这行删除）
%%writefile cipin.py
#打开并读取文件  
file = open(r'C:\Users\21033\Desktop\Walden.txt','r')
lines = file.readlines()
#要把每行拆成单词、
words = []

for line in lines:
    #print(line.split(" "))
    tmp_list = line.split(" ")
    for word in tmp_list:
    #words.append(tmp_list)
        words.append(word.replace(',','').replace(',','').replace('"','').replace(':','').lower)
words
# 对words中每一个元素计算它出现的个数
# 把统计结果保存到字典中，字典的key是单词，value是单词出现的次数
words.count = {}
word_set = set(words)
#for word in words:
for word in word_set:
    count_num = words.count(word)  #重复取单词太耗时间所以加入set
    word_count[word] = count_num
    
word_count
# 对 word_count字典进行排序，按照出现的次数（value）进行降序排序 
sorted(word_count.items(),key=lambdn item: item[1],reverse=True)

#word_count.items()
```

Writing ciping.py（运行成功时显示）
```python
file.read()
```
