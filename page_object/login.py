from selenium.webdriver.common.by import By

class Login():
    def __init__(self,driver):
        self.driver=driver
        self.account_ele=By.ID,"username"
        self.password_ele=By.ID,"password"
        self.login_ele=By.XPATH,"/html/body/div/div[2]/div[1]/div[3]/div"
        self.logout1_ele=By.XPATH,'//*[@id="root"]/header/nav/div/ul/li[2]/a'
        self.logout2_ele=By.XPATH,'//*[@id="root"]/header/nav/div/ul/li[2]/ul/li[3]/div[2]'


    def input_username(self,username):
        self.driver.find_element(*self.account_ele).clear()
        if username is not None and username !="":
            self.driver.find_element(*self.account_ele).send_keys(username)

    def input_password(self,password):
        self.driver.find_element(*self.password_ele).clear()
        if password is not None and password !="":
            self.driver.find_element(*self.password_ele).send_keys(password)


    def click_login(self):
        self.driver.find_element(*self.login_ele).click()

    def click_logout(self):
        self.driver.find_element(*self.logout1_ele).click()
        self.driver.find_element(*self.logout2_ele).click()