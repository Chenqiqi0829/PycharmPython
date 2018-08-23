#coding=utf-8
import math
class test_lianxi_1_10:
# 【程序1】：
# 题目：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
    def test_01(self):
            s=0
            for i in range(1,5):
                for j in range(1,5):
                    for k in range(1,5):
                        if i!=j and j!=k and i!=k:
                            s=s+1
                            print(i*100+j*10+k)
            print("三位数一共有:",s)

# 【程序2】
# 题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可可提成7.5%；
# 20万到40万之间时，高于20万元的部分，可提成5%；
# 40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%，
# 高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
    def test_02(self):
        print("请输入利润：")
        i=input()
        result=i.isdigit()
        while result==False:
            print("请输入正确的利润：")
            i=input()
            if i.isdigit():
                break
        sale=int(i)
        if sale<=10:
            print("应发奖金总数为：",round(sale*0.1,2),"万元")
        elif  10<sale<=20:
            total=10*0.1+(sale-10)*0.075
            print("应发奖金总数为：", round(total, 2), "万元")
        elif  20<sale<=40:
            total=10*0.1+(sale-10)*0.075+(sale-20)*0.05
            print("应发奖金总数为：", round(total, 2), "万元")
        elif 40<sale<=60:
            total=10*0.1+10*0.075+20*0.005+(sale-40)*0.03
            print("应发奖金总数为：", round(total, 2), "万元")
        elif 60<sale<=100:
            total=10*0.1+10*0.075+20*0.005+20*0.003+(sale-60)*0.015
            print("应发奖金总数为：", round(total, 2), "万元")
        else:
            total=10*0.1+10*0.075+20*0.005+20*0.003+40*0.015+(sale-100)*0.01
            print("应发奖金总数为：", round(total, 2), "万元")

# 【程序3】
# 题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
    def test_03(self):
        result=True
        s=1
        while 1<=s<=10000:
            m=math.sqrt(s+100)
            n=math.sqrt(s+268)
            if m-int(m)==0 and n-int(n)==0:
                print("这个整数是：", s)
                break
            s=s+1




if __name__=='__main__':
    test=test_lianxi_1_10()
    #test.test_01()
    #test.test_02()
    test.test_03()