# 给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。

# 输入：head = [1,2,3,4]
# 输出：[2,1,4,3]
#
# 输入：head = []
# 输出：[]
#
# 输入：head = [1]
# 输出：[1]

class Lnode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

#写法1：
# class ChangeLnode:
#     def changeLnode(self,linklist):
#         #当为空节点或者只有一个节点的时候
#         if linklist==None or linklist.next==None:
#             return linklist
#
#
#         #建立一个头结点
#         head = Lnode()
#         head.next = linklist
#
#         pre = head #建立一个前指针：永远指向即将翻转节点的前一个节点
#         rev_pre = pre.next #建立一个马上翻转节点
#         cur = rev_pre.next
#
#         while cur:
#             #翻转节点并连接断掉的节点
#             next_node = cur.next #保存下一个节点
#             cur.next = rev_pre
#             rev_pre.next = next_node
#             pre.next = cur
#             #更新指针的位置
#             pre = rev_pre
#             rev_pre = next_node
#             if rev_pre is None or rev_pre.next is None:
#                 break
#             else:
#                 cur = rev_pre.next
#         #while cur：写的并不好，有以下原因
#         #1.在if中判断的时候是“从左到右”进行判断，如果rev_pre.next is None在前rev_pre is None在后（即if rev_pre.next is None or rev_pre is None）
#             #的写法一定会报错。当如果是rev_pre本来就是None时，在rev_pre.next就会报错，所以这里写的时候必须要考虑这个问题，很麻烦，很容易错。
#         #2.如果能够将判断条件全部都能够通过while的话最好不要在while内部用if判断
#
#         return head.next


# 写法2：
class ChangeLnode:
    def changeLnode(self,linklist):
        #当为空节点或者只有一个节点的时候
        if linklist==None or linklist.next==None:
            return linklist


        #建立一个头结点
        head = Lnode()
        head.next = linklist

        pre = head

        while pre.next and pre.next.next:
            first, second = pre.next, pre.next.next
            first.next = second.next
            second.next = first
            pre.next = second
            pre = first

        return head.next




#辅助函数1：数组—>链表
def TupelBecomeLinklist(tuple_list):
    if not tuple_list:
        return None

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
    text_data = [
        [1, 2, 3, 4],
        # 输出：[2,1,4,3]

        [],
        # 输出：[]

        [1],
        # 输出：[1]

        [1,2,3,4,5]
        #输出：[2, 1, 4, 3, 5]
    ]

    #实例化对象
    changenode = ChangeLnode()

    for head in text_data:
        #将数组转化为链表
        linklist = TupelBecomeLinklist(head)
        #翻转链表
        new_linklist = changenode.changeLnode(linklist)
        #将链表转化为数组并打印输出
        print(LinklistBecomeTuple(new_linklist))



