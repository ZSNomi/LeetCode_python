# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
#
# 输入：head = [1,2,3,4,5], n = 2
# 输出：[1,2,3,5]
#
# 输入：head = [1], n = 1
# 输出：[]
#
# 输入：head = [1,2], n = 1
# 输出：[1]

# class Lnode:
#     def __init__(self,val=0,next=None):
#         self.val = val
#         self.next = next
#
# class DeleteCountdownN:
#     #计算链表的长度方法1：直接用普通函数
#     def lenth(self,linklist):
#         count,cur = 0,linklist
#
#         while cur:
#             count += 1
#             cur = cur.next
#
#         return count
#
#
#     def DelCountdownN(self,linklist,N):
#         #建立一个默认值为0的头结点
#         head = Lnode()
#         head.next = linklist
#
#         #得到链表的长度
#         lenth_linklist = self.lenth(linklist)
#
#         #删除倒数第N个节点即删除正数lenth(linklist)+1-N的个节点
#         #找到要删除的正数的lenth(linklist)+1-N个节点的前一个节点
#         pre = head
#         for _ in range(lenth_linklist-N):
#             pre = pre.next
#
#         #然pre指向要删除的节点的下一个节点
#         pre.next = pre.next.next
#
#         return head.next



# class Lnode:
#     def __init__(self,val=0,next=None):
#         self.val = val
#         self.next = next
#
#     def __len__(self):
#         size,cur = 0,self
#
#         while cur is not None:
#             size += 1
#             cur = cur.next
#
#         return size
#
# class DeleteCountdownN:
#     def DelCountdownN(self,linklist,N):
#         #建立一个默认值为0的头结点
#         head = Lnode()
#         head.next = linklist
#
#         #得到链表的长度
#         lenth_linklist = len(linklist)
#
#         #删除倒数第N个节点即删除正数lenth(linklist)+1-N的个节点
#         #找到要删除的正数的lenth(linklist)+1-N个节点的前一个节点
#         pre = head
#         for _ in range(lenth_linklist-N):
#             pre = pre.next
#
#         #然pre指向要删除的节点的下一个节点
#         pre.next = pre.next.next
#
#         return head.next

#使用快慢指针
class Lnode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

class DeleteCountdownN:
    def DelCountdownN(self,linklist,N):
        if linklist is None or N<=0:
            return linklist

        #建立一个默认值为0的头结点
        head = Lnode()
        head.next = linklist

        fast = slow =head
        #让快指针前进N步
        for _ in range(N):
            fast = fast.next
            if fast is None: #如果还没有走到N步就为None直接返回原链表
                return linklist

        #让快慢指针同步前进直到fast.next指针为None,fast指针此时指向即将删除的节点的前一个节点
        while fast.next is not None:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
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
    # head = [1, 2, 3, 4, 5]
    # n = 2
    # 输出：[1,2,3,5]

    # head = [1]
    # n = 1
    # 输出：[]

    head = [1, 2]
    n = 1
    # 输出：[1]

    #将数组转化为链表
    linklist = TupelBecomeLinklist(head)
    #删除指定节点
    #实例化对象
    delete_manage = DeleteCountdownN()
    linklist = delete_manage.DelCountdownN(linklist,n)
    #将链表转化为数组进行打印输出
    print(LinklistBecomeTuple(linklist))
