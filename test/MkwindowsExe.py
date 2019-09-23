# -*- coding :utf-8 -*-
#Author :刘悦
import os
import datetime
local_dir=r'E:\test'
local_path=r'E:\test\test.txt'
if not os.path.exists(local_dir):
	os.mkdir(local_dir)
f=open(local_path,'a+')
date_str=datetime.datetime.now()
print(date_str)
content="成功写入%s\n"%(str(date_str))
f.write(content)
f.close()
print('执行成功')
while True:
	str=input("请输入你想输入的东西,输入 exit 退出: \t")
	print('你输入的是: \t %s'%str)
	if str=='exit':
		print('退出')
		break;














