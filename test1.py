#9:02 2018/5/10
#python练习

import this
import os
#c:/test 若使用c:\test会被认为是转移符号
#https://blog.csdn.net/qq_33363973/article/details/77862007
#创建文件
with open('c:/test.txt','at',encoding='utf-8') as f:
	f.write('dongyusheng\nline2')
#读取文件
with open('c:/test.txt','rt') as f2:
	data=f2.read()
print(data)
#按行读取
with open('c:/微信.txt','rt') as f3:
    for line in f3:
	    print(line)
#写入print的内容
def range1(n):
	return list(range(n))
	
with open('c:/微信.txt','at+') as f3:
    print(range1(100),file=f3)

with open('c:/test.doc','at',encoding='utf-8') as f:
	f.write('dongyusheng\nline2')

#文件名和文件路径的操作
import os




#串行端口
import serial

