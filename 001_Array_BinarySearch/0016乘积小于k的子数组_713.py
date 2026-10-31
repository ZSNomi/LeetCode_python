# 给定一个整数数组 nums 和一个整数 k。
# 请你返回 子数组 内所有元素的 乘积严格小于 k 的连续子数组的数目
#
# 示例 1：
# 输入：nums = [10,5,2,6], k = 100
# 输出：8
# 解释：8 个乘积小于 100 的子数组分别为：[10]、[5]、[2]、[6]、[10,5]、[5,2]、[2,6]、[5,2,6]。
# 需要注意的是 [10,5,2] 并不是乘积小于 100 的子数组。
#
# 示例 2：
# 输入：nums = [1,2,3], k = 0
# 输出：0



#法1：
# def multiplication(nums,k):
#     left = 0
#     mult = nums[0]
#     toatl_size = 0
#
#     for right in range(1,len(nums)):
#         mult *= nums[right]
#         if mult<k:
#             toatl_size += 1
#
#         #窗口乘积大于等于k
#         while mult>=k or right==len(nums)-1:
#             if left<right:
#                 if nums[left] < k:
#                     toatl_size += 1
#                 mult /= nums[left]
#                 if mult < k:
#                     toatl_size += 1
#                 left += 1
#             else:
#                 break
#     return toatl_size

#存在问题：
# 1.右指针起步不对：for right in range(1, len(nums)) 导致你直接跳过了第一个元素，如果数组只有一个元素，直接错。
# 2.while 的条件完全混乱：你把 right == len(nums)-1 放进收缩条件里


#滑动窗口真正的使用方法：
def multiplication(nums,k):
    left = 0
    multi_result = 1
    num = 0

    if k<1:
        return 0

    for right in range(len(nums)):
        multi_result *= nums[right]

        if multi_result<k:
            num += right-left+1

        #缩小窗口
        while multi_result>=k:
            multi_result /= nums[left]
            left += 1
            if multi_result < k:
                num += right - left + 1
    return num


if __name__ == "__main__":
    # nums = [10, 5, 2, 6]
    # k = 100
    # 输出：8

    # nums = [1, 2, 3]
    # k = 0
    # 输出：0

    nums = [1, 2, 3,4,5,6]
    k = 100

    print(multiplication(nums,k))



