# 给你一个按照非递减顺序排列的整数数组nums，和一个目标值target。请你找出给定目标值在数组中的开始位置和结束位置。
# 如果数组中不存在目标值target，返回[-1, -1]。你必须设计并实现时间复杂度为O(logn) 的算法解决此问题。
#
# 示例1：
# 输入：nums = [5, 7, 7, 8, 8, 10], target = 8
# 输出：[3, 4]
#
# 示例2：
# 输入：nums = [5, 7, 7, 8, 8, 10], target = 6
# 输出：[-1, -1]


# 示例3：
# 输入：nums = [], target = 0
# 输出：[-1, -1]

#自己的想法：没有满足时间复杂度为O(logn)
# def find_index(nums,target):
#     left_pointer = 0
#     right_pointer = len(nums)-1
#     mid_pointer = (left_pointer+right_pointer)//2
#     list = []
#     if right_pointer == -1:
#         return [-1,-1]
#     else:
#         while left_pointer<=right_pointer:
#             mid_pointer = (left_pointer + right_pointer) // 2
#             if nums[mid_pointer] == target:
#                 list.append(mid_pointer)#保存当前匹配值的下标
#                 nums.remove(target)#删除第一个匹配的值
#                 list.sort()#对下标进行排序
#             elif nums[mid_pointer] < target:
#                 left_pointer = mid_pointer+1
#             elif nums[mid_pointer] > target:
#                 right_pointer = mid_pointer-1
#         if len(list) == 0:
#             return [-1,-1]
#         else:
#             return [list[0],list[len(list)-1]]


#二分查找：满足时间复杂度为O(logn)
def find_index(nums,target):
    #构造一个找左边界的方法：
    def find_left(target_new):
        left_pointer = 0
        right_point = len(nums)

        while left_pointer<right_point:
            mid_pointer = (left_pointer + right_point) // 2
            if nums[mid_pointer] < target_new:
                left_pointer = mid_pointer + 1
            else:
                right_point = mid_pointer
        return left_pointer

    #寻找左边界
    leff_index = find_left(target)

    #边界超出的情况以及没有找打相应元素
    if leff_index==len(nums) or nums[leff_index] !=target:
        return [-1,-1]

    #寻找右边界
    right_index = find_left(target+1)-1

    return [leff_index,right_index]





if __name__ == "__main__":
    nums = [5, 7, 7, 8, 8, 10]
    target = 8

    # nums = [5, 7, 7, 8, 8, 10]
    # target = 6

    # nums = []
    # target = 0
    print(find_index(nums,target))










