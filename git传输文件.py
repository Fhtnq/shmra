
# coding: utf-8

# ### 新建代码仓库（云端github，gitee，etc）
# 
#  * 创建一个仓库
#  * 仓库的url
# 
# ### 本地代码上传到新建的仓库
# 
#  * 本地的代码仓库（本地文件夹）
#  * 启动Git Bash命令
#  * Linux操作命令
#  
# pwd # 显示当前所在的路径
# cd  # change directory，进入指定的路径下
# 
#  * 进入了本地的代码仓库（文件夹）
#  
#  ls -a # ls：list，-a：all，显示当前路径下的所有的文件及文件夹（包括隐藏文件）
#  
#  * 初始化当前文件夹为一个Git代码仓库
#  
# git init
# 
# 
#  * 添加到本地仓库，登记下想把哪些文件提交到本地仓库去。
# 
# git add 文件名
# git add .
# 
#  * 提交到本地仓库,成功会出现仓库记录的变动信息
#  
# git commit -m "message"
# 
#  * 计算机初次使用Git，会提示配置用户名及登陆邮箱
#  
# git config --global user.email "you@example.com"
# git config --global user.name "Your Name"
# 
# 
# ### 目前完成了本地仓库的代码提交
# ### 下一步进行远程代码仓库提交
# 
#  * 提交到哪？远程代码仓库的地址要添加到本地仓库的配置中.
#  
# git remote add origin https://  ——————        #origin 是代码仓库命
# 名，可以为其他名称。https：//XXX.com/xxx.git是远程代码仓库的地址。
# 
# 完成了远程代码仓库的配置
# 
#  * 远程代码仓库的提交
#  
# git push -u origin master#-u origin 指定仓库;master为远程仓库的代码分支
# 
# ### 完成了初次从本地到远程的代码提交
# 

# ### 本地修改了文件（代码、文档），代码仓库的更新
# 
#  * 修改文件后
#  
# git add修改的文件名
# 
# git commit -m"msg"提交你修改的文件
# 
# 完成了本地的代码仓库更新 

# ### 本地新建文件夹（本地仓库2），从远程仓库更新代码到本地
# 
# git pull https://.git
# 
# ### 本地仓库2中添加一个文件，提交到本地仓库2
# 
# ### 更新本地仓库2至远程仓库
