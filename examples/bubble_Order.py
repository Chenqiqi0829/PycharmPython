#coding=utf-8

# 冒泡排序
m=[10,5,8,45,65,158,23,14,1,100,78,142]
print("排序前m数组为",m)
for i in range(len(m)):
    for j in range(i+1,len(m)):
        if m[i]>m[j]:
            t=m[i]
            m[i]=m[j]
            m[j]=t
        j=j+1
    i=i+1
print("排序后m数组为",m)

# 插入一个数字然后排序
x=input()
print("插入一个数字",x)
m.append(int(x))
print(m)
for i in range(len(m)-1):
    if m[len(m)-i-1]<m[len(m)-i-2]:
        t=m[len(m)-i-2]
        m[len(m)-i-2]=m[len(m)-i-1]
        m[len(m)-i-1]=t
    i=i+1
print("插入一个数字后排序为",m)




