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

# #法1：不是最优解：
# #定义链表结构
# class Lnode:
#     def __init__(self,val=0,next=None):
#         self.val = val
#         self.next = next
#
#
# class ReveableLinklist:
#     def reverse(self,linklist):
#         #将链表转化为数组
#         new_tuple = linklist_become_tuple(linklist)
#
#         #对数组进行转化
#         for i in range(len(new_tuple)//2):
#             new_tuple[i],new_tuple[len(new_tuple)-1-i] = new_tuple[len(new_tuple)-1-i], new_tuple[i]
#
#         #将翻转后的数组转化为链表
#         new_linklist = tuple_become_linklist(new_tuple)
#
#         return new_linklist
#
#
# #辅助函数：数组转化为链表
# def tuple_become_linklist(tuple_head):
#     if not tuple_head:
#         return
#
#     #建立一个头结点：
#     cur_head = Lnode()
#
#     #建立一个指针并让指针指向头结点
#     cur = cur_head
#
#     for val in tuple_head:
#         new_node = Lnode(val)
#         cur.next = new_node
#         cur = cur.next
#
#     return cur_head.next
#
# #辅助函数：链表转化为数组
# def linklist_become_tuple(linklist):
#     #建立一个空的头结点
#     top = Lnode()
#
#     top.next = linklist
#
#     cur = top
#
#     new_tuple = []
#
#     while cur.next:
#         new_tuple.append(cur.next.val)
#         cur = cur.next
#
#     return new_tuple
#
#
# if __name__ == "__main__":
#
#     head = [1, 2, 3, 4, 5]
#     # 输出：[5,4,3,2,1]
#
#     # head = [1, 2]
#     # 输出：[2,1]
#
#     # head = []
#     # 输出：[]
#
#     #将列表转化为链表
#     lnode = tuple_become_linklist(head)
#
#     #实例化反转方法
#     reverse = ReveableLinklist()
#     new_linklist = reverse.reverse(lnode)
#
#     #将的得到的反转后的链表转化为数组，方便打印输出
#     new_tuple = linklist_become_tuple(new_linklist)
#     print(new_tuple)




#法2：最优解。空间复杂度为：O(1)
class Lnode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

class Reverse:
    def reverse(self,link_list):
        pre = None  #用来记录上一个节点
        cur = link_list

        while cur:
            next_node = cur.next #保存下一个节点
            cur.next = pre #翻转当前节点
            pre = cur
            cur = next_node

        return pre

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
    # 实例化 Solution 类
    solution = Reverse()

    # 测试用例
    test_cases = [
        [1, 2, 3, 4, 5],  # 示例1
        [1, 2],  # 示例2
        []  # 示例3
    ]

    for arr in test_cases:
        # 1. 将输入列表构建为链表
        head = tuple_become_linklist(arr)

        # 2. 调用反转方法
        new_head = solution.reverse(head)

        # 3. 将反转后的链表转换回列表用于输出
        result_arr = linklist_become_tuple(new_head)

        # 4. 打印结果
        print(f"输入: {arr}")
        print(f"输出: {result_arr}")
        print("-" * 20)