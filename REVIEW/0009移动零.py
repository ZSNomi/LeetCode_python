# 给定一个数组nums，编写一个函数将所有0移动到数组的末尾，同时保持非零元素的相对顺序。请注意 ，必须在不复制数组的情况下原地对数组进行操作。
#
# 示例1:
# 输入: nums = [0, 1, 0, 3, 12]
# 输出: [1, 3, 12, 0, 0]
#
# 示例2:
# 输入: nums = [0]
# 输出: [0]

def move_zero(nums):
    left = 0

    for right in range(1,len(nums)):
        if nums[left]==0 and nums[right]!=0:
            nums[left],nums[right] = nums[right],nums[left]
            left += 1
        if nums[left] !=0:
            left += 1
    return nums



if __name__ == "__main__":


    nums = [2,0,1,2,0,12,9,2,0,0]
    print(move_zero(nums))