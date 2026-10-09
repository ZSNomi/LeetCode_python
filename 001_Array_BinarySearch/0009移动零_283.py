# 给定一个数组nums，编写一个函数将所有0移动到数组的末尾，同时保持非零元素的相对顺序。请注意 ，必须在不复制数组的情况下原地对数组进行操作。
#
# 示例1:
# 输入: nums = [0, 1, 0, 3, 12]
# 输出: [1, 3, 12, 0, 0]
#
# 示例2:
# 输入: nums = [0]
# 输出: [0]

#自己的写法：快慢指针
# def move_zero(nums):
#     slow_pointer = 0
#
#     for fast_pointer in range(1,len(nums)):
#         if nums[slow_pointer]==0 and nums[fast_pointer]!=0:
#             nums[slow_pointer] = nums[fast_pointer]
#             nums[fast_pointer] = 0
#             slow_pointer += 1
#         elif nums[slow_pointer]!=0:
#             slow_pointer +=1
#     print(nums)

#AI写法：更简洁
def move_zero(nums):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]#交换两个元素值 的常用写法
            # 它的意思是：
            # 1.先计算右边nums[fast]和nums[slow]的值；
            # 2.然后把nums[fast]的值赋给nums[slow]；
            # 3.把nums[slow]原来的值赋给nums[fast]。
            # 也就是把nums[slow]和nums[fast]两个位置的值互换。

            # 为什么这样可以：
            # slow 是“下一个非零元素要放的位置”，fast 负责找非零元素；找到就交换，把 0 赶到后面，slow 前移；找不到就继续走。这样非零元素按原顺序排在前面，0 自然被挤到后面。
            slow += 1
    # 原地修改完成，不需要 print，直接返回即可

if __name__ == "__main__":
    # nums = [0, 1, 0, 3, 12]

    # nums = [0]

    nums = [2,0,1,2,0,12,9,2,0,0]
    move_zero(nums)