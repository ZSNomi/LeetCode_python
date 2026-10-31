# 给定两个字符串 s 和 t，长度分别是 m 和 n，返回 s 中的 最短窗口子串，使得该子串包含 t 中的每一个字符（包括重复字符）。
# 如果没有这样的子串，返回空字符串 ""。
#
# 示例 1：
# 输入：s = "ADOBECODEBANC", t = "ABC"
# 输出："BANC"
# 解释：最小覆盖子串 "BANC" 包含来自字符串 t 的 'A'、'B' 和 'C'
#
# 示例 2：
# 输入：s = "a", t = "a"
# 输出："a"
# 解释：整个字符串 s 是最小覆盖子串
#
# 示例 3:
# 输入: s = "a", t = "aa"
# 输出: ""
# 解释: t 中两个字符 'a' 均应包含在 s 的子串中，
# 因此没有符合条件的子字符串，返回空字符串

def min_string(s,t):
    if len(s)<len(t):
        return ""

    need_t = {}
    window = {}
    valid = 0
    left = 0
    min_num = float('inf')
    new_min_string = ''

    for i in t:
        need_t[i] = need_t.get(i,0)+1

    for right in range(len(s)):
        char_right = s[right]
        if char_right in need_t:
            window[char_right] = window.get(char_right,0)+1
            if window[char_right] == need_t[char_right]:
                valid += 1



        while valid==len(need_t):
            if right-left+1<min_num:
                min_num = right-left+1
                new_min_string = s[left:right+1]#截取字符串

            #尝试缩小窗口：
            char_left = s[left]
            if char_left in need_t:
                window[char_left] -= 1
                if window[char_left]<need_t[char_right]:
                    valid -= 1
            left += 1
    return new_min_string




if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    # 输出："BANC"

    # s = "a"
    # t = "a"
    # 输出："a"

    # s = "a"
    # t = "aa"
    # 输出: ""

    s = "AADOBECODEBASDASDASDANC"
    t = "ABC"
    print(min_string(s,t))

#1：可以不用截取S的长度，用当找到后记录下当前left的位置赋值给变量start_pos，最后返回S【start_pos,start_pos+min_len】\

# 思路：
# 1：明确采用滑动窗口
# 2：思考何时扩大窗口，何时缩小窗口：
#     （1）何时扩大窗口：一直扩大窗口直到字符串中包括了t中所需的字符及其个数。（即valid满足条件）
#     （2）何时缩小窗口：当valid满足条件（valid==need_t:字符串中包括了t中所需的字符及其个数）后开始缩小窗口
# 3.需要哪些变量作用是什么？
#     （1）left：左指针
#     （2）right：右指针
#     （3）window字典:只需要记录下当前窗口中在need_t需要的字符及其个数，不用所有的字符都进行记录
#     （4）min_num:记录下满足条件最短的字符个数
#     （5）valid：用来记录各个所需字符的字符数是否满足条件。当个数没有满足所需个数valid不变，只有当该字符的个数达到了valid才能加1，直到valid与need_t的个数相等（所有字符的个数都满足条件）
#     （6）new_string（非必须）：用来记录当前满足条件的字符串。可用startpos变量来代替
