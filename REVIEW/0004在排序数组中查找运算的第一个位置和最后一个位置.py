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

def star_end(nums,target):
    def left_indef(num_tar):
        left_pointer = 0
        right_pointer = len(nums)
        mid_pointer = (left_pointer+right_pointer)//2
        while left_pointer<right_pointer:
            if nums[mid_pointer]<num_tar:
                left_pointer = mid_pointer+1
            else:
                right_pointer = mid_pointer
            mid_pointer = (left_pointer+right_pointer)//2
        return left_pointer
    left_index = left_indef(target)
    if left_index==len(nums) or nums[left_index] !=target:
        return (-1,-1)
    right_index = left_indef(target+1)-1

    return (left_index,right_index)

if __name__ == "__main__":
    # nums = [5, 7, 7, 8, 8, 10]
    # target = 8

    # nums = [5, 7, 7, 8, 8, 10]
    # target = 6

    nums = []
    target = 0

    print(star_end(nums,target))