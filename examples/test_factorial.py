#coding=utf-8
import unittest

class test_factorial():

    def factorial(self):
        print("请输入要计算的阶乘数！")
        num=input()
        s=num
        if num.isdigit():
            for i in range(1,int(num)):
                s=int(s)*int(i)
            print("%s 的阶乘是：%s" %(num,s))
        else:
            print("请输入正整数！")
            m=test_factorial()
            m.factorial()
if __name__=='__main__':
    a=test_factorial()
    a.factorial()