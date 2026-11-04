# 给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。
#
# 例1：
#     输入：matrix = [[1,1,1],[1,0,1],[1,1,1]]
#     输出：[[1,0,1],[0,0,0],[1,0,1]]
#
# 例2：
#     输入：matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
#     输出：[[0,0,0,0],[0,4,5,0],[0,3,1,0]]

#普通想法：用字典来记录扫描到矩阵中0的列和行，然后在次扫描矩阵，将字典中的记录的行和列全部置为0
# def matrix_zero(matrix):
#     line = len(matrix) #矩阵的行数
#     column = len(matrix[0]) #矩阵的列数——>一行有多少个元素
#
#     matrix_new = []
#
#     #扫描矩阵的0，并将其行列记录在矩阵当中
#     for i in range(line):
#         for j in range(column):
#             if matrix[i][j]==0:
#                 matrix_new.append([i,j])
#
#     #按照扫描到的0的位置将矩阵matrix的行列全部置为0
#     for i in range(len(matrix_new)):
#         line_zero, column_zero = matrix_new[i]
#         #将line_zero行所有元素变为0
#         for j in range(column):
#             matrix[line_zero][j] = 0
#         #将column_zero列所有元素变为0
#         for k in range(line):
#             matrix[k][column_zero] = 0
#     return matrix


#进阶想法：
def matrix_zero(matrix):
    line = len(matrix) #矩阵有多少行
    column = len(matrix[0]) #矩阵有多少列——>一行有多少个元素
    line_zero = False
    column_zero = False

    #遍历第一行和第一列，查找是否有0元素.有0元素将变量line_zero或者column_zero设为True
    #遍历第一行：
    for i in range(column):
        if matrix[0][i]==0:
            line_zero = True
    #遍历第一列：
    for i in range(line):
        if matrix[i][0]==0:
            column_zero = True

    #遍历除了第一行和第一列的元素，看是否为0，有零的话将行首、列首设为0
    for i in range(1,line):
        for j in range(1,column):
            if matrix[i][j]==0:
                #行首设为0
                matrix[0][j] = 0
                #列首设为0
                matrix[i][0] = 0

    #在次遍历除了第一行和第一列的元素，看该元素所对应的行首或者列首是否为0，若为0，则将该元素设为0
    for i in range(1,line):
        for j in range(1,column):
            #当列首为0 或者 行首为0时，将该元素设为0
            if matrix[0][j]==0 or matrix[i][0]==0:
                matrix[i][j] = 0

    #通过变量line_zero和 column_zero的bool值查看第一行和第一列是否有0，若改行有0，则一整行全部变为0，若该列有0，则一整行都变为0
    if line_zero==True:
        for j in range(column):
            matrix[0][j] = 0
    if column_zero==True:
        for i in range(line):
            matrix[i][0] = 0

    return matrix


if __name__ == "__main__":
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    #     输出：[[1,0,1],[0,0,0],[1,0,1]]

    # matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    #     输出：[[0,0,0,0],[0,4,5,0],[0,3,1,0]]

    print(matrix_zero(matrix))


# 普通想法：用字典来记录扫描到矩阵中0的列和行，然后在次扫描矩阵，将字典中的记录的行和列全部置为0
# 思路：
#     1.用双重for循环查找到原矩阵中0的行列，并将其行列的值保存到新的矩阵当中去。
#     2.for循环依次取出用来记录0行列值的新矩阵，在将每一行和每一列分别置为0

# 进阶想法：(原地修改)
# 1.先遍历第一行和第一列查看是否有0元素，如果第一行有零元素则将变量line_zero设为True,若果第一列有零元素，则将变量line_zero设为True.
#     (1)为什么要检查第一行和第一列是否有0，并用变量来记录？
#         当第一行有0的时候那么第一行元素会全部变成0，即[0,0]的元素为0，那么第一列的元素将会变成0，如此下去矩阵中的所有元素最终将会变成0.
# 2.遍历除了第一行和第一列外的元素，查看是否有为0的元素，当有0元素的时候，将该元素所对应的行首和列首元素设为0。
# 3.继续遍历除了第一行和第一列外的元素，并查看每一个元素所对应的行首或者列首是否是否为0，若为0，则将 该元素 设为0.知道遍历完所有元素
# 4.通过第一步遍历第一行和第一列得到的变量line_zero、line_zero来判断是否要要将第一行和第一列的元素全部设置为0

