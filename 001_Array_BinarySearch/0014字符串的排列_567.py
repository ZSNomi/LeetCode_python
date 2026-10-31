# 给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的 排列。如果是，返回 true ；否则，返回 false 。
# 换句话说，s1 的排列之一是 s2 的 子串 。
#
# 示例 1：
# 输入：s1 = "ab" s2 = "eidbaooo"
# 输出：true
# 解释：s2 包含 s1 的排列之一 ("ba")
#
# 示例 2：
# 输入：s1= "ab" s2 = "eidboaoo"
# 输出：false

#法1：最坏情况下：O（m*n），问题出在：right += 1在里面手动添加了right。——>这样的话right的推进还特别的乱
# def substring_panduan(s1,s2):
#     need = {}
#     valide = 0
#     window = {}
#     for c in s1:
#         need[c] = need.get(c,0)+1
#
#     for right in range(len(s2)):
#         c = s2[right]
#
#         while c in need:
#             window[c] = window.get(c,0)+1
#             if window[c] == need[c]:
#                 valide += 1
#             if window[c] > need[c]:
#                 break
#             if valide == len(need):
#                 return True
#             if right+1 < len(s2):
#                 right += 1
#             else:
#                 return False
#             c = s2[right]
#         window.clear()
#         valide = 0
#
#     return False

#法2：滑动窗口
def substring_panduan(s1,s2):
    left= 0
    need = {}
    window = {}
    valid = 0

    #将需要的字符存放在字典当中
    for c in s1:
        need[c] = need.get(c,0)+1

    for right,c in enumerate(s2):
        if c in need:
            window[c] = window.get(c,0)+1
            if window[c] == need[c]:
                valid += 1

        while right-left+1 > len(s1):
            d = s2[left]
            if d in need:
                if window[d] == need[d]:
                    valid -= 1
                window[d] -= 1
            left += 1

        if  right-left+1==len(s1) and valid==len(need):
            return True

    return False








if __name__ == "__main__":
    # s1 = "ab"
    # s2 = "eidbaooo"
    # 输出：true

    # s1 = "ab"
    # s2 = "eidboaoo"
    # 输出：false

    s1 = "abccbb"
    s2 = "eidboaoabccboabcbcb"

    # s1 = "abc"
    # s2 = "aabbcc"

    print(substring_panduan(s1,s2))

