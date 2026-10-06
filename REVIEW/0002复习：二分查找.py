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


def find_index(nums,target):
    left_pointer = 0
    right_pointer = len(nums)-1

    while left_pointer<=right_pointer:
        mid_pointer = (left_pointer + right_pointer) // 2
        if nums[mid_pointer] == target:
            return mid_pointer
        elif nums[mid_pointer]<target:
            left_pointer = mid_pointer+1
        elif nums[mid_pointer]>target:
            right_pointer = mid_pointer-1
    return -1


if __name__ == "__main__":
    nums = [-1, 0, 3, 5, 9, 12]
    target_one = 9
    index_exsit = find_index(nums,target_one)
    print(index_exsit)

    nums = [-1, 0, 3, 5, 9, 12]
    target = 2
    index_noexsit = find_index(nums, target)
    print(index_noexsit)