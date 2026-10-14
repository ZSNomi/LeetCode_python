# 给你一个按非递减顺序排序的整数数组nums，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。
#
# 示例1：
# 输入：nums = [-4, -1, 0, 3, 10]
# 输出：[0, 1, 9, 16, 100]
# 解释：平方后，数组变为[16, 1, 0, 9, 100]排序后，数组变为[0, 1, 9, 16, 100]
#
# 示例2：
# 输入：nums = [-7, -3, 2, 3, 11]
# 输出：[4, 9, 9, 49, 121]

def square_array(nums):
    left = 0
    right = len(nums)-1
    square_nums = [0]*len(nums)
    square_nums_tailor = len(nums)-1

    while left<=right:
        if nums[left]**2<nums[right]**2:
            square_nums[square_nums_tailor] = nums[right]**2
            right -= 1
        else:
            square_nums[square_nums_tailor] = nums[left] ** 2
            left += 1
        square_nums_tailor -= 1
    return square_nums

if __name__ == "__main__":
    # nums = [-4, -1, 0, 3, 10]
    # 输出：[0, 1, 9, 16, 100]

    nums = [-7, -3, 2, 3, 11]
    # 输出：[4, 9, 9, 49, 121]

    print(square_array(nums))