# coding:utf-8

import unittest
import time

from common.HTMLTestRunner_yo import HTMLTestRunner

discover = unittest.defaultTestLoader.discover("E:\\PycharmProjects\\sele_qijubang_pro\\case","test*.py")

# 打印出现,目录是否正确

print(discover)
# discover2 = unittest.defaultTestLoader.discover("E:\\PycharmProjects\\sele_qijubang_pro\\case","test*.py")
#
# all = unittest.TestSuite()
#
# for i in discover1:
#     all.addTest(i)
# for j in discover2:
#     all.addTest(j)
# print(all)

nowtime = time.strftime("%Y_%m_%d %H_%M_%S")
print(nowtime)

reportpath = "E:\\PycharmProjects\\sele_qijubang_pro\\report"+"\\report%s.html" % nowtime
fp = open(reportpath, "wb")

runner = HTMLTestRunner(fp,verbosity=2, title="测试报告",
                        description="报告内容", retry=1)
runner.run(discover)