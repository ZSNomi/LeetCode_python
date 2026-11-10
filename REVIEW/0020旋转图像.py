# 给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。
# 你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像
#
# 例1：
#     输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
#     输出：[[7,4,1],[8,5,2],[9,6,3]]
# 例2：
#     输入：matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
#     输出：[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

# 方法1：两个动作：（1）按照主对角线交换数据值 （2）左右交换数据值
def rotationMatrix(matrix):
    line = len(matrix) #矩阵的行数
    column = len(matrix[0]) #矩阵的列数——>一行中有多少个元素

    #动作1：按照主对角线交换数据
    for i in range(column):
        for j in range(i,line):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

    #动作2：左右交换数据值：
    for i in range(column):
        for j in range(line//2):
            matrix[i][j],matrix[i][column-j-1] = matrix[i][column-j-1],matrix[i][j]

    return matrix






if __name__ == "__main__":
    # matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    #     输出：[[7,4,1],[8,5,2],[9,6,3]]

    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    #     输出：[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

    print(rotationMatrix(matrix))
