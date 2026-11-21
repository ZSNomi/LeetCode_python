# 给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。

# 示例1：
# 输入：head = [1,2,3,4,5], left = 2, right = 4
# 输出：[1,4,3,2,5]
#
# 示例2：
# 输入：head = [5], left = 1, right = 1
# 输出：[5]


#定义链表结构
class Lnode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

#定义反转链表的方法
class Reverse:
    def reverse(self,linklist,left,right):
        #建立一个空节点
        top = Lnode()
        top.next = linklist

        #循环找到left的前一个节点：
        pre = top
        for _ in range(left-1):
            pre = pre.next

        #需要保存要left所指节点（pre.next）:该节点反转后会是最后一个节点，需要将其的next指向right的下一个节点
        end_node = pre.next

        #开始翻转链表：一共要反转right-left次
        pre_pointer = pre.next
        cur = pre_pointer.next
        for _ in range(right-left):
            next_node = cur.next #保存当前节点的下一个节点
            cur.next = pre_pointer #翻转当前节点
            pre_pointer = cur
            cur = next_node
        #链接已经断掉的链表
        pre.next = pre_pointer
        end_node.next = cur

        return top.next





#辅助函数1：数组—>链表
def TupelBecomeLinklist(tuple_list):
    #建立一个数值为0的头结点
    head = Lnode(0)

    cur = head

    for val in tuple_list:
        new_node = Lnode(val)
        cur.next = new_node
        cur = cur.next
    return head.next

#辅助函数2：链表->数组
def LinklistBecomeTuple(linklist):
    #建立一个新的数组
    new_tuple = []
    cur = linklist

    while cur:
        new_tuple.append(cur.val)
        cur = cur.next
    return new_tuple

if __name__ == "__main__":

    # head = [1, 2, 3, 4, 5]
    # left = 2
    # right = 4
    # 输出：[1,4,3,2,5]

    head = [5]
    left = 1
    right = 1
    # 输出：[5]


    #实例化对象
    reverse = Reverse()

    #1.将数组转化为链表
    new_head = TupelBecomeLinklist(head)
    #2.进行翻转得到新的链表
    new_head = reverse.reverse(new_head,left,right)
    #3.将链表转化为数组后打印输出
    print(LinklistBecomeTuple(new_head))