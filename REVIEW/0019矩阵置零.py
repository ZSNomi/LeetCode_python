# 给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。
#
# 例1：
#     输入：matrix = [[1,1,1],[1,0,1],[1,1,1]]
#     输出：[[1,0,1],[0,0,0],[1,0,1]]
#
# 例2：
#     输入：matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
#     输出：[[0,0,0,0],[0,4,5,0],[0,3,1,0]]

#方法1：普通方法：用新数组记录下来0元素的行列，在根据新数组的数据进行填充0
# def matrix_zero(matrix):
#     line = len(matrix) #矩阵行数
#     column = len(matrix[0]) #矩阵的列数——>一行有多少个元素
#     new_list = []
#
#     #记录原矩阵中0所在行数与列数
#     for i in range(line):
#         for j in range(column):
#             if matrix[i][j]==0:
#                 new_list.append([i,j])
#
#     #遍历新矩阵，得到每一个0的行数和列数（需要解包操作）
#     for line_zero,column_zero in new_list:
#         #将原数组中的line_zero行和column_zero列全部置为0
#
#         #将原数组中的line_zero行全部置为0:
#         for i in range(column):
#             matrix[line_zero][i] = 0
#         #将原数组中的column_zero列全部置为0:
#         for i in range(line):
#             matrix[i][column_zero] = 0
#
#     return matrix

#原地修改方式：利用第一行和第一列来标记改行或该列中是否有0元素。但是需要先检查第一行和第一列中是否有0元素，并用变量保存
def matrix_zero(matrix):

    line = len(matrix) #矩阵的行数
    column = len(matrix[0]) #矩阵的列数

    #第一行、列是否有0元素的判断变量
    line_zero = False
    column_zero = False

    #1.检查第一行、列是否有零
    #检查第一行是否有0元素：
    for i in range(column):
        if matrix[0][i]==0:
            line_zero = True
    #检查第一列是否有0元素
    for i in range(line):
        if matrix[i][0]==0:
            column_zero= True

    #2.检查除了第一行和第一列以外的所有元素是否有0元素，如果有0元素，那么将该零元素所在的行首和列首元素设置为0
    for i in range(1,line):
        for j in range(1,column):
            if matrix[i][j]==0:#如果当前元素为0，则将i行的首元素设为0，以及将j列的首元素设为0
                matrix[i][0] = 0 #将列首设为0
                matrix[0][j] = 0 #将行首设为0

    #3.再次遍历原矩阵除了第一行和第一列外的所有元素：这次的目的是看所对应的列首或者行首是否是0，如果是0，那么该元素matrix[i][j]置为0
    for i in range(1,line):
        for j in range(1,column):
            #判断matrix[i][j]元素的行首列首是否为0，只要有一个为0，那么该元素就要置为0
            if matrix[0][j]==0 or matrix[i][0]==0:
                matrix[i][j] = 0

    #4.再次遍历第一行和第一列：经过前3步，已经将所有除了第一行和第一列应该置0的元素全部置0，然后现在需要判断第一行是否有零，
    # 如果有那么第一行全部为0，同理第一列如果有0，那么第一列的所有元素都要置0
    #判断第一行是否有0：
    if line_zero==True:
        for i in range(column):
            matrix[0][i] = 0
    #判断第一列是否有0：
    if column_zero==True:
        for i in range(line):
            matrix[i][0] = 0

    return matrix


if __name__ == "__main__":
    # matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    #     输出：[[1,0,1],[0,0,0],[1,0,1]]

    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    #     输出：[[0,0,0,0],[0,4,5,0],[0,3,1,0]]

    print(matrix_zero(matrix))
