#coding=utf-8

import unittest

class Multiplication_table(unittest.TestCase):
    def setUp(self):
        print("打印九九乘法表")

    def test_multiplication(self):
        for  i in range(1,10):
            for j in range(i,10):
                s=i*j
                print("%s * %s = %s" % (i,j,s))
                j=j+1
            i=i+1

    def tearDown(self):
        print("九九乘法表打印结束")
if __name__=="__main()__":
    unittest.main()