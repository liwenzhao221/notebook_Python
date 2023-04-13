'''
可以接受客户端什么样的数据访问
'''

from views import *


# 路由列表
# 当请求内容是/time的时候 ，希望用show_time模型进行处理
urls = [
    ('/time',show_time),
    ('/hello',hello),
    ('bye',bye)
]