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

#1：考虑什么情况应该扩大窗口，什么时候缩小窗口：当不满足条件的时候就需要扩大窗口来增加总值，满足条件后就缩小窗口来求最小长度
def short_list(nums,target):
    left = 0
    min_lenth = float('inf')
    total = 0

    for right in range(len(nums)):
        total += nums[right]
        while total>=target and left<= right:#满足条件了执行."left<= right"是用于防止出现左指针到右指针的右边
            min_lenth = min(min_lenth,right-left+1)#满足条件后不断将左指针向右移来缩小窗口（求最小长度）
            total -= nums[left]
            left += 1

    return min_lenth if min_lenth != float('inf') else 0



if __name__ == "__main__":
    # target = 7
    # nums = [2, 3, 1, 2, 4, 3]
    # 输出：2

    target = 4
    nums = [1, 4, 4]
    # 输出：1

    target = 11
    nums = [1, 1, 1, 1, 1, 1, 1, 1]
    # 输出：0

    print(short_list(nums,target))

