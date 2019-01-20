
#蒙得卡罗方法计算圆周率pi,加入进度条
from random import random
from time import perf_counter
import time
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

    time_detal=end_time-start
    #print()多次刷新函数会占用大量时间！！
    print("\r[{:^3.0f}%{}{}]{:<2.2f}s".format(c,a,b,time_detal),end='')#idle中显示效果不正确，要去python命令行下看执行效果
print('程序结束'.center(50//2,'*'))
   #
pi =4*(hits/DARTS)
print('圆周率的值是：{}'.format(pi))
print('运行时间是：{:5f}'.format(perf_counter()-start))


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
