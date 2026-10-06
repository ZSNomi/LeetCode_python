# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出和为目标值 target  的那 两个 整数，并返回它们的数组下标。
# 你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。
# 你可以按任意顺序返回答案。
#
# 示例1：
# 输入：nums = [2, 7, 11, 15], target = 9
# 输出：[0, 1]
# 解释：因为 nums[0] + nums[1] == 9 ，返回[0, 1] 。


def FindIndex():
    nums = [2, 7, 11, 15]
    target = int(input("输入目标值："))

    #初始化一个字典，用于保存数字（key）和对应的下标（value）
    dict_former = {}

    #for循环遍历dict_former查找当前数的与target的补数
    for (index,value) in enumerate(nums):
        if target-value in dict_former.keys():
            return [dict_former[target-value],index]
        dict_former[value] = index
    return [-1,-1]

if __name__ == "__main__":
    list = FindIndex()
    print(list)


