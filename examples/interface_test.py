#coding=utf-8
import requests
import json
url1={'mysql旧':'http://192.168.13.141:4042/sw/serviceApi/09f4fef9249c457ca67b4a7a45823730/interface/51aa655ec2734aa4a5f38bae78a7fc3a/customWrapper',
      'sqlserver旧':'http://192.168.13.141:4042/sw/serviceApi/09f4fef9249c457ca67b4a7a45823730/interface/bd3f6e5debb34d94b63688d40bbbb244/customWrapper',
      'oracle旧':'http://192.168.13.141:4042/sw/serviceApi/09f4fef9249c457ca67b4a7a45823730/interface/c2e5e94645dc4e99bc34bbcbc18bfb1a/customWrapper'}

# get类型的接口
for i in range(len(url1.values())):
    r1=requests.get(list(url1.values())[i])
    result1=r1.json()
    if result1['state']==True:
        print("接口测试通过,",list(url1.keys())[i])
    else:
        print("接口测试不通过,", list(url1.keys())[i])

# post类型的接口
url2="http://192.168.13.141:4042/sw/123/wrapper/custom/getData/v1.0"
para={'mysql新2':'e17a2ff38bf54971a79614641740e890',
      'sqlserver新':'bdda55e32a8c4c748769637427829c0d',
      'oracle新2':'ac42d681bdde489a82dc23869af80eb1'}
for i in range(len(para.keys())):
    r2 = requests.post(url2, json={'token':'123','serviceNo':list(para.values())[i]})
    result2 = r2.json()
    if result2['code'] == '0':
        print("接口测试通过,", list(para.keys())[i])
    else:
        print("接口测试不通过,", list(para.keys())[i])


