#星期转换程序 函数形式

import turtle

# -*- coding: utf-8 -*-
def weekchange(week):
    weekstr='一二三四五六七'
    weekstrnew='星期'+weekstr[week-1]
    return weekstrnew

weeknum=eval(input('请输入1-7\n'))
print(weekchange(weeknum))


#十二星座unicode字符;chr(),ord()
'''
for i in range(12):
    print(chr(19800+i),end='')

for i in range(100)
:
    print(chr(100+i),end='')
    
'''
#str.format()的基础应用，6种format控制格式
print('\n')
print('{0:=^30}{1:<10}'.format('dongyusheng','666'))


#时间的基本使用和定时功能
import time
print(time.ctime())
t=time.localtime() #计算机识别的格式;gmtime()是标准时区CUT时区，我们是+8区，laocaltime()是本地时区的格式
print(time.strftime('%Y-%m-%d %H:%M:%S',t)) #获取的小时与本地时区差8H.不是本地时区？


#程序进度条的设计:已经实现输出长度固定50的情况
start_time=time.perf_counter()
scale=100
print('程序开始'.center(50//2,'*'))
for i in range(scale+1):
    a='▉'*int(i*(50/scale)) #进度条文本框固定为50
    b='▕'*(50-int(i*(50/scale)))
    c=(i/scale)*100
    end_time=time.perf_counter()
    time_detal=end_time-start_time
    print("\r[{:^3.0f}%{}{}]{:<2.2f}s".format(c,a,b,time_detal),end='')#idle中显示效果不正确，要去python命令行下看执行效果
    time.sleep(0.01)
end_time=time.perf_counter()
print('程序结束'.center(50//2,'*'))
#进度条单行进度刷新
#▉▉▉▊▋▕▕▕▕▔▔▔▕▕▕完美的程序


#课程四 程序的控制，异常处理
try :
    ajj=eval(input('输入整数'))
except :
    print('不是整数')

#BMI指数
height,weight=eval(input('请输入身高（米）和体重(公斤)[逗号隔开]:'))
bmi=weight/pow(height,2)
print('BMI 数值为：{:.2f}'.format(bmi))
who,nat='',''
if bmi<18.5:
    who,nat='偏瘦','偏瘦'
elif 18.5<=bmi<24:
    who,nat='正常','正常'
elif 24<=bmi<28:
    who,nat='正常','偏胖'
elif 28<=bmi<30:
    who,nat='偏胖','肥胖'
else :
    who,nat='肥胖','肥胖'
print("BMI指标为：国际'{0}',国内'{1}'".format(who,nat))

#随机函数
import random
random.seed(10) #随机种子,不定义则默认为系统当前时间
random.random()
print(random.random())

#蒙得卡罗方法计算圆周率pi,加入进度条
from random import random
from time import perf_counter
DARTS=1000*1000
hits=0.0
start=perf_counter()
print('计算pi程序开始'.center(50//2,'*'))
for i in range(1,DARTS+1):
    x,y=random(),random()
    dist=pow(x**2+y**2,0.5)
    if dist<=1.0:
        hits=hits+1
    #进度条插入
    a='▉'*int(i*(50/DARTS)) #进度条文本框固定为50
    b='▕'*(50-int(i*(50/DARTS)))
    c=(i/DARTS)*100
    end_time=time.perf_counter()
    time_detal=end_time-start_time
    print("\r[{:^3.0f}%{}{}]{:<2.2f}s".format(c,a,b,time_detal),end='')#idle中显示效果不正确，要去python命令行下看执行效果
print('程序结束'.center(50//2,'*'))
   #
pi =4*(hits/DARTS)
print('圆周率的值是：{}'.format(pi))
print('运行时间是：{:5f}'.format(perf_counter()-start))

'''循环会占用大量时间，可以用perf_counter()来探测时间！'''


#绘制七段数码管
import turtle,time


def drawGap():
    turtle.penup()
    turtle.fd(5)

def drawLine(draw):#绘制单段数码管
    drawGap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawGap()
    turtle.right(90)

def drawDigit(digit):
    drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,6,8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if digit in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,2,3,4,7,8,9] else drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)
def drawDate(date):
    turtle.pencolor('red')
    for i in date:
        if i =='-':
            turtle.write('年',font=('Arial',18,'normal'))
            turtle.pencolor('green')
            turtle.fd(40)
        elif i =="=":
            turtle.write('月',font=('Arial',18,'normal'))
            turtle.fd(40)
        elif i =="+":
            turtle.write('日',font=('Arial',18,'normal'))
            turtle.fd(40)
        elif i =="@":
            turtle.write('时',font=('Arial',18,'normal'))
            turtle.fd(40)
        elif i =="$":
            turtle.write('分',font=('Arial',18,'normal'))
            turtle.fd(40)
        elif i =="&":
            turtle.write('秒',font=('Arial',18,'normal'))
            turtle.fd(40)
        else:
            drawDigit(eval(i))

def main():
    turtle.setup(2000,1000,0,0)
    turtle.penup()
    turtle.goto(-800,0)
    turtle.pensize(5)
    drawDate(time.strftime('%Y-%m=%d+%H@%M$%S&',time.localtime()))
    turtle.hideturtle()
    turtle.done()
main()



#基本统计值计算
def getNum(): #获取用户不确定输入
    nums=[]
    iNumstr=input('请输入数字（回车退出）：')
    while iNumstr !='':
        nums.append(eval(iNumstr))
        iNumstr=input('请输入数字（回车退出）：')
    return nums

def mean(numbers):#计算平均值
    s=0.0
    for num in numbers:
        s=s+num
    return  s/len(numbers)

def dev(numbers,mean):
    sdev=0.0
    for num in numbers:
        sdev=sdev+(num-mean)**2
    return pow(sdev/(len(numbers)-1),0.5)

def median(numbers):
        sorted(numbers)
        size=len(numbers)
        if size %2==0:
            med =(numbers[size//2-1]+numbers[size//2])/2
        else:
            med =numbers[size//2]
        return med
n =getNum()
m=mean(n)
print('平均值：{},方差：{:.2},中位数：{}'.format(m,dev(n,m),median(n)))




