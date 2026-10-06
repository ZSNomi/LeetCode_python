# 给你一个非负整数x ，计算并返回x的算术平方根 。
# 由于返回类型是整数，结果只保留整数部分 ，小数部分将被舍去 。
# 注意：不允许使用任何内置指数函数和算符，例如pow(x, 0.5)或者x ** 0.5 。

# 示例1：
# 输入：x = 4
# 输出：2

# 示例2：
# 输入：x = 8
# 输出：2
# 解释：8的算术平方根是2.82842..., 由于返回类型是整数，小数部分将被舍去


#自己的想法：但是在建数组那里内容开销极大
# def cal_square(x):
#     def left_num(x,nums):
#         left_pointer = 0
#         right_pointer = len(nums)
#         mid_pointer = (left_pointer + right_pointer) // 2
#
#         while left_pointer < right_pointer:
#             if nums[mid_pointer]* > x:
#                 right_pointer = mid_pointer
#             else:
#                 left_pointer = mid_pointer+1
#             mid_pointer = (left_pointer + right_pointer) // 2
#         return nums[mid_pointer]-1
#
#
#     if x ==1 or x==2:
#         return 1
#     elif x==0:
#         return 0
#     elif x<0:
#         return -1
#     else:
#         nums = []
#         for i in range(1, x):
#             nums.append(i)
#         return left_num(x,nums)

#方法2：不用构建数组，内存不会存在任何的问题（空间复杂度为O(1)），时间复杂度为O(logn)
def cal_square(x):
    if x<0:
        return -1
    if x ==0:
        return 0
    else:
        left = 1
        right = x+1
        while left<right:
            mid = (left+right)//2
            if mid**2>x:
                right = mid
            else:
                left = mid +1
        return left-1

if __name__ == "__main__":
    x = int(input("输入整数X："))
    print(cal_square(x))






