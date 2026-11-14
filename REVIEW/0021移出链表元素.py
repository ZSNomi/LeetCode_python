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

#定义节点的结构体
class LNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

#定义类：包含删除方法
class OperLink:
    def delete_node(self,linklist:LNode,val:int):
        #建立一个初始值为0的头节点，用于指向链表首节点
        top = LNode(0)
        top.next = linklist

        #建立cur指针用于遍历链表
        cur = top

        while cur.next:
            if cur.next.val==val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return top.next

#辅助函数：将数组转变为链表：
def tuple_become_linklist(head):
    #数组为空
    if not head:
        return None

    #建立一个值为默认值0的头结点
    top = LNode()

    #建立一个指向头结点的指针
    cursor = top

    #建立节点、为节点赋值、链接链表
    for val in head:
        node = LNode(val) #从元组中取出值并赋值给节点cur
        cursor.next = node
        cursor = cursor.next

    return top.next

#辅助函数：将链表转化为数组（用于最后结果的打印）
def linklist_become_tuple(linklist:LNode):
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
    head = [1, 2, 6, 3, 4, 5, 6]
    val = 6
    # 输出：[1,2,3,4,5]

    # head = []
    # val = 1
    # 输出：[]

    # head = [7, 7, 7, 7]
    # val = 7
    # 输出：[]

    opera = OperLink()
    #将列表转化为链表
    linklist = tuple_become_linklist(head)

    # 进行删除操作
    linklist = opera.delete_node(linklist, val)
    # 将链表转化为列表后再进行打印输出
    print(linklist_become_tuple(linklist))


