"""
从终端输入一个单词,
可以打印出单词及其解释,
如果没有这个单词则打印 "没有该单词
"""

word = input("Word:")  # 要查找的单词

# 打开文件 'r'
f = open('dict.txt')

# 每次获取一行
for line in f:
    w = line.split(' ')[0]
    # 如果遍历到的单词已经大于目标,就结束查找
    if w > word:
        print("没有找到该单词")
        break
    elif w == word:
        print(line)
        break
else:
    print("没有找到单词")

f.close()

