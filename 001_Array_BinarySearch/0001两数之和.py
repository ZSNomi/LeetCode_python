# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出和为目标值 target  的那 两个 整数，并返回它们的数组下标。
# 你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。
# 你可以按任意顺序返回答案。
#
# 示例1：
# 输入：nums = [2, 7, 11, 15], target = 9
# 输出：[0, 1]
# 解释：因为 nums[0] + nums[1] == 9 ，返回[0, 1] 。


#标签：数组、哈希查找
#适用场景：
#   暴力求解：一个动，一个不懂进行一一对比的时候
#   哈希查找：适用于（1）某样东西是不是存在（2）记录已经见过的东西（3）快速找到某个东西的位置


#方法1:暴力求解：时间复杂度O(n^2)
def pos_return(num, target):
    pos1 = 0
    pos2 = 1
    for i in range(pos1,len(num)):
        pos2 = i+1
        while pos2 < len(num) and num[i]+num[pos2]!=target:
            pos2 = pos2 + 1
        if pos2<len(num):
            return i,pos2
    return -1, -1

target = 10
num = [5, 11, 23, 54, 2, 8, 1, 24, 67, 35]
print(pos_return(num, target))
#思路：
# （1）：定义一个函数实现
# （2）：传参：传入数组（元组）、目标值
# （3）两重循环（双指针）：一重循环用于控制从哪个数开始遍历，另一重循环用于遍历数组
#     ①：为了控制边界，用for循环从下标0开始遍历，直至最后一位数（len(num)）
#     ②：当第二个指针指向最后一位数依旧没有找到时，需要将改指针回退，所以需要设置使指针回退的代码：pos2=i+1
#     ③:第二个指针用while遍历：条件是如果没有找到使得两个数相加等于目标值并且第二个指针要没有越过边界（len(num)），那么就不断地将第二指针后移一位（pos2 +=1）
#     ④：当跳出循环体后就需要判断到底是越位导致的还是找到了两个值的和为目标值；若是找到了目标值（pos2<len(num)）——没有越位那就是找到了想加为目标值的两个数，那么直接返回下标索引即可。若没有找到那么执行for的下一步循环
#     ⑤：可能存在数组里面没有两数相加等于目标值的，所以在for循环结束之后直接返回（-1，-1）用来保底。

#方法2：哈希查找：通过一个“键”（key），直接一步找到它对应的“值”（value）——>时间复杂度：O（n）
def dict_way(nums,target):
    """
    通过哈希查找来查找满足两个数之和为目标值的两个数的下标
    :param nums: 形参，表示要查找的数列
    :param target: 目标值
    :return: 返回两个数在数组nums中的下标
    """
    dict_num = {}  #
    for index,value in enumerate(nums):
        if target-value in dict_num:
            return dict_num[target-value],index
        else:
            dict_num[value] = index
    return -1,-1

target = 10
num = [5, 11, 23, 54, 2, 8, 1, 24, 67, 35]
print(dict_way(num,target))
# 思路：
# （1）：构造函数
# （2）：核心思想：通过查看target和当前元素的差值是否在字典中存在，如果没有存在那么就将该数作为字典的key，下标作为values存在字典中。
#     ①为什么这样是可以的？
#         a):target = 10,nums=[3,7,...],dict_num={}.
#         b):当targe-3=7，此时dict_num中没有，那么将该值与所在下标存储在字典中，此时dict_num{"3":0}
#         c):当num = 7时，target-7=3存在字典当中，且下标为0
#         d):所以返回的下标就是dict_num[target-num]（即7的补数3（key））的下标和当前该数的下标index


