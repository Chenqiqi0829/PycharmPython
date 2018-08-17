#coding=utf-8
import requests,unittest

class InterfacePost():
    def sentInterface(self,url,serviceNos,query):
        r=requests.post(url,json={'token':'123','serviceNo':serviceNos,'queryCondition':query})
        return r.json()

# Post接口测试
class interfacePostTest(unittest.TestCase):

    def setUp(self):
        self.url="http://192.168.13.141:4042/sw/123/wrapper/custom/getData/v1.0"
        para = {'mysql新2': 'e17a2ff38bf54971a79614641740e890',
                'sqlserver新': 'bdda55e302a8c4c748769637427829c0d',
                'oracle新2': 'ac42d681bdde489a82dc23869af80eb1'}
        self.t=len(para.keys())
        self.va=list(para.values())
        self.ke=list(para.keys())
        self.inter = InterfacePost()

    def test_post_interface(self):
        for i in range(self.t):
            ins=self.inter.sentInterface(self.url,self.va[i],'[]')
            #assert ins['code']=='0'
            #print("接口测试通过,", self.ke[i])
            #print(ins)
            if ins['code'] == '0':
                print("接口测试通过,",self.ke[i])
            else:
                print("接口测试不通过,",self.ke[i])

    def test_interface_eq(self):
        for i in range(self.t):
            ins=self.inter.sentInterface(self.url,self.va[i],'["id":"{"eq":"3"}"]')
            assert ins['code']=='0'
            assert ins['id']=='2'

if __name__=='__main__':
    #unittest.main()
    suite=unittest.TestSuite()
    suite.addTest('test_post_interface')
    suite.addTest('test_interface_eq')
    runner=unittest.TextTestRunner()
    runner.run(suite)
