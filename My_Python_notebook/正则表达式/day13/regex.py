"""
regex.py  re模块 功能函数演示1
"""

import re

# 目标字符串
s = "Alex:1994,Sunny:1999"
pattern = r"(\w+):(\d+)" # 正则表达式

# re调用函数
l = re.findall(pattern,s)
print(l)

# regex表达式对象调用函数
regex = re.compile(pattern)
l = regex.findall(s,) # 截取s[0:13]作为匹配目标
print(l)

# 按照正则匹配的内容,分割目标
l = re.split(r'[,:]',s)
print(l)

# 使用字符串替换匹配到的部分
s = re.subn(r':','-',s,1)
print(s)








