# 给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。

# 示例1：
# 输入：head = [1,2,6,3,4,5,6], val = 6
# 输出：[1,2,3,4,5]

#示例2：
# 输入：head = [], val = 1
# 输出：[]

# 示例3：
# 输入：head = [7,7,7,7], val = 7
# 输出：[]

#1:类：定义节点
class LinkedNode:
    #初始化对象
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

#2.类：方法：删除目标节点
class LinkList_manege:
    #定义方法：
    def delete_val(self,head:LinkedNode,val:int)->LinkedNode:
        #添加一个首节点，并让首节点指向链表的第一个节点：
        top = LinkedNode(0,head)#实例化名为top的一个对象

        #定义一个cursor节点用来遍历
        cursor = top

        while cursor.next:
            if cursor.next.val == val:
                cursor.next = cursor.next.next
            else:
                cursor = cursor.next
        return top.next


#辅助方法1：将元组转化为链表：
def tuple_become_linklist(array_head):
    if not array_head:
        return None
    #实例化一个节点
    list_head = LinkedNode(0)

    #定义一个cursor：
    cursor = list_head

    for val in array_head:
        cursor.next = LinkedNode(val)
        cursor = cursor.next
    return list_head.next

#辅助方法2：将链表转化为数组
def linklist_become_tuple(linklist):
    #初始化一个数组：
    arr = []

    #声明一个指针：
    cur = linklist

    while cur:
        arr.append(cur.val)
        cur = cur.next

    return arr

if __name__ == "__main__":

    # head = [1, 2, 6, 3, 4, 5, 6]
    # val = 6
    # 输出：[1,2,3,4,5]

    # head = []
    # val = 1
    # 输出：[]

    head = [7, 7, 7, 7]
    val = 7
    # 输出：[]

    #1.将数组转化成链表
    head1 = tuple_become_linklist(head)
    #2.调用方法
    linklist_manege = LinkList_manege()
    head2 = linklist_manege.delete_val(head1,val)
    #3.将链表转化为数组后打印出来
    print(linklist_become_tuple(head2))
