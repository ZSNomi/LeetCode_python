# 给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。

# 示例1：
# 输入：head = [1,2,3,4,5], left = 2, right = 4
# 输出：[1,4,3,2,5]
#
# 示例2：
# 输入：head = [5], left = 1, right = 1
# 输出：[5]


#自己的想法
class Lnode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

class Reverse:
    def reverse(self,linklist,left,right):
        #建立一个值为0的头结点
        head = Lnode()
        head.next = linklist

        pre = head

        #先找到left的前一个节点：
        for _ in range(left-1):
           pre = pre.next

        #进行翻转right-left次:
        reverse_pre = pre.next
        cur = reverse_pre.next
        finally_end_node = pre.next
        for _ in range(right-left):
            next_node = cur.next #保存下一个节点
            cur.next = reverse_pre #翻转当前节点
            reverse_pre = cur
            cur = next_node

        #链接断链：
        pre.next = reverse_pre
        finally_end_node.next = cur

        return head.next



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

    #数组转化为链表
    new_list = TupelBecomeLinklist(head)
    #翻转链表：
    reversr_manage = Reverse()
    linklist = reversr_manage.reverse(new_list,left,right)
    #链表转化为数组打印输出
    print(LinklistBecomeTuple(linklist))