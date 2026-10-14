# 给定一个含有 n 个正整数的数组和一个正整数 target 。
# 找出该数组中满足其总和大于等于 target 的长度最小的  [numsl, numsl+1, ...,numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。

# 示例 1：
# 输入：target = 7, nums = [2,3,1,2,4,3]
# 输出：2
# 解释：子数组 [4,3] 是该条件下的长度最小的子数组。

# 示例 2：
# 输入：target = 4, nums = [1,4,4]
# 输出：1

# 示例 3：
# 输入：target = 11, nums = [1,1,1,1,1,1,1,1]
# 输出：0

#想法1：对数组进行排序，从后往前比较大小后一次往前相加——>不行❌️。因为要求连续。子数组 / subarray：原数组中连续的一段。子序列 / subsequence：原数组中不要求连续，只要保持相对顺序即可。
# def short_len(target,nums):
#     nums.sort()
#     end = len(nums)
#     head = end-1
#
#     while head >= 0:
#         sum = 0
#         for times in range(head,end):
#             sum += nums[times]
#         if sum>=target:
#             return end-head
#         head -= 1
#     return 0

#AI方法：滑动窗口——>用两个指针来指向一个区间，并用一个初始值为0的变量记录可以实现目标的连续长度。将该区间的值加起来如果大于target就将
# 左指针右移收缩尝试更短的能不能实现要求，如果不行就将右指针右移扩大范围，指导左右指针指向最后一个元素
def short_len(target,nums):
    left = 0
    total = 0#用于记录当前区域的总值
    ans = float('fin')# Python 中代表正无穷大的写法是 float('inf')

    for right in range(len(nums)):
        total += nums[right]
        while total>= target:
            ans = min(ans,right-left+1)#当前满足时，取当前窗口的长度和记录的最小长度做比较，取最小的那个进行保存
            #左指针尝试右移缩小区间，在通过while判断
            total -= nums[left]
            left += 1
    return 0 if ans == float('inf') else ans





if __name__ == "__main__":
    # target = 7
    # nums = [2, 3, 1, 2, 4,3]

    # target = 4
    # nums = [1, 4, 4]

    target = 11
    nums = [1, 1, 1, 1, 1, 1, 1, 1]

    print(short_len(target,nums))



