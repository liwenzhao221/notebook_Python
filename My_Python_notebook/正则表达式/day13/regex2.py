"""
regex2.py
match对象属性实例
"""

import re

pattern = r"(ab)cd(?P<pig>ef)"
regex = re.compile(pattern)
obj = regex.search("abcdefghi",0,7)  # match对象

# 属性变量
print(obj.pos)  # 目标字符串开始位置
print(obj.endpos) # 目标字符串结束位置
print(obj.re)  # 正则
print(obj.string) # 目标字符串
print(obj.lastgroup) # 最后一组组名
print(obj.lastindex) # 最后一组序号

print("=====================================")
# 属性方法
print(obj.span()) # 匹配到的内容在目标字符串中的位置
print(obj.start())
print(obj.end())
print(obj.groups()) # 子组内容对应的元组
print(obj.groupdict()) # 捕获组字典
print(obj.group()) # 获取match对象内容
print(obj.group('pig'))





