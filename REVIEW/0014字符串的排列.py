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

def judgment(s1,s2):

    window = {}#用来保存当前窗口中存在s1中的元素
    need = {}#用来保存s1中的元素类型及其个数
    left = 0
    valid = 0

    for c in s1:
        need[c] = need.get(c,0)+1

    for right,char in enumerate(s2):
        if char in need:
            window[char] = window.get(char,0)+1
            if window[char] == need[char]:
                valid += 1

        while right-left+1 >len(s1):
            char_left = s2[left]
            if char_left in need:
                if window[char_left] == need[char_left]:
                    valid -= 1
                window[char_left] -= 1
            left += 1

        if valid==len(need):
            return True

    return False


if __name__ == "__main__":

    # s1 = "ab"
    # s2 = "eidbaooo"
    # 输出：true

    s1 = "ab"
    s2 = "eidboaoo"
    # 输出：false

    print(judgment(s1,s2))

#思路：在S2上维持一个和s1一样大的滑动窗口，判断窗口内的字符及其个数和s1的是否一致。
# 1.确定使用 滑动窗口 且   滑动窗口的大小应该和s1的大小一致，不一致就需要扩大、缩小窗口
# 2.将窗口内中存在于s1中的字符放到字典window中并记录其个数。当窗口小于的时候其实什么都不用干，只需要扩大窗口就可以了。——>小技巧：因为是字符串，所以可以通过enumerate（）方式来得到下标（赋值给right）以及字符，不用使用s2[right]的形式
# 3.用valid来判断是否已经满足了条件，并在窗口滑动的过程中相应的改变valid
# 4.如果未满足条件且窗口已经大于s1的长度的话进行缩小窗口
# 5.缩小窗口的过程中需要判断left所指的字符是否属于need，并实时改变valid的值。