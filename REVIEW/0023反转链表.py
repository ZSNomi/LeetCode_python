# 给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
#
# 示例1：
# 输入：head = [1,2,3,4,5]
# 输出：[5,4,3,2,1]
#
# 示例2：
# 输入：head = [1,2]
# 输出：[2,1]
#
# 示例3：
# 输入：head = []
# 输出：[]

#定义链表结构体：
class Lnode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

#定义方法：
class Reverse:
    def reverse(self,head):
        pre = None
        cur = head

        while cur:
            next_node = cur.next #保存下一个节点
            cur.next = pre #反转当前节点
            pre = cur
            cur = next_node

        return pre

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

    case_text = [
        [1, 2, 3, 4, 5],
        # 输出：[5,4,3,2,1]

        [1, 2],
        # 输出：[2,1]

        []
        # 输出：[]
    ]

    manage_reverse = Reverse()
    for head in case_text:
        #数组转化为链表：
        linklist = TupelBecomeLinklist(head)
        #翻转链表
        new_linklist = manage_reverse.reverse(linklist)
        #将链表转化为数组进行打印
        print(LinklistBecomeTuple(new_linklist))


