#1：内置函数：Python 解释器自带的、不需要导入任何模块就可以直接使用的函数。

#（1）内置函数range（）:返回一系列增加整数，长用于for



#（2）内置函数zip():返回一系列的并行元素的元组
#     ①使用zip一定要用list括起来
#     ②在for中使用zip时需要有对应的元素来进行接收
#     ③若元素个数不同，没法一一对应的话，那么多的元素不会展现
s1= (1,2,3,"a","like")
s2 = (4,5,"good","A")
print(list(zip(s1,s2)))#[(1, 4), (2, 5), (3, 'good'), ('a', 'A')]

for a,b in zip(s1,s2):
    print(a,b)

str1 = "good"
str2 = "bad"
print(list(zip(str1,str2)))#[('g', 'b'), ('o', 'a'), ('o', 'd')]


#（3）内置函数enumerate（）：同时生成可迭代对象中元素的值和索引
A = "ABCDE"
for (index,value) in enumerate(A):
    print(index,value,end="  ")#0 A  1 B  2 C  3 D  4 E
print()
for (i,v) in enumerate(A,1):#下标从1开始数
    print(i,v,end="  ")#1 A  2 B  3 C  4 D  5 E

