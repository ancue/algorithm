'''
02-替换空格

请实现一个函数，将一个字符串中的空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
'''


# 在Python中str类型是不可变的类型, 使用replace语句会生成一个新的str, 原始的s还是带空格的str变量
def replaceSpace(s):
    # 首先判断类型，因为如果输入为integer的话，没有len，就会直接报错
    if not isinstance(s, str) or len(s) <= 0:
        return ''

    string = list(s)
    stringReplace = []
    for item in string:
        if item == ' ':
            stringReplace.append('%')
            stringReplace.append('2')
            stringReplace.append('0')
        else:
            stringReplace.append(item)
    return "".join(stringReplace)


def replaceSpace1(s):
    if not isinstance(s, str) or len(s) <= 0:
        return ''

    return s.replace(' ', '%20')


s = 'we are happy'
print('replaceSpace')
print(replaceSpace(s))
print(replaceSpace1(s))

'''
27-字符串的排列

输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
结果请按字母顺序输出。
输入描述:
输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。
'''


def permutation(s):
    if not isinstance(s, str) or len(s) <= 0:
        return []

    if len(s) == 1:
        return list(s)

    charList = list(s)
    charList.sort()
    str1 = []
    for i in range(len(charList)):
        if i > 0 and charList[i] == charList[i - 1]:
            continue

        temp = permutation(''.join(charList[:i]) + ''.join(charList[i + 1:]))

        for j in temp:
            str1.append(charList[i] + j)
    return str1


s = 'abcc'
print('\npermutation')
print(permutation(s))

exit(0)
'''
43-字符串的左旋转

对于一个给定的字符序列S，请你把其循环左移K位后的序列输出。
例如，字符序列S=”abcXYZdef”,要求输出循环左移3位后的结果，即“XYZdefabc”。
'''


def leftRotate(s, k):
    if len(s) <= 0 or k < 0 or len(s) < 0:
        return ''

    slist = list(s)
    # 翻转数组
    rotate(slist)
    length = len(s)
    pivot = length - k
    frontlist = rotate(slist[:pivot])
    backlist = rotate(slist[pivot:])
    return ''.join(frontlist) + ''.join(backlist)


# 翻转数组
def rotate(slist):
    if not slist or len(slist) < 0:
        return ''

    start = 0
    end = len(slist) - 1
    while start < end:
        slist[start], slist[end] = slist[end], slist[start]
        start += 1
        end -= 1
    return slist


s = 'abcdefGHIJK'
s1 = ''
print('\nleftRotate')
print(leftRotate(s, 2))
print(leftRotate(s1, 2))

'''
字符串具有相同字符的最长子串

求一个字符串的最长子串，其中子串所有字符相同
'''


def findLCS(s):
    if not s:
        return ''

    if len(s) == 1:
        return s

    length = len(s)
    maxIndex, maxLength = 0, 1
    curIndex = 0

    while curIndex < length:
        tempLength = 1
        # 在一个连续的子串中
        while curIndex + tempLength < length and s[curIndex] == s[curIndex + tempLength]:
            tempLength += 1

        # 如果当前子串长度大于之前最大子串长度
        if maxLength < tempLength:
            maxLength = tempLength
            maxIndex = curIndex

        # 到达字符串的尾部，跳出
        if curIndex + tempLength == length:
            break

        curIndex += tempLength

    # 最大子串长度为1时，返回第一个字符
    if maxIndex == 1:
        return s[0]
    else:
        return s[maxIndex:maxIndex + maxLength]


s = 'abcdddeeggggg'
s1 = ''
s2 = 'abcdefg'
print('\nfindLCS')
print(findLCS(s))
print(findLCS(s1))
print(findLCS(s2))

'''
找出字符串中重复出现的最长子串

找出一行字符串中出现的相同且长度最长的字符串, 输出它及首字符的位置
例如"yyabcdabjcabceg", 输出结果应该为abc和3
'''


def maxStr(s):
    if not s:
        return ''

    if len(s) == 1:
        return [s, 0]

    length = len(s)
    temp = []
    for i in range(length):
        temp.append(s[i:])

    listWithIndex = []

    '''
    将字符串每次剔除一个，拆分为短子串，然后排序
    可以使包含相同子串的短子串相邻
    再比较相邻短子串
    '''
    for index, val in enumerate(temp):
        listWithIndex.append([val, index + 1])
    listWithIndex.sort()

    maxLength, maxList, maxIndex = 0, '', 0
    for listIndex in range(length - 1):
        firstList = listWithIndex[listIndex]
        secondList = listWithIndex[listIndex + 1]
        index, tempLength, tempList = 0, 0, ''

        while index < len(firstList[0]) and index < len(secondList[0]) and firstList[0][index] == secondList[0][index]:
            tempLength += 1
            tempList += firstList[0][index]
            index += 1
        # 如果子串长度大于之前最大子串长度
        if tempLength > maxLength:
            maxLength = tempLength
            maxList = tempList
            maxIndex = min(firstList[1], secondList[1])
    return [maxList, maxIndex]


s = 'abbcabbdtt'
print('\nmaxStr')
print(maxStr(s))
