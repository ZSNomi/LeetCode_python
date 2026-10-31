# 给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。

# 示例 1：
# 输入：n = 3
# 输出：[[1,2,3],[8,9,4],[7,6,5]]
#
# 示例 2：
# 输入：n = 1
# 输出：[[1]]

#方法1：（推荐）
def matrix(n):
    left,right = 0,n-1 #left 和 right是用来控制从左到右或者是从左到右进行填充数字时的边界
    top,bottom = 0,n-1#top 和 bottom 是用来控制从上到下或者从下岛上进行数字填充时的边界
    #建立一个n*n的矩阵：
    matrix_list = [[0]*n for _ in range(n)]

    num = 1 #即将填充的数

    while num <= n*n:
        # 1：从左往右进行填充：
        for i in range(left, right+1):
            matrix_list[top][i] = num
            num += 1
        top += 1  # top收缩——>改行已经填满，下次从上往下或者从下往上进行填充的时候改行不再被填充

        # 2:从上往下进行填充：
        for i in range(top, bottom+1):
            matrix_list[i][right] = num
            num += 1
        right -= 1

        # 3:从右往左进行填充：
        for i in range(right, left-1,-1):
            matrix_list[bottom][i] = num
            num += 1
        bottom -= 1

        # 4:从下往上进行填充
        for i in range(bottom, top-1,-1):
            matrix_list[i][left] = num
            num += 1
        left += 1

    return matrix_list







if __name__ == "__main__":
    # n = 3
    # 输出：[[1,2,3],[8,9,4],[7,6,5]]

    n = 1
    # 输出：[[1]]

    print(matrix(n))



