# 给你一个非负整数x ，计算并返回x的算术平方根 。
# 由于返回类型是整数，结果只保留整数部分 ，小数部分将被舍去 。
# 注意：不允许使用任何内置指数函数和算符，例如pow(x, 0.5)或者x ** 0.5 。

# 示例1：
# 输入：x = 4
# 输出：2

# 示例2：
# 输入：x = 8
# 输出：2
# 解释：8的算术平方根是2.82842..., 由于返回类型是整数，小数部分将被舍去

def squareRoot(target):
    if target<0:
        return -1
    else:
        left_pointer = 0
        right_pointer = target+1
        mid_pointer = (left_pointer+right_pointer)

        while left_pointer<right_pointer:
            if mid_pointer**2==target:
                return mid_pointer
            elif mid_pointer**2<target:
                left_pointer = mid_pointer+1
            else:
                right_pointer = mid_pointer
            mid_pointer = (left_pointer+right_pointer)//2
        return left_pointer-1




if __name__ == "__main__":
    target = int(input("输入要计算平方根的数："))
    print(squareRoot(target))
