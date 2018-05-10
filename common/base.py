# coding:utf-8

from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base():


    def __init__(self, driver):
        self.driver = driver

        self.timeout = 30
        self.poll = 0.5

    def findElement(self, locl):

        element = WebDriverWait(self.driver, self.timeout, self.poll, ElementNotVisibleException).until(lambda x: x.find_element(*locl))
        return element

    def findElementNew(self, locl):
        element = WebDriverWait(self.driver, self.timeout, self.poll, ).until(EC.title_contains("发送"))
        return element

    def findElements(self, locl):
        elements = WebDriverWait(self.driver, self.timeout, self.poll).until(lambda x: x.find_element(*locl))
        return elements

    def sendKeys(self, loctor, text):
        ele = self.findElement(loctor)
        ele.send_keys(text)

    def click(self, loctor):

        ele =self.findElement(loctor)
        ele.click()

    def clear(self, loctor):
        ele = self.findElement(loctor)
        ele.clear()

    def js_scroll_end(self):

        '''滚动到浏览器底部'''

        js_heig = "window.scrollTo(0, document.body.scrollHeight)"

        self.driver.execute_script(js_heig)

    def js_focut(self, loctor):

        '''自动聚焦到元素'''

        targe = self.findElement(loctor)

        self.driver.execute_script("argements[0].scrollIntoView()", targe)


    def js_scroll_top(self):

        ''' 浏览器回到顶部 '''

        js = "window.scrollTo(0, 0)"

        self.driver.execute_script(js)


if __name__ == "__main__":

    driver = webdriver.Firefox()

    base = Base(driver)

    driver.get("https://www.baidu.com")

    locl1 = ("id", "kw") # 定位百度输入框
    base.sendKeys(locl1, "发送内容")

    locl2 = ("css selector", "#su")

    base.click(locl2)