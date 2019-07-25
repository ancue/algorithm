'''
07-斐波那契数列

大家都知道斐波那契数列
现在要求输入一个整数n，请你输出斐波那契数列的第n项。
n<=39
不是求出整个数列，这样会占用空间
使用一个长度为2的列表记录最新的两个值
'''


def fib(n):
    tempArray = [0, 1]
    if n >= 2:
        for i in range(2, n + 1):
            tempArray[i % 2] = tempArray[0] + tempArray[1]
    return tempArray[n % 2]


print('\nFib')
print(fib(0))
print(fib(1))
print(fib(2))
print(fib(3))
print(fib(39))

'''
08-跳台阶

青蛙跳台阶, 每次可以跳1级或2级
求该青蛙跳上一个n 级的台阶总共有多少种跳法。
是n-1 和 n-2 的可能跳法的总和，与斐波那契相同
'''


def jumpFloor(number):
    tempArray = [1, 2]
    if number >= 3:
        for i in range(3, number + 1):
            tempArray[(i + 1) % 2] = tempArray[0] + tempArray[1]
    return tempArray[(number + 1) % 2]


print('\njumpFloor')
print(jumpFloor(1))
print(jumpFloor(3))
print(jumpFloor(5))

'''
09-变态跳台阶

青蛙跳台阶, 每次可以跳1级、2级、。。。、n级
此时该青蛙跳上一个n级的台阶总共有多少种跳法

F(n)=F(n-1)+F(n-2)+....+F(0)
F(n-1)=F(n-2)+F(n-3)+F(0)

得到F(n) = 2*F(n-1)
'''


def jumpFloor2(number):
    n = 1
    if number >= 2:
        for i in range(number - 1):
            n = n * 2
    return n


print('\njumpFloor2')
print(jumpFloor2(1))
print(jumpFloor2(3))
print(jumpFloor2(5))

'''
10-矩形覆盖

我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？

n 是n-1 和 n-2 的可能的总和，与斐波那契相似
'''


def rectCover(number):
    if number == 0:
        return 0
    tempArray = [1, 2]
    if number >= 3:
        for i in range(3, number + 1):
            tempArray[(i + 1) % 2] = tempArray[0] + tempArray[1]
    return tempArray[(number + 1) % 2]


'''
29-最小的k个数

输入n个整数，找出其中最小的K个数。
例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4。

O(nlogk)的算法, 适合海量数据
利用一个k容量的容器存放数组, 构造最大堆
当下一个数据大于最大数, 跳过, 小于最大数, 则进入容器替换之前的最大数

堆分为两种：最大堆和最小堆，两者的差别在于节点的排序方式。
在最大堆中，父节点的值比每一个子节点的值都要大。
在最小堆中，父节点的值比每一个子节点的值都要小。
这就是所谓的“堆属性”，并且这个属性对堆中的每一个节点都成立。
注意：堆的根节点中存放的是最大或者最小元素，但是其他节点的排序顺序是未知的。
'''

import heapq


def getLeastNums(inputs, k):
    if inputs == None or len(inputs) < k or len(inputs) <= 0 or k <= 0:
        return []

    output = []
    for num in inputs:
        if len(output) < k:
            output.append(num)
        else:
            # 构造最大堆
            output = heapq.nlargest(k, output)
            if num > output[0]:
                continue
            else:
                output[0] = num
    return output[::-1]


print('\ngetLeastNums')
print(getLeastNums([], 2))
print(getLeastNums([1, 2], 3))
print(getLeastNums([3, 5, 1, 5, 2], 3))

'''
33-丑数

把只包含因子2、3和5的数称作丑数（Ugly Number）。
例如6、8都是丑数，但14不是，因为它包含因子7。
习惯上我们把1当做是第一个丑数。
求按从小到大的顺序的第N个丑数。
'''


def getUglyNum(index):
    if index == None or index <= 0:
        return 0

    uglyNumbers = [1] * index
    nextIndex = 1
    index2 = 0
    index3 = 0
    index5 = 0

    while nextIndex < index:
        minVal = min(uglyNumbers[index2] * 2, uglyNumbers[index3] * 3, uglyNumbers[index5] * 5)
        uglyNumbers[nextIndex] = minVal

        while uglyNumbers[index2] * 2 <= uglyNumbers[nextIndex]:
            index2 += 1
        while uglyNumbers[index3] * 3 <= uglyNumbers[nextIndex]:
            index3 += 1
        while uglyNumbers[index5] * 5 <= uglyNumbers[nextIndex]:
            index5 += 1
        nextIndex += 1
    return uglyNumbers[-1]


print('\ngetUglyNum')
print(getUglyNum(0))
print(getUglyNum(1))
print(getUglyNum(15))

'''
41-和为s的连续整数序列

找出所有和为S的连续正数序列
输出所有和为S的连续正数序列。
序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序
'''


def findCS(tsum):
    if tsum < 3:
        return []
    # 最小数
    small = 1
    # 最大数
    big = 2
    middle = (tsum + 1) // 2
    curSum = small + big
    output = []
    # 最小数要小于中位数
    while small < middle:
        if curSum == tsum:
            output.append(list(range(small, big + 1)))
        while curSum > tsum and small < middle:
            # 如果和大于tsum，最小数向前移动一位
            curSum -= small
            small += 1
            if curSum == tsum:
                output.append(list(range(small, big + 1)))
        # 如果和小于tsum，最大数向前移动一位
        big += 1
        curSum += big
    return output


print('\nfindCS')
print(findCS(0))
print(findCS(60))

'''
42-和为s的两个数字

输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，
如果有多对数字的和等于S，输出两个数的乘积最小的。
对应每个测试案例，输出两个数，小的先输出。
'''


def find2nums(array, tsum):
    # 从左右一起查找
    if array == None or len(array) <= 0 or array[-1] + array[-2] < tsum:
        return []
    start = 0
    end = len(array) - 1
    while start < end:
        sum = array[start] + array[end]
        if sum < tsum:
            # 小于和，最小值前移一位
            start += 1
        elif sum > tsum:
            # 大于和，最大值后移一位
            end -= 1
        else:
            return [array[start], array[end]]
    return []


print('\nfind2nums')
print(find2nums([3, 4, 5, 6], 7))
print(find2nums([3, 4, 5, 6], 12))

'''
46-约瑟夫环

0, 1, 2, n-1这n个数字排成一个圆环, 从数字0开始每次从这个圆圈里删除第m个数字
求这个圆圈中最后剩下的一个数字
'''

'''
对于n个数组成的序列
第一轮从0开始，被删除的数是(m-1) % n
第二轮从m % n开始，被删除的数是(m-1) % (n - 1)
...
第n轮被删除的数字就是最后剩下的

f(1) = 0
f(i) = (f[i-1] + m) % i
'''

def remainIndex(n, m):
    if n < 1 or m < 1:
        return -1
    remainIndex = 0
    for i in range(1, n + 1):
        remainIndex = (remainIndex + m) % i
    return remainIndex

print('\nremainIndex')
print(remainIndex(7, 3))
print(remainIndex(0, 2))
print(remainIndex(5, 0))

'''
8皇后

在8*8的国际象棋上摆放八个皇后, 使其不能相互攻击, 即任意两个皇后不得处在同一行, 同一列或者同一对角线上

可以用回溯法, 也可以用下面的判别方法:
由于8各皇后的任意两个不能处在同一行, 那么肯定每一个皇后占据一行。
定义一个数组columnIndex[8], 数组中的第i个数字表示位于第i行的皇后列号
先把数组columnIndex[8]的8个数字分别用0-7初始化, 接下来就是对数组columnIndex的全排列
因为我们使用不同的数字初始化数组,所以任意两个皇后肯定不同列, 只需判断每一个排列对应的8个皇后是不是在一个对角线上
也就是对于下标i和j, 是不是abs(i-j) = columnIndex[i]-columnIndex[j]
'''

# 排序有 8! 种可能
def Permutation(pointArr):
    if not len(pointArr):
        return []
    if len(pointArr) == 1:
        return pointArr
    numList = pointArr
    numList.sort()
    pStr = []
    for i in range(len(numList)):
        if i > 0 and numList[i] == numList[i - 1]:
            continue
        temp = Permutation(numList[:i] + numList[i + 1:])

        if type(temp[0]) == int:
            for j in temp:
                pStr.append([numList[i]] + [j])
        else:
            for j in temp:
                tempArr = [numList[i]] + j
                pStr.append(tempArr)
    return pStr

def Judge(alist):
    length = len(alist)
    for i in range(length):
        for j in range(length):
            if i == j:
                continue
            if i - j == alist[i] - alist[j] or j - i == alist[i] - alist[j]:
                return False
    return True


def queen(alist):
    allAns = Permutation(alist)

    for tempList in allAns:
        isQueen = Judge(tempList)
        if isQueen:
            print(tempList)

print('\nQueen')
print(queen([0,1,2,3,4,5,6,7]))

'''
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
'''

