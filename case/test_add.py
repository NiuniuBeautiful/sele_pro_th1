# coding:utf-8

import unittest
def add(a,b):
    return a+b
class Test1(unittest.TestCase):
    def test_01(self):
        c = add(3, 3) # 实际结果
        ex = 6 # 期望结果
        self.assertEqual(c,ex) #断言
if __name__ == "__main__":
    unittest.main()