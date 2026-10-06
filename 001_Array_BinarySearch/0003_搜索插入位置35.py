# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
# 请必须使用时间复杂度为O(logn) 的算法。

# 示例1:
# 输入: nums = [1, 3, 5, 6], target = 5
# 输出: 2

# 示例2:
# 输入: nums = [1, 3, 5, 6], target = 2
# 输出: 1

# 示例3:
# 输入: nums = [1, 3, 5, 6], target = 7
# 输出: 4

def index_insert(nums,targetr):
    letf_pionter = 0
    right_pointer = len(nums)-1
    mid_pointer = (letf_pionter + right_pointer) // 2

    while letf_pionter<=right_pointer:
        if nums[mid_pointer]==targetr:
            return mid_pointer
        elif nums[mid_pointer]<targetr:
            letf_pionter = mid_pointer+1
        elif nums[mid_pointer]>targetr:
            right_pointer = mid_pointer-1
        mid_pointer = (letf_pionter + right_pointer) // 2
    if nums[mid_pointer]>targetr:
        return mid_pointer
    else:
        return mid_pointer+1


if __name__ == "__main__":
    # nums = [1, 3, 5, 6]
    # target = 5

    # nums = [1, 3, 5, 6]
    # target = 2

    nums = [1, 3, 5, 6]
    target = 7
    print(index_insert(nums,target))