# coding:utf-8
import unittest
from selenium import webdriver
import time

class TestLogin(unittest.TestCase):
    u'''测试登录功能点'''
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Firefox()


    def setUp(self):
        self.driver.get("https://qijubang.cqbornsoft.com")
        time.sleep(2)

    # 登录成功
    def test_03(self):
        u'''测试登录账号 xy001,密码：z111111,登录成功'''
        self.driver.find_element_by_id("userName").send_keys("xy001")

        self.driver.find_element_by_id("passwords").send_keys("z111111")

        self.driver.find_element_by_id("verificationaCode").send_keys("8888")
        time.sleep(1)
        self.driver.find_element_by_class_name("u-button").click()
        time.sleep(2)
        t = self.driver.find_element_by_css_selector("span:nth-child(2)").text

        print(t)

        self.assertTrue(t == "xy001")

    # 用户名错误登录失败
    def test_01(self):
        u''' 测试登录账号 xy00,密码：z111111,登录用户名错误 '''
        self.driver.find_element_by_id("userName").send_keys("xy00")

        self.driver.find_element_by_id("passwords").send_keys("z111111")

        self.driver.find_element_by_id("verificationaCode").send_keys("8888")
        time.sleep(1)
        self.driver.find_element_by_class_name("u-button").click()
        time.sleep(2)
        t = self.driver.find_element_by_id("userName-error").text

        print(t)

        self.assertTrue(t == "用户名不存在")

    #密码为空登录失败
    def test_02(self):
        u''' 测试登录账号--密码为空 '''
        self.driver.find_element_by_id("userName").clear()
        time.sleep(1)
        self.driver.find_element_by_id("userName").send_keys("xy001")

        self.driver.find_element_by_id("passwords").send_keys("")

        self.driver.find_element_by_id("verificationaCode").send_keys("8888")
        time.sleep(1)
        self.driver.find_element_by_class_name("u-button").click()
        time.sleep(2)
        t = self.driver.find_element_by_id("passwords-error").text

        print(t)

        self.assertTrue(t == "密码必填")

    def tearDown(self):
        self.driver.delete_all_cookies() #退出登录

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    # def tearDown(self):
    #
    #     self.driver.quit()
if __name__ == "__main__":

    unittest.main()