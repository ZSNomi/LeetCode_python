# 给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。
# 你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像
#
# 例1：
#     输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
#     输出：[[7,4,1],[8,5,2],[9,6,3]]
# 例2：
#     输入：matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
#     输出：[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

#方法1：两个动作——>1.沿着对角线对折交换数据（matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]）  2.左右翻转每一行
# def rotationMatrix(matrix):
#     lenth_matrix = len(matrix)
#
#     #沿着组对角线折叠交换元素
#     for i in range(lenth_matrix):
#         for j in range(i+1,lenth_matrix):# 注意：j 从 i+1 开始，避免重复交换
#             matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
#
#     #左右对称交换
#     for i in range(lenth_matrix):
#         for j in range(lenth_matrix//2):
#             matrix[i][j],matrix[i][lenth_matrix-1-j] = matrix[i][lenth_matrix-1-j],matrix[i][j]
#
#     return matrix

#方法2：按层（圈）进行四角轮换
def rotationMatrix(matrix):
    n = len(matrix)

    # 一共要转多少层？n 的一半（向下取整）
    for layer in range(n // 2):
        # 每一层，从 layer 开始，到 n - 1 - layer 结束
        for j in range(layer, n - 1 - layer):
            # 保存左上角的值
            temp = matrix[layer][j]

            # 左上角 <- 左下角
            matrix[layer][j] = matrix[n - 1 - j][layer]

            # 左下角 <- 右下角
            matrix[n - 1 - j][layer] = matrix[n - 1 - layer][n - 1 - j]

            # 右下角 <- 右上角
            matrix[n - 1 - layer][n - 1 - j] = matrix[j][n - 1 - layer]

            # 右上角 <- 左上角 (之前存的 temp)
            matrix[j][n - 1 - layer] = temp

    return matrix


if __name__ == "__main__":
    # matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    #     输出：[[7,4,1],[8,5,2],[9,6,3]]

    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    #     输出：[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

    print(rotationMatrix(matrix))




