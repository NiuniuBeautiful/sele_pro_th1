import os
'''
获取文件路径
'''
print(__file__)

real = os.path.realpath(__file__)  # 真实路径

print(real)

# 当前脚本的文件夹路径
dirname = os.path.dirname(real)

print(dirname)

gc = os.path.dirname(dirname)

print(gc)

# 进common

com = os.path.join(gc, "common")

print(com)