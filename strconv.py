#1.1字符串的拼接
##str1 = input("请输入一个人的名字：")
##str2 = input("请输入一个地点：")
##print("世界这么大，{}想去{}看看。".format(str1,str2))
#------------------------------------#
#eval():eval函数将字符串当成有效Python表达式来求值，并返回计算结果
#与之对应的repr（）函数，它能够将Python的变量和表达式转换为字符串表示
#1.2整数序列求和
##n = input("请输入一个整数N：")
##sum = 0
##for i in range(int(n)):#或者调和函数eval(n)
##    print(i,end = ' ')
##    sum = sum + i+1
##print("1到N求和结果为：",sum)
#--------------------------------------#
#1.3 9*9乘法表
#版本一
##for i in range(1,10):
##    for m in range(1,i+1):
##        sum = i*m
##        if m < i:
##            if sum < 10:
##                print(m,'*',i,"= {}".format(sum),end = '  ')
##            else:
##                print(m,'*',i,'=',sum,end = ' ')
##        else:
##            print(m,'*',i,'=',sum)
#版本二
##for i in range(1,10):
##    for j in range(1,i+1):
##        print("{} * {} = {:2}".format(j,i,i*j),end = ' ')
##    print('')
#-----------------------------------------------#
#---------1.4 计算1+2!+3!+4!+...+10!------------#
##sum,tmp = 0,1
##for i in range(1,11):
##    tmp *= i
##    sum += tmp
##print("1+2!+3!+4!+...+10!=",sum)
#------------------------------------------------#
#---------1.5 猴子吃桃问题 ----------------------#
#list(range(5,0,-1)) -----  [5, 4, 3, 2, 1]
##n = 1
##for i in range(5,0,-1):
##    n = (n+1)*2  #n = (n+1)<<1 左移一位乘以2
##print(n)
#-------------------------------------------------#
#--------1.6 健康食谱输出 ------------------------#
##diet = ['西红柿','土豆','鸡蛋','黄瓜','青菜']
##for i in range(5):
##    for j in range(5):
##        if (i != j):
##            print(diet[i],diet[j],sep = '炒')
#-------------------------------------------------#
#--------1.7 绘制五角星 --------------------------#
##from turtle import *
####fillcolor("red")
##color('red','yellow') #color('线条颜色','填充颜色')
##begin_fill()
##while True:
##    forward(200)
##    right(144)
##    if abs(pos()) < 1:
##        break
##end_fill()
#-------------------------------------------------#
#------1.8 太阳花的绘制 --------------------------#
##from turtle import *
##color('red','yellow')
##begin_fill()
##while True:
##    forward(200)
##    left(170)
##    if abs(pos()) <1:
##        break
##end_fill()
##done()
#---------------------------------------------------#
#输出某个整数或浮点数的0~5次方
#import math # 导入 math 模块
##a = input()
##print(pow(eval(a),0), pow(eval(a),1),pow(eval(a),2),pow(eval(a),3),pow(eval(a),4),pow(eval(a),5))
#---------------------------------------------------#

#---------------------20180406------------------------------#
#---------------温度转换程序1.1 P35-------------------------#
##TempStr = input("请输入带有符号的温度值：")
##if TempStr[-1] in ['F','f']:
##    C = (eval(TempStr[0:-1]) - 32) / 1.8
##    print("华氏温度{}转换为摄氏度温度是：{:.2f}C".format(TempStr,C))
##elif TempStr[-1] in ['C','c']:
##    F = eval(TempStr[0:-1])*1.8 + 32
##    print("摄氏温度{}转换为华氏温度是：{:.2f}F".format(TempStr,F))
##else:
##    print("输入格式错误")
#-----------------循环输入----------------------------------#
##TempStr = input("请输入带有符号的温度值：")
##while TempStr[-1] not in ['N','n']:
##    if TempStr[-1] in ['F','f']:
##        C = (eval(TempStr[0:-1]) - 32) / 1.8
##        print("华氏温度{}转换为摄氏度温度是：{:.2f}C".format(TempStr,C))
##    elif TempStr[-1] in ['C','c']:
##        F = eval(TempStr[0:-1])*1.8 + 32
##        print("摄氏温度{}转换为华氏温度是：{:.2f}F".format(TempStr,F))
##    else:
##        print("输入格式错误")
##    TempStr = input("请输入带有符号的温度值：")
#-----------------------------------------------------------------#
#PythonDraw.py
#------------------------蟒蛇绘制-------------------#
#import 引入一个绘图库
import turtle
#turtle的绘图窗体
#turtle.setup(width,height,startx,starty)
turtle.setup(650,350,200,200)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.pencolor("violet")
turtle.seth(-40)
for i in range(4):
    turtle.circle(40,80)
    turtle.circle(-40,80)
##turtle.penup()
##turtle.circle(40,120)
##turtle.circle(-40,180)
##turtle.pendown()
##turtle.setheading(-90)
##turtle.fd(300)
##turtle.setheading(180)
##turtle.circle(20,360)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,120)
turtle.fd(40)
turtle.done()
