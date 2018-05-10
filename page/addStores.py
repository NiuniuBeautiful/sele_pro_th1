
from selenium import webdriver
from common.base import Base

class AddStores(Base):
    driver = webdriver.Firefox()
    driver.find_element_by_link_text("分店管理").click()
    driver.find_elements_by_xpath(".//*[@class='xui-a-con commodityCenter']")[1].click()

    store_loc = ("link text", "分店管理")  # 分店管理
    add_store_loc = ("xpath", ".//*[@class='xui-short-button newStore']")  # 新增分店
    stor_user_loc = ("id", "userName")
    stor_name_loc = ("id", "storeName")

    def sub_click(self):
        ''' 点击新增分店 '''
        # self.add_store_loc.
    def input_bug_title(self):
        ''' 输入标题 '''
        pass
    def input_bug_detail(self):
        '''输入bug详情'''
        pass