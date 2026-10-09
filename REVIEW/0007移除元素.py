# 给你一个数组nums和一个值val，你需要原地移除所有数值等于val的元素。元素的顺序可能发生改变。然后返回nums中与val不同的元素的数量。
# 假设num中不等于val的元素数量为k，要通过此题，您需要执行以下操作：更改nums数组，使nums的前k个元素包含不等于val的元素。nums的其余元素和nums的大小并不重要。返回k。
# 用户评测：评测机将使用以下代码测试您的解决方案：
# int[]nums = [...]; // 输入数组
# int val = ...; // 要移除的值
# int[] expectedNums = [...]; // 长度正确的预期答案。它以不等于val的值排序。
#
# int k = removeElement(nums, val); // 调用你的实现
#
# assert k == expectedNums.length;
# sort(nums, 0, k); // 排序nums的前k个元素
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }
# 如果所有的断言都通过，你的解决方案将会通过。
#
# 示例1：
# 输入：nums = [3, 2, 2, 3], val = 3
# 输出：2, nums = [2, 2, _, _]
# 解释：你的函数应该返回k = 2, 并且nums中的前两个元素均为2。你在返回的k个元素之外留下了什么并不重要（因此它们并不计入评测）。
#
# 示例2：
# 输入：nums = [0, 1, 2, 2, 3, 0, 4, 2], val = 2
# 输出：5, nums = [0, 1, 4, 0, 3, _, _, _]
# 解释：你的函数应该返回k = 5，并且nums中的前五个元素为0, 0, 1, 3, 4。
# 注意这五个元素可以任意顺序返回。
# 你在返回的k个元素之外留下了什么并不重要（因此它们并不计入评测）。

def removeElement(nums, val):
    slow  = 0
    for fast in range(1,len(nums)):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1
    return slow

if __name__ == "__main__":
    # nums = [3, 2, 2, 3]
    # val = 3

    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    k = removeElement(nums, val)
    print(f"{k},{nums}")

#思想：slow指针只是用来记录当前要填入不是val值的位置，而fast指针用来寻找不是val值