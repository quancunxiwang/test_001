from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from page_object.login import Login
from data.data import Read_File

class Test_Login():
    def test_001(self,login):
        '''
        验证有效的用户名和密码是否可以登录成功
        '''
        self.driver=login
        demo=Login(self.driver)

        read_demo=Read_File()
        read_txt=read_demo.read_excel()
        username=read_txt[0][0]
        password=read_txt[0][1]
        
        demo.input_username(username=username)
        demo.input_password(password=password)
        demo.click_login()
        sleep(2)
        demo.click_logout()
        assert login.title=="白月SMS系统 | 登录"
        


    def test_002(self,login):
        '''
        验证只输入用户名，不输入密码是否可以登录成功
        '''
        self.driver=login
        demo=Login(self.driver)

        read_txt=Read_File()
        read_demo=Read_File()
        read_txt=read_demo.read_excel()
        username=read_txt[1][0]
        password=read_txt[1][1]
        
        demo.input_username(username=username)
        demo.input_password(password=password)
        demo.click_login()
        
        assert self.driver.switch_to.alert.text=="请输入密码"
        sleep(1)
        self.driver.switch_to.alert.accept()