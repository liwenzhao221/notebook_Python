"""
linklist.py
功能: 实现单链表的构建和操作
重点代码
"""

# 创建节点类
class Node:
    """
    思路 : *自定义类视为节点类,类中的属性为数据内容
          *写一个next属性,用来和下一个 节点建立关系
    """
    def __init__(self,val,next = None):
        """
        val: 有用数据
        next: 下一个节点引用
        """
        self.val = val
        self.next = next


# 链式线性表操作类
class LinkList:
    """
    思路 : 生成单链表,通过实例化的对象就代表一个链表
          可以调用具体的操作方法完成各种功能
    """
    def __init__(self):
        # 链表的初始化节点,没有有用数据,但是便于标记链表的开端
        self.head = Node(None)

    # 初始化链表,添加一组节点
    def init_list(self,list_):
        p = self.head  # p 作为移动变量
        for i in list_:
            # 遍历到一个值就创建一个节点
            p.next = Node(i)
            p = p.next

    # 遍历链表
    def show(self):
        p = self.head.next  # p代表第一个有值的节点
        while p is not None:
            print(p.val)
            p = p.next  # p向后移动

    # 判断链表为空
    def is_empty(self):
        if self.head.next is None:
            return True
        else:
            return False

    # 清空链表
    def clear(self):
        self.head.next = None

    # 尾部插入
    def append(self,val):
        p = self.head
        # p移动到最后一个节点
        while p.next is not None:
            p = p.next
        p.next = Node(val) # 最后添加节点

    # 头部插入
    def head_insert(self,val):
        node = Node(val)
        node.next = self.head.next
        self.head.next = node

    # 指定位置插入
    def insert(self,index,val):
        # 设置个p 移动到待插入位置的前一个
        p = self.head
        for i in range(index):
            # 如果index超出了最大范围跳出循环
            if p.next is None:
                break
            p = p.next
        # 插入节点
        node = Node(val)
        node.next = p.next
        p.next = node

    # 删除节点
    def remove(self,val):
        p = self.head
        # p 移动,待删除节点上一个
        while p.next is not None and p.next.val != val:
            p = p.next

        if p.next is None:
            raise ValueError("x not in linklist")
        else:
            p.next = p.next.next


    # 获取某个节点的值 (通过索引获取)
    def search(self,index):
        if index < 0:
            raise IndexError("index out of range")

        p = self.head.next
        # 循环移动p
        for i in range(index):
            if p is None:
                raise IndexError("index out of range")
            p = p.next
        return p.val


if __name__ == "__main__":
    # 想有一个链表
    link = LinkList()

    # 初始化一组数据
    l = [1,2,3,4]
    link.init_list(l)
    link.clear()
    print(link.search(0))

    # 链表遍历
    # link.show()
    # link.insert(2,88)
    # link.show()

    # link.clear()
    # print(link.is_empty())





# Abby = Node((1,'Abby',18,'w'))
# Emma = Node((2,'Emma',17,'w'))
# Alex = Node((3,'Alex',19,'m'))
#
# Abby.next = Emma
# Emma.next = Alex

