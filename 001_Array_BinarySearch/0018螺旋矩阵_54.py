# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
#
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
#
# 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]


def get_element(matrix):
    left = 0
    right = len(matrix[0]) - 1 if matrix else 0
    top, bottom = 0, len(matrix) - 1
    new_matrix = [0]*(len(matrix)*len(matrix[0]))
    pos = 0

    while pos < len(matrix) * len(matrix[0]):
        # 从左到右
        for i in range(left, right + 1):
            new_matrix[pos] = matrix[top][i]
            pos += 1
        top += 1
        if pos >= (len(matrix) * len(matrix[0])) :
            break

        # 从上到下
        for i in range(top, bottom + 1):
            new_matrix[pos] = matrix[i][right]
            pos += 1
        right -= 1
        if pos >= (len(matrix) * len(matrix[0])):
            break

        # 从右到左
        for i in range(right, left - 1, -1):
            new_matrix[pos] = matrix[bottom][i]
            pos += 1
        bottom -= 1
        if pos >= (len(matrix) * len(matrix[0])) :
            break


        # 从下往上
        for i in range(bottom, top - 1, -1):
            new_matrix[pos] = matrix[i][left]
            pos += 1
        left += 1
        if pos >= (len(matrix) * len(matrix[0])) :
            break
    return new_matrix


if __name__ == "__main__":
    # matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # 输出：[1,2,3,6,9,8,7,4,5]

    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    # 输出：[1,2,3,4,8,12,11,10,9,5,6,7]

    print(get_element(matrix))

# 注意：
#     这里和正方形之间的区别，当矩阵是一个n*n的话，那么一圈下来如何还有元素，这些元素依旧还是一个正方形，while循环依旧还是会继续执行
#     “从左到右——>从上到下——>从右到左——>从下到上”的一整个循环，这样下来后新建的数组和以前的数组个数刚好相同；如果是长方形的话就会出现
#     一圈下来后如果内部还有元素，那么不需要走完“从左到右——>从上到下——>从右到左——>从下到上”的一整个循环便可以取完全部的元素，但是依旧
#     会往下继续执行，那么久必定会超出新建的数组的界限。（核心总结：record_num < num 只在每圈开始时判断，进入一圈后四步会无条件执行；
#     当最后只剩一行或一列时，取完后仍会继续执行后面的方向，导致重复访问或下标越界）解决方法如下：
#     （1）如本方法一样，每一次取完一条边后便检查看是否已经取完全元素，如果取完了就直接跳出循环
#     （2）通过用边界条件控制，不提前越界。
#
#     （1）正方形：4*4                              长方形：
#         1  2  3  4                                    1  2  3  4
#         5  6  7  8————》一圈之后：6  7                  5  6  7  8————>一圈之后： 6  7
#         9  10 11 12            10  11                 9  10 11 12
#         13 14 15 16
