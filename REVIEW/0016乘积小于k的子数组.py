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

def mul_litter(nums,k):
    left = 0
    mul_sum = 1
    num = 0

    if k<1:
        return 0

    for right in range(len(nums)):
        mul_sum *= nums[right]

        if mul_sum<k:
            num += right-left+1

        while mul_sum>=k:
            mul_sum /= nums[left]
            left += 1
            if mul_sum<k:
                num += right-left+1
    return num





if __name__ == "__main__":
    # nums = [10, 5, 2, 6]
    # k = 100
    # 输出：8

    nums = [1, 2, 3]
    k = 0
    # 输出：0

    print(mul_litter(nums,k))

# 思路：
# 1.确定使用滑动窗口
# 2.何时扩大窗口？何时缩小窗口？
#     （1）扩大窗口：只要窗口内的乘积小于k就扩大窗口
#     （2）缩小窗口：只要窗口内的乘积大于等于k就扩大窗口


# num += right - left + 1 的核心含义是：
# 固定右端点 right 时，以 right 结尾、且乘积严格小于 k 的连续子数组个数，正好等于当前窗口长度 right - left + 1。
# [left, right] 这个窗口内所有元素的乘积 < k
# 当右端点固定在 right 时，所有以 right 结尾的子数组，左端点可以是：left, left + 1, left + 2, ..., right
# 一共有：right - left + 1个。
# 这些子数组分别是：
#     [left, right]
#     [left + 1, right]
#     [left + 2, right]
#     ...
#     [right, right]
# 因为它们都是当前窗口 [left, right] 的子数组，而当前窗口乘积已经小于 k，所以这些子数组的乘积也都小于 k。

