#coding=utf-8

# 字符串
print("字符串：")
# a.移除name变量对应的值两边的空格，并输入移除有的内容
name = " aleX "
print("a:",name.strip())
# b.判断name变量对应的值是否以 "al"开头，并输出结果
name="  aleX  "
print("b:",name.startswith('al'))
# c.判断name变量对应的值是否以 "X"结尾，并输出结果
name="  aleX"
print("c:",name.endswith('X'))
# d.将name变量对应的值中的 " l" 替换为 " p"，并输出结果
name="  aleX  "
print("d:",name.replace('l','p'))
# e.将name变量对应的值根据 " l" 分割，并输出结果。
name="  aleX  "
print("e:",name.split('l'))
# f.请问，上一题 e分割之后得到值是什么类型？
name="  aleX  "
print("f:",type(name.split('l')))
# g.将name变量对应的值变大写，并输出结果
name="  aleX  "
print("g:",name.strip().upper())
# h.将name变量对应的值变小写，并输出结果
name="  aleX  "
print("h:",name.lower())
# i.请输出name变量对应的值的第2个字符？
name="  aleX  "
print("i:",name.strip()[1])
# j.请输出name变量对应的值的前3个字符？
name="  aleX  "
print("j:",name.strip()[:3])
# k.请输出name变量对应的值的后2个字符？
name="  aleX  "
print("k:",name.strip()[-2:])
# l.请输出name变量对应的值中 "e" 所在索引位置？
name="  aleX  "
print("l:",name.strip().index('e'))

# 列表
print("\n列表：")
# a.计算列表长度并输出
li = ['alex','eric','rain']
print("li.a:",len(li))
# b.列表中追加元素"seven"，并输出添加后的列表
li.append("seven")
print("li.b:",li)
# c.请在列表的第1个位置插入元素 "Tony"，并输出添加后的列表
li.insert(0,"Tony")
print("li.c:",li)
# d.请修改列表第2个位置的元素为 "Kelly"，并输出修改后的列表
li[1]="Kelly"
print("li.d:",li)
# e.请删除列表中的元素"eric"，并输出修改后的列表
li.remove("eric")
print("li.e:",li)
# f.请删除列表中的第2个元素，并输出删除的元素的值和删除元素后的列表
print("li.f1:",li[1])
li.pop(1)
print("li.f2:",li)
# g.请删除列表中的第3个元素，并输出删除元素后的列表
li.pop(2)
print("li.g:",li)
# h.请删除列表中的第2至4个元素，并输出删除元素后的列表
li = ['Tony','alex','eric','rain']
del li[1:4]
print("li.h:",li)
# i.请将列表所有的元素反转，并输出反转后的列表
li = ['Tony','alex','eric','rain']
print("li.i:",li[::-1])
# j.请使用for、len、range 输出列表的索引
li = ['Tony','alex','eric','rain']
for i in range(len(li)):
    print(i)
# k.请使用enumrate输出列表元素和序号（序号从 100 开始）
for k,i in enumerate(li,100):
    print("li.k:",k,i)
# l.请使用for循环输出列表的所有元素
for i in li:
    print("li.l:",i)

# 字典
dic={'k1':"v1","k2":"v2","k3":[11,22,33]}
# a. 请循环输出所有的 key
for i in dic.keys():
    print("dic.a:",i)
# b. 请循环输出所有的 value
for i in dic.values():
    print("dic.b:",i)
# c. 请循环输出所有的 key 和 value
for i,j in dic.items():
    print("dic.c:",i,j)
# d. 请在字典中添加一个键值对， "k4":"v4"，输出添加后的字典
dic["k4"]="v4"
print("dic.d:",dic)
# e. 请在修改字典中 "k1" 对应的值为 "alex"，输出修改后的字典
dic["k1"]="alex"
print("dic.e:",dic)
# f. 请在 k3 对应的值中追加一个元素 44，输出修改后的字典
i=dic.get("k3")
i.append(44)
dic["k3"]=i
print("dic.f:",dic)
# g. 请在 k3 对应的值的第 1 个位置插入个元素 18，输出修改后的字典
dic["k3"].insert(0,18)
print("dic.g:",dic)

