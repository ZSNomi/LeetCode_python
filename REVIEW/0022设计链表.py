# 你可以选择使用单链表或者双链表，设计并实现自己的链表。
# 单链表中的节点应该具备两个属性：val 和 next 。val 是当前节点的值，next 是指向下一个节点的指针/引用。
# 如果是双向链表，则还需要属性 prev 以指示链表中的上一个节点。假设链表中的所有节点下标从 0 开始。

# 实现 MyLinkedList 类：
# MyLinkedList() 初始化 MyLinkedList 对象。
# int get(int index) 获取链表中下标为 index 的节点的值。如果下标无效，则返回 -1 。
# void addAtHead(int val) 将一个值为 val 的节点插入到链表中第一个元素之前。在插入完成后，新节点会成为链表的第一个节点。
# void addAtTail(int val) 将一个值为 val 的节点追加到链表中作为链表的最后一个元素。
# void addAtIndex(int index, int val) 将一个值为 val 的节点插入到链表中下标为 index 的节点之前。如果 index 等于链表的长度，那么该节点会被追加到链表的末尾。如果 index 比长度更大，该节点将 不会插入 到链表中。
# void deleteAtIndex(int index) 如果下标有效，则删除链表中下标为 index 的节点。

# 示例：
# 输入
# ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
# [[], [1], [3], [1, 2], [1], [1], [1]]
# 输出
# [null, null, null, null, 2, null, 3]
# 解释
# MyLinkedList myLinkedList = new MyLinkedList();
# myLinkedList.addAtHead(1);
# myLinkedList.addAtTail(3);
# myLinkedList.addAtIndex(1, 2);    // 链表变为 1->2->3
# myLinkedList.get(1);              // 返回 2
# myLinkedList.deleteAtIndex(1);    // 现在，链表变为 1->3
# myLinkedList.get(1);              // 返回 3

#定义节点结构体
class Lnode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

#定义响应的方法：
class Operate:
    #初始化方法:建立虚拟头结点以及链表长度
    def __init__(self):
        self.myLinkedlist = Lnode()
        self.size = 0


    #实现功能：int get(int index) 获取链表中下标为 index 的节点的值。如果下标无效，则返回 -1 。
    def get_index(self,index):
        #判断下标是否有效
        if index<0 or index>=self.size:#用等于是因为链表下标是从0开始算起
            return -1

        #建立一个指针指向链表
        cur = self.myLinkedlist.next

        for _ in range(index):
            cur = cur.next

        return cur.val

    #实现功能：void addAtIndex(int index, int val) 将一个值为 val 的节点插入到链表中下标为 index 的节点之前。如果 index 等于链表的长度，那么该节点会被追加到链表的末尾。如果 index 比长度更大，该节点将 不会插入 到链表中。
    def addAtIndex(self,index,val):#对列表进行原地操作（增加节点），无需任何返回
        #检查index的有效性
        if index<0 or index>self.size:
            return

        #创建指针cur指向链表。
        cur = self.myLinkedlist

        #遍历链表，让cur指向index的前一个节点
        for _ in range(index):
            cur = cur.next

        #创建值为val的节点并将其插入到链表当中
        new_node = Lnode(val)
        new_node.next = cur.next
        cur.next = new_node

        #更新size的大小
        self.size += 1

    #实现功能：void addAtHead(int val) 将一个值为 val 的节点插入到链表中第一个元素之前。在插入完成后，新节点会成为链表的第一个节点。
    def addAtHead(self,val):
        self.addAtIndex(0,val)

    #实现功能：void addAtTail(int val) 将一个值为 val 的节点追加到链表中作为链表的最后一个元素。
    def addAtTail(self,val):
        self.addAtIndex(self.size,val)

    #实现功能：void deleteAtIndex(int index) 如果下标有效，则删除链表中下标为 index 的节点。
    def deleteAtIndex(self,index):
        #判断下标是否有效
        if index<0 or index>=self.size:
            return

        #创建指针cur让其指向链表头节点
        cur = self.myLinkedlist

        #遍历链表，让cur指向index的前一个节点
        for _ in range(index):
            cur = cur.next

        cur.next = cur.next.next

        #更新链表长度：
        self.size -= 1

#辅助函数：将数组转变为链表：
def tuple_become_linklist(head):
    #数组为空
    if not head:
        return None

    #建立一个值为默认值0的头结点
    top = Lnode()

    #建立一个指向头结点的指针
    cursor = top

    #建立节点、为节点赋值、链接链表
    for val in head:
        node = Lnode(val) #从元组中取出值并赋值给节点cur
        cursor.next = node
        cursor = cursor.next

    return top.next

#辅助函数：将链表转化为数组（用于最后结果的打印）
def linklist_become_tuple(linklist:Lnode):
    #建立一个空数组
    new_list = []

    #创建一个指针指向首节点
    cur = linklist

    #用cur遍历指针，并将遍历得到的值添加到数组当中
    while cur:
        new_list.append(cur.val)
        cur = cur.next

    return new_list


if __name__ == "__main__":
    obj = Operate()

    obj.addAtHead(1)
    obj.addAtTail(3)
    obj.addAtIndex(1, 2)

    print(obj.get_index(1))   # 2

    obj.deleteAtIndex(1)

    print(obj.get_index(1))   # 3
    print(linklist_become_tuple(obj.myLinkedlist.next))  # [1, 3]




