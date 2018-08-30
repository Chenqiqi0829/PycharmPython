#coding=utf-8

class test_lianxi_11_20:
    # 【程序12】
    # 题目：判断101 - 200之间有多少个素数，并输出所有素数
    # 定义为在大于1的自然数中，除了1和它本身以外不再有其他因数,如3,5,7,11,13
    def test_12(self):
        sunum=[]
        for i in range(101,201):
            s = 0
            for j in range(2,i):
                if i%j==0:
                    break
                else:
                    s=s+1
                    if s==i-2:
                        sunum.append(i)
        print(len(sunum),sunum)

    # 【程序13】
    # 题目：打印出所有的“水仙花数”，所谓“水仙花数”是指一个三位数，其各位数字立方和等于该数本身。
    # 例如：153是一个“水仙花数”，因为153 = 1的三次方＋5的三次方＋3的三次方
    def test_13(self):
        print("水仙花数有：")
        for i in range(1,10):
            for j in range(0,10):
                for k in range(0,10):
                    total=i*100+j*10+k
                    if total==i*i*i+j*j*j+k*k*k:
                        print(total)

    # 【程序14】
    # 题目：将一个正整数分解质因数。例如：输入90, 打印出90 = 2 * 3 * 3 * 5。
    def test_14(self):
        print("请输入正整数：")
        num=input()
        if num.isdigit()==False:
            while True:
                print("您输入不对，请输入正整数：")
                num=input()
                if num.isdigit() and int(num)>2:
                    break
        total=int(num)
        li=[]
        s=0
        for i in range(2,total-1):
            if total%i==0:
                if total==2:
                    print(num,"不是质数")
                else:
                    while True:
                        total=total/i
                        li.append(i)
                        if total%i!=0:
                            break
            else:
                s=s+1
                if s==i:
                    print(num,"不是质数")
        print("质数的因子有",li)
        s=li[0]
        for i in range(1,len(li)):
            s=str(s)+'*'+str(li[i])
        print("%s=%s"%(num,s))

    # 【程序17】
    # 题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
    def test_17(self):
        s=input("input a string:")
        abc=0
        null=0
        num=0
        other=0
        for i in s:
            if i.isdigit():
                num+=1
            elif i.isspace():
                null+=1
            elif i.isalpha():
                abc+=1
            else:
                other+=1
        print("英文字母有%d个，空格有%d个，数字有%d个，其他字符有%d个" % (abc,null,num,other))

    # 【程序18】
    # 题目：求s = a + aa + aaa + aaaa + aa...a的值，其中a是一个数字。例如2 + 22 + 222 + 2222 + 22222(此时共有5个数相加)，
    # 几个数相加有键盘控制。
    def test_18(self):
        a=int(input("input a number:"))
        s=int(input("input add number:"))
        re=0
        if s==1:
            print("the result is :",a)
        else:
            total=a
            for i in range(2,s+1):
                total=total*10
                total=total+a
                re=re+total
            print("the result is:",re+a)

    # 【程序19】
    # 题目：一个数如果恰好等于它的因子之和，这个数就称为“完数”。例如6 = 1＋2＋3.
    # 编程找出1000以内的所有完数。
    def test_19(self):
        s=[]
        for i in range(2,1001):
            t=i
            li = [1]
            total = 0
            for j in range(2,i):
                if i%j==0:
                    while True:
                        i=i/j
                        li.append(j)
                        if i%j!=0:
                            break
            for k in li:
                total=total+int(k)
            if t==total:
                s.append(t)
        print(s)



if __name__=='__main__':
    test=test_lianxi_11_20()
    #test.test_12()
    #test.test_13()
    #test.test_14()
    #test.test_17()
    #test.test_18()
    test.test_19()


