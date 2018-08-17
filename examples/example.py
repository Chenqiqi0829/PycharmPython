#coding=utf-8
from selenium import webdriver
import unittest,time

class VisitTest(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()

    def test_visit(self):
        self.driver.get("http://www.baidu.com")
        self.driver.maximize_window()
        print(self.driver.title)
        print(self.driver.current_url)
        assert self.driver.title.find("百度一下")>=0,"打开错误"
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()

if __name__=='__main__':
    unittest.main()
