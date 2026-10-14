# 给你一个按非递减顺序排序的整数数组nums，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。
#
# 示例1：
# 输入：nums = [-4, -1, 0, 3, 10]
# 输出：[0, 1, 9, 16, 100]
# 解释：平方后，数组变为[16, 1, 0, 9, 100]排序后，数组变为[0, 1, 9, 16, 100]
#
# 示例2：
# 输入：nums = [-7, -3, 2, 3, 11]
# 输出：[4, 9, 9, 49, 121]

#想法1：直接对这些数组进行平方后再用方法sort进行排序——>时间复杂度O(nlogn)
# def sort_way(nums):
#     list_square = []
#     for times in range(len(nums)):
#         list_square.append(nums[times]**2)
#     list_square.sort()#O(n log n)
#     print(list_square)

#想法2：用二分法。1.找到正负数的交接处 2.一个指针左边，一个指针右边进行比较大小后插入
# def binary_way(nums):
#     square_list = []
#     def find_min():
#         left = 0
#         right = len(nums)
#         mid = (left+right)//2
#
#         while left<right:
#             if nums[mid]<0:
#                 left = mid + 1
#             else:
#                 right = mid
#             mid = (left+right)//2
#         return left
#     threshold_index = find_min()
#     left = threshold_index - 1
#     right = threshold_index
#     while right<len(nums) or left>=0:
#         if right<len(nums) and left>=0:
#             if nums[left] ** 2 < nums[right] ** 2:
#                 square_list.append(nums[left] ** 2)
#                 left -= 1
#             else:
#                 square_list.append(nums[right] ** 2)
#                 right += 1
#         elif right == len(nums) and left>=0:
#             square_list.append(nums[left] ** 2)
#             left -= 1
#         elif left<0 and right<len(nums):
#             square_list.append(nums[right] ** 2)
#             right += 1
#     return square_list

#方法3：从元素组的两端开始比较大小，从后往前填写平方进新建立的数组里面（所以这里新建数组的长度是固定的，和原来的数组一样长）
def bothEnds(nums):
    new_list = [0]*len(nums)#新建立一个长度为len(nums)的数组并且刚开始元素全部设置为0
    left = 0
    right = len(nums)-1
    new_end_pointer = len(nums)-1

    while left<right:
        if abs(nums[left]) < abs(nums[right]):#当左边指针所指元素的绝对值小于右指针所指元素的绝对值
            new_list[new_end_pointer] = nums[right]**2
            right -= 1#右指针想左移动
            new_end_pointer -= 1 #新列表的指针后移一步
        else:
            new_list[new_end_pointer] = nums[left]**2
            left += 1
            new_end_pointer -= 1
    return  new_list

if __name__ == "__main__":
    nums = [-4, -1, 0, 3, 10]

    # sort_way(nums)

    # print(binary_way(nums))

    print(bothEnds(nums))
