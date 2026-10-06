# 给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果 target 存在返回下标，否则返回 -1。
# 你必须编写一个具有 O(log n) 时间复杂度的算法。
#
# 示例 1:
# 输入: nums = [-1,0,3,5,9,12], target = 9
# 输出: 4
# 解释: 9 出现在 nums 中并且下标为 4
#
# 示例 2:
# 输入: nums = [-1,0,3,5,9,12], target = 2
# 输出: -1
# 解释: 2 不存在 nums 中因此返回 -1

def find_target(nums,target):
    pos_left = 0
    pos_right = len(nums)-1
    while pos_right<=pos_left:#边界问题
        pos_mid = (pos_left + pos_right) // 2
        if target<nums[pos_mid]:
            pos_right = pos_mid-1
        elif target>nums[pos_mid]:
            pos_left = pos_mid+1
        else:
            return pos_mid
    else:
        return -1

nums = [-1,0,3,5,9,12]
target = 6
print(find_target(nums,target))

#标签：二分法
#适用场景：数组有序
#总结：
# 1：容易出错的地方
#     （1）while的判定判定条件，容易漏掉边界
#     （2）如果当中间指针指的不是target值的时候，那么下一步的左（右）指针不用考虑该位置，直接向右（左）移动一位。

