from common.base import Base
from selenium import webdriver
class loginpage(Base):
    '''登录页面'''
    user_loc = ("id", "userName")
    pws_loc = ("id", "passwords")
    code_loc = ("id", "verificationaCode")
    sub_loc = ("class", "button")
    xxx_loc = ("text", "text")
    def open_login_page(self):
        '''打开登录页面'''
        self.driver.get("https://qijubang.cqbornsoft.com")


    def logout(self):
        '''登出'''
        #driver = webdriver.Firefox
        self.driver.delete_all_cookies()
        self.driver.refresh()
    def input_user(self):
        '''输入用户名'''
        pass
    def input_pws(self):
        '''输入密码'''
        pass
    def input_code(self):
        '''输入验证码'''
        pass
    def sub_button(self):
        '''点击登录按钮'''
        self.sub_button().click()

    def login(self, userName="xy001lk", pws="z111111", code="8888"):
        '''登录'''
        self.open_login_page()
        self.input_user(userName)
        self.input_pws(pws)
        self.input_code(code)
        self.sub_button()

    def get_login_result(self):
        try:
            t = self.findElement(self.xxx_loc).text
            return t
        except:
            print("返回字符为空")
            return " "