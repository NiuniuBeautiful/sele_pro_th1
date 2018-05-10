from selenium import webdriver
import unittest
from page.loginpage import loginpage
import  ddt

# 参数和代码分离
testdata = [

    {"username": "xy001", "pws": "z111111", "code": "8888", "result": "xy001"},

    {"username": "xy002", "pws": "z111111", "code": "8888", "result": "xy002"},

    {"username": "xy003", "pws": "z111111", "code": "8888", "result": "xy003"},

    {"username": "xy004", "pws": "z111111", "code": "8888", "result": "xy004"}]
@ddt.ddt
class LoginCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.loginpage = loginpage(cls.driver)

    def login_case(self, username, pws, code):
        # 登录
        self.loginpage.login(username, pws, code,)

        # 获取实际结果
        result = self.loginpage.get_login_result()

        return result

    @ddt.data(*testdata)
    def test_login_01(self, case1):
        res = self.login_case(case1["username"], case1["pws"], case1["code"])
        self.assertEqual(case1["result"] == res)

    def tearDown(self):
        self.driver.delete_all_cookies()

        self.driver.refresh()


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()