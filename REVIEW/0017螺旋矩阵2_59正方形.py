# 给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。

# 示例 1：
# 输入：n = 3
# 输出：[[1,2,3],[8,9,4],[7,6,5]]
#
# 示例 2：
# 输入：n = 1
# 输出：[[1]]

def spiralMatrix(n):
    left = 0
    right = n-1
    top = 0
    bottom = n-1
    record_num = 1

    #初始化一个n*n且初始值全为0的矩阵
    matrix = [[0]*n for _ in range(n)]

     #从左到右、从上到下、从右往左、从下往上依次添加元素直到n**2
    while record_num<=n**2:
        # 从左到右:最上面一行
        for i in range(left, right+1):
            matrix[top][i] = record_num
            record_num += 1
        top += 1

        # 从上到下：最右边一列
        for i in range(top, bottom+1):
            matrix[i][right] = record_num
            record_num += 1
        right -= 1

        # 从右到左：最下面一行
        for i in range(right, left-1, -1):
            matrix[bottom][i] = record_num
            record_num += 1
        bottom -= 1

        # 从下到上：最左边一列
        for i in range(bottom, top-1,-1):
            matrix[i][left] = record_num
            record_num += 1
        left += 1
    return matrix


if __name__ == "__main__":
    # n = 3
    # 输出：[[1,2,3],[8,9,4],[7,6,5]]

    n = 1
    # 输出：[[1]]

    print(spiralMatrix(n))

    