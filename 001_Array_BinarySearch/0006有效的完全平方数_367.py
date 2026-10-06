# 给你一个正整数num 。如果num是一个完全平方数，则返回true ，否则返回false 。
#
# 完全平方数是一个可以写成某个整数的平方的整数。换句话说，它可以写成某个整数和自身的乘积。不能使用任何内置的库函数，如sqrt 。
#
# 示例1：
# 输入：num = 16
# 输出：true
# 解释：返回true ，因为4 * 4 = 16且4是一个整数。
#
# 示例2：
# 输入：num = 14
# 输出：false
# 解释：返回false ，因为3.742 * 3.742 = 14但3.742不是一个整数。

#同样使用二分法
def Judgement(num):
    left = 1
    right = num+1

    if num == 1:
        return  True
    else:
        while left < right:
            mid = (left + right) // 2
            if mid ** 2 > num:
                right = mid
            elif mid**2==num:
                return True
            else:
                left = mid+1
        return False


if __name__ == "__main__":
    num = int(input("输入一个整数"))
    print(Judgement(num))