


import re

f = open('CSS.txt',encoding='utf-8')
w = open('CSS_Finish.txt','w',encoding='utf-8')
data=''
for line in f.read():
    data += line
    if line == '}':
        data += '\n'

w.write(data)

# print(data)

# pattern = r"(.+})" # 正则表达式
# l = re.findall(pattern,data)
# print(l)
#print(l[1])
#print(l[2])

# for line in l:
#     w.write(line+'\n')