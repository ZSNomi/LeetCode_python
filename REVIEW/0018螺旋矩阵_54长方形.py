# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
#
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
#
# 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]

def matrix_add(matrix):
    line_num = len(matrix) #矩阵中有几行
    column_num = len(matrix[0]) #矩阵中一行有多少列

    left = 0
    right = column_num-1
    top = 0
    bottom = line_num -1

    record_num = 0
    matrix_all = [0]*(line_num*column_num) #建立一个个数为m*n个初始为0的数列


    while record_num<line_num*column_num:
        #从左到右
        for i in range(left,right+1):
            matrix_all[record_num] = matrix[top][i]
            record_num += 1
        top += 1
        if record_num>=line_num*column_num:
            break

        #从上到下
        for i in range(top,bottom+1):
            matrix_all[record_num] = matrix[i][right]
            record_num += 1
        right -= 1
        if record_num>=line_num*column_num:
            break

        #从右到左
        for i in range(right,left-1,-1):
            matrix_all[record_num] = matrix[bottom][i]
            record_num += 1
        bottom -= 1
        if record_num>=line_num*column_num:
            break

        #从下到上：
        for i in range(bottom,top-1,-1):
            matrix_all[record_num] = matrix[i][left]
            record_num += 1
        left += 1
        if record_num>=line_num*column_num:
            break

    return matrix_all





if __name__ == "__main__":
    # matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # 输出：[1,2,3,6,9,8,7,4,5]

    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    # 输出：[1,2,3,4,8,12,11,10,9,5,6,7]

    print(matrix_add(matrix))