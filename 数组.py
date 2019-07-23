'''
1.二维数组中的查找

在一个二维数组中，每一行都按照从左到右递增的顺序排序
每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''

'''
查找方式从右上角或者右上角开始查找
如果当前元素大于target, 左移一位继续查找
如果当前元素小于target, 下移一位继续查找
进行了简单的修改, 可以判定输入类型为字符的情况
'''


class SearchNum():

    def find(self, target, array):
        if not array:
            return False

        row_nums = len(array)
        col_nums = len(array[0])
        row = 0
        col = col_nums - 1

        while col >= 0 and row <= row_nums - 1:
            if target > array[row][col]:
                row += 1
            elif target < array[row][col]:
                col -= 1
            else:
                return True
        return False


search = SearchNum()
print('\nSearchNum')
print(search.find(10, [[1, 3, 5, 7, 8],
                       [3, 5, 7, 9, 11]]))

'''
6. 旋转数组的最小数字

把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
'''


class Rotate():
    '''
    考虑情况：
    1. 数组为空
    2. 如果按顺序排列
    3. 数组只有一个元素
    4. 旋转数组
    '''

    def find(self, array):
        if not array:
            return 0

        first = 0
        last = len(array) - 1
        minVal = array[0]

        if array[first] < array[last]:
            return array[first]
        else:
            # 二分法找到数组中的最小值
            while (last - first) > 1:
                mid = (first + last) // 2

                if array[first] == array[last] == array[mid]:
                    for i in range(1, len(array)):
                        if array[i] < minVal:
                            minVal = array[i]
                            last = i
                elif array[mid] >= array[first]:
                    first = mid
                elif array[mid] <= array[last]:
                    last = mid

            minVal = array[last]
            return minVal


Test = Rotate()
print('\nRotate')
print(Test.find([3, 4, 5, 1, 2]))
print(Test.find([1, 2, 3, 4, 5]))
print(Test.find([1, 1, 1, 0, 1]))
print(Test.find([1, 0, 1, 1, 1]))
print(Test.find([]))
print(Test.find([1]))
print(Test.find([1, 0]))

'''
13. 调整数组顺序使奇数位于偶数前面

输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分
所有的偶数位于位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
'''


class OrderArray():
    def sort_array(self, array):
        if not array:
            return array

        odd = []
        even = []
        for i in range(len(array)):
            if array[i] % 2 == 0:
                even.append(array[i])
            else:
                odd.append(array[i])

        return odd + even

    def sort_array2(self, array):
        return sorted(array, key=lambda c: c % 2, reverse=True)


test = OrderArray()
print('\nOrderArray')
print(test.sort_array2([2, 3, 1, 9, 5, 0, 8]))

'''
28. 数组中出现次数超过一半的数字

数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
'''


class MoreThanHalfNum_Solution():
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        length = len(numbers)
        if not numbers:
            return 0
        result = numbers[0]
        times = 1

        '''
        当下一个数字与上一个相同时，times++
        不相同时，times--
        times为0时，另选一个数，times=1
        最终选出需要去验证的数字
        复杂度为O(n)
        当作一个特殊的处理去记
        
        还可以使用collections.Counter，只是复杂度就不知道了
        '''
        for i in range(1, length):
            if times == 0:
                result = numbers[i]
                times = 1
            elif numbers[i] == result:
                times += 1
            else:
                times -= 1

        if not self.CheckMoreThanHalf(numbers, length, result):
            return 0
        return result

    def CheckMoreThanHalf(self, numbers, length, number):
        times = 0
        for i in range(length):
            if numbers[i] == number:
                times += 1

        if times * 2 <= length:
            return False
        return True


moreThanHalf = MoreThanHalfNum_Solution()
print('\nMoreThanHalfNum_Solution')
print(moreThanHalf.MoreThanHalfNum_Solution([3, 9, 0, 5, 2, 2]))

'''
30-连续数组的最大和

输入一个整型数组,数组里有正数也有负数。
数组中一二或连续的多个整数组成一个子数组。求所有子数组的和的最大值。
要求时间复杂度为O(n)
'''


class GreatestSumOfSubsequence():
    def find(self, array):
        if not array:
            return 0

        max_sum = 0
        cur_sum = 0

        for i in range(len(array)):
            if cur_sum <= 0:
                cur_sum = array[i]
            else:
                cur_sum += array[i]

            if cur_sum > max_sum:
                max_sum = cur_sum

        return max_sum

    def dp(self, array):
        '''
        动态规划
        '''
        if not array:
            return 0

        aList = [0] * len(array)
        for i in range(len(array)):
            if i == 0 or aList[i - 1] <= 0:
                aList[i] = array[i]
            else:
                aList[i] = array[i] + aList[i - 1]

        return max(aList)


greatest = GreatestSumOfSubsequence()
print('\nGreatestSumOfSubsequence')
print(greatest.find([]))
print(greatest.find([1, 2, -3]))
print(greatest.find([2, 5, -4, 0, 0, -2]))
print(greatest.dp([]))
print(greatest.dp([1, 2, -3]))
print(greatest.dp([2, 5, -4, 0, 0, -2]))

'''
32-把数组排成最小的数

输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
'''


class MinNumber():
    def find(self, array):
        if not array:
            return 0

        '''
        冒泡排序
        '''
        aList = [str(num) for num in array]
        for i in range(len(aList) - 1):
            for j in range(i + 1, len(aList)):
                if aList[i] + aList[j] > aList[j] + aList[i]:
                    aList[i], aList[j] = aList[j], aList[i]
        return ''.join(aList)


min_num = MinNumber()
print('\nMinNumber')
print(min_num.find([3, 32, 321]))
print(min_num.find([3]))
print(min_num.find([]))

'''
35-数组中的逆序对

在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组,求出这个数组中的逆序对的总数P。
'''
import copy


class InversePair():
    def find(self, array):
        if not array:
            return 0

        sort_arr = copy.deepcopy(array)
        sort_arr = sorted(sort_arr)
        count = 0

        for i in range(len(sort_arr)):
            count += array.index(sort_arr[i])
            # 获取了之后要删除
            array.remove(sort_arr[i])
        return count


obj = InversePair()

print('\nInverse Pair')
print(obj.find([2, 1, 3, 0]))

'''
37-数字在排序数组中出现的次数

统计一个数字在排序数组中出现的次数。
'''


class NumCount():
    def find(self, data, k):
        if not data or k not in data:
            return 0

        index = data.index(k)
        index2 = sorted(data, reverse=True).index(k)
        return len(data) - index - index2


num_count = NumCount()
print('\nNumCount')
print(num_count.find([], 2))
print(num_count.find([1, 1, 4, 4, 4, 6666, 7777], 2))
print(num_count.find([1, 1, 4, 4, 4, 6666, 7777], 4))

'''
40-数组中只出现一次的数字

一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
'''


class OnceOnly():
    def find(self, array):
        arr = []
        for i in range(len(array)):
            if array[i] not in arr:
                arr.append(array[i])
            else:
                arr.remove(array[i])
        return arr


once = OnceOnly()
print('\nOnce Only')
print(once.find([1, 2, 1, 2, 0, 7, 7, 4]))

'''
50-数组中重复的数字

在一个长度为n的数组里的所有数字都在0到n-1的范围内。
数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。
请找出数组中任意一个重复的数字。
例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是重复的数字2或者3。
'''


class DuplicateNum():
    def find(self, array):
        dup = []
        for i in range(len(array)):
            if array[i] not in dup:
                dup.append(array[i])
            else:
                return array[i]


dup = DuplicateNum()
print('\nDuplicateNum')
print(dup.find([0, 9, 1, 2, 3, 4, 4]))

'''
51-构建乘积数组

给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1]
其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。
'''


class Multiply():
    def mul(self, array):
        if not array:
            return None
        length = len(array)
        aList = [1] * length
        # 正向的时候舍弃array[0]，取[1, length -1]
        for i in range(1, length):
            aList[i] = aList[i - 1] * array[i - 1]

        temp = 1
        # 反向的时候舍弃array[length-1]，取[0,length-2]
        for i in range(length - 2, -1, -1):
            temp *= array[i + 1]
            aList[i] *= temp
        return aList


s = Multiply()
print('\nMultiply')
print(s.mul([1, 2, 3, 4]))
