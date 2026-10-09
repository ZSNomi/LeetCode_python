# 给你一个非严格递增排列的数组nums ，请你原地删除重复出现的元素，使每个元素只出现一次 ，返回删除后数组的新长度。
# 元素的相对顺序应该保持一致 。然后返回nums中唯一元素的个数。考虑nums的唯一元素的数量为k。去重后，返回唯一元素的数量k。
# nums的前k个元素应包含排序后的唯一数字。下标k - 1之后的剩余元素可以忽略
#
# 判题标准:
# 系统会用下面的代码来测试你的题解:
#
# nums = [...]; // 输入数组
# int[] expectedNums = [...]; // 长度正确的期望答案
#
# int k = removeDuplicates(nums); // 调用
#
# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }
# 如果所有断言都通过，那么您的题解将被通过。
#
# 示例1：
# 输入：nums = [1, 1, 2]
# 输出：2, nums = [1, 2, _]
# 解释：函数应该返回新的长度2 ，并且原数组nums的前两个元素被修改为1, 2 。不需要考虑数组中超出新长度后面的元素。
#
# 示例2：
# 输入：nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# 输出：5, nums = [0, 1, 2, 3, 4, _, _, _, _, _]
# 解释：函数应该返回新的长度5 ， 并且原数组nums的前五个元素被修改为0, 1, 2, 3, 4 。不需要考虑数组中超出新长度后面的元素。

def removeDuplicates(nums):
    slow = 0
    for fast in range(1,len(nums)):
        if nums[slow] != nums[fast]:
            slow += 1
            nums[slow] =nums[fast]
    return slow+1

if __name__ == "__main__":
    nums = [1, 1, 2]

    # nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

    k = removeDuplicates(nums)
    print(f"{k},{nums}")

#思路：fast指针用来找和slow指针不相等的元素，slow指针用来指向当前比较元素。当找了一个和当前元素不相等的元素，那么就需要将这个元素插入到下一个位置。即在插入钱先将slow指针后移一位
