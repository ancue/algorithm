# 1. 两数之和
"""
给定一个整数数组 nums 和一个目标值 target
在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
"""


def twoSum(nums, target):
    hashdict = {}
    for i, item in enumerate(nums):
        if (target - item) in hashdict:
            return (hashdict[target - item], i)
        hashdict[item] = i

    return (-1, -1)

print(twoSum([1, 4, 7, 9, 3], 7))

# 三数之和
"""
给定一个包含 n 个整数的数组 nums，
判断 nums 中是否存在三个元素 a，b，c ，
使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

"""


def threeSum(nums):
    if nums is None or len(nums) < 3:
        return []
    if len(nums) == 3 and sum(nums) == 0:
        return [sorted(nums)]
    # 从小到大排序
    nums.sort()
    result, length = [], len(nums)
    for i in range(length - 2):
        if i > 0 and nums[i - 1] == nums[i]:
            continue

        # 从两端到中间
        l, r = i + 1, length - 1
        while l < r:
            # 对于每一个元素，从两端到中间搜索和为0的组合
            sum = nums[i] + nums[l] + nums[r]
            if sum == 0:
                result.append([nums[i], nums[l], nums[r]])
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
            if sum > 0:
                r -= 1
            else:
                l += 1
    return result

print(threeSum([1, 0, -1, 2, 3, -2]))


# 121. 股票最大利润
"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。
只允许完成一笔交易
"""


def maxProfit1(prices):
    length = len(prices)
    if length == 0:
        return 0
    max_profit, low = 0, prices[0]
    for i in range(1, length):
        if low > prices[i]:
            low = prices[i]
        else:
            temp = prices[i] - low
            if temp > max_profit:
                max_profit = temp
    return max_profit


# 122. 股票买卖最大利润
"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。
允许多次交易
"""


def maxProfit2(prices):
    priceList = zip(prices[0:-1], prices[1:])
    return sum([y - x for x, y in priceList if x < y])


# 122. 股票买卖最大利润
"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。
最多允许两笔交易
"""


def maxProfit2(prices):
    ls = len(prices)
    if ls == 0:
        return 0
    b1 = b2 = -prices[0]
    s1 = s2 = 0
    for i in range(1, ls):
        b1 = max(b1, -prices[i]) # 手上的钱减去价钱，即为剩余
        s1 = max(b1 + prices[i], s1) # 第一次卖掉，为剩余
        b2 = max(b2, s1 - prices[i])    # 再买一次
        s2 = max(s2, b2 + prices[i])    # 再卖一次
    return max(s1, s2)


# 字符串反转
"""
输入字符串以字符数组 char[] 的形式给出。
"""

# 8. 字符串转整数
"""
假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−231,  231 − 1]。
如果数值超过这个范围，请返回  INT_MAX (2^31 − 1) 或 INT_MIN (−2^31) 。

如果字符串以空格开始，寻找到第一个非空格的字符
如果第一个非空字符为正号或负号，则与后面尽可能多的数字组合起来
如果第一个字符不是正负号，或数字字符，返回0
"""


def myAtoi(str):
    sign = 1
    max_int, min_int = 2147483647, -2147483648
    result, pos = 0, 0
    ls = len(str)
    while pos < ls and str[pos] == ' ':
        pos += 1
    if pos < ls and str[pos] == '-':
        sign = -1  # 符号
        pos += 1
    elif pos < ls and str[pos] == '+':
        pos += 1
    # ord() 函数以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值
    # 判断字符是否为数字，可以import re ，用正则判断
    while pos < ls and ord(str[pos]) >= ord('0') and ord(str[pos]) <= ord('9'):
        num = ord(str[pos]) - ord('0')
        # 如果超出范围
        if result > max_int / 10 or (result == max_int / 10 and num >= 8):
            if sign == -1:
                return min_int
            return max_int

        result = result * 10 + num
        pos += 1
    return sign * result

# 26. 删除数组中重复的数
"""
给定一个排序数组，要求在原地删除重复出现的元素，使得每个元素只出现一次
返回移除后数组的新长度
"""


def removeDuplicates(nums):
    if len(nums) <= 1:
        return len(nums)
    left = 0
    for i in range(1, len(nums)):
        if nums[left] != nums[i]:
            left += 1
            nums[left] = nums[i]

    return left + 1


# 27. 删除元素
"""
给定一个数组 nums 和一个值 val，
你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。
"""


def removeElement(nums, val):
    ls = len(nums)
    if ls == 0:
        return ls
    count = 0
    index = 0
    while index < ls - count:
        if nums[index] == val:
            nums[index] = nums[ls - 1 - count]
            count += 1
        else:
            index += 1
    return ls - count


# 53. 最大子序和
"""
给定一个整数数组 nums ，
找到一个具有最大和的连续子数组（子数组最少包含一个元素）
返回其最大和。
"""


def maxSubArray(nums):
    if nums is None or len(nums) == 0:
        return []

    sum = 0
    maxsum = nums[0]
    for i in range(len(nums)):
        sum += nums[i]
        # 元素可以为负，但是sum不能为负
        if sum < 0 :
            sum = 0
        maxsum = max(maxsum, sum)
    return maxsum

