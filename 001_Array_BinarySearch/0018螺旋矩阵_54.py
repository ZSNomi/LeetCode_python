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

        # 从上到下
        for i in range(top, bottom + 1):
            new_matrix[pos] = matrix[i][right]
            pos += 1
        right -= 1

        # 从右到左
        for i in range(right, left - 1, -1):
            new_matrix[pos] = matrix[bottom][i]
            pos += 1
        bottom -= 1

        # 从下往上
        for i in range(bottom, top - 1, -1):
            new_matrix[pos] = matrix[i][left]
            pos += 1
        left += 1
    return new_matrix


if __name__ == "__main__":
    # matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # 输出：[1,2,3,6,9,8,7,4,5]

    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    # 输出：[1,2,3,4,8,12,11,10,9,5,6,7]

    print(get_element(matrix))


