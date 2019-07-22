"""
r[i]=r[j]，且r[i]在r[j]之前，而在排序后的序列中，r[i]仍在r[j]之前，则称这种排序算法是稳定的；否则称为不稳定的。

稳定的排序算法：冒泡排序、插入排序、归并排序。
不是稳定的排序算法：选择排序、快速排序、堆排序。
"""

"""
冒泡排序
相邻两项比较，小的放到前面
复杂度 O(n²) 
"""


def bubbleSort(arr):
    for i in range(1, len(arr)):
        for j in range(0, len(arr) - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


"""
选择排序
选择排序提高了冒泡排序的性能，它每遍历一次列表只交换一次数据，找到最小值然后互换位置
复杂度 O(n²) 
"""


def selectionSort(arr):
    for i in range(len(arr) - 1):
        # 记录最小数的索引
        minIndex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        # i 不是最小数时，将 i 和最小数进行交换
        if i != minIndex:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr


"""
插入排序
建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。
复杂度 O(n²) 
"""


def insertionSort(alist):
    for i in range(1, len(alist)):
        currentValue = alist[i]
        position = i
        # 将选取的值在有序序列中，从后往前逐个比较，找到其在有序序列中的位置
        while alist[position - 1] > currentValue and position > 0:
            alist[position] = alist[position - 1]
            position = position - 1
        alist[position] = currentValue
    return alist


"""
归并排序

复杂度 O(nlogn)
"""

"""
快速排序
分治法，所有元素比基准值 pivotkey 小的摆放在基准前面，所有元素比基准值 pivotkey 大的摆在基准的后面
递归地把小于基准值的子数列和大于基准值的子数列排序
最好情况  O(nlogn)
最坏情况  O(n²) 如果每一次最左边的值最小且被选为 pivotkey，右边几乎为整个序列
"""
def quickSort(arr, left=None, right=None):
    left = 0 if left is None else left
    right = len(arr) - 1 if right is None else right
    if left < right:
        partitionIndex = partition(arr, left, right)
        quickSort(arr, left, partitionIndex - 1)
        quickSort(arr, partitionIndex + 1, right)
    return arr

def partition(L, left, right):
    pivotkey = L[left]

    while left < right:
        while left < right and L[right] >= pivotkey:
            right -= 1
        L[left] = L[right]

        while left < right and L[left] <= pivotkey:
            left += 1
        L[right] = L[left]

    L[left] = pivotkey
    return left

print(quickSort([3, 2, 1, 5, 9, 10, 4, 8]))

"""
堆排序
堆是一个近似完全二叉树的结构，除了最后一层之外的其他每一层都被完全填充，
并且所有结点都保持向左对齐的树，子结点的值总是小于（或者大于）它的父节点。

大顶堆：每个节点的值都大于或等于其子节点的值，在堆排序算法中用于升序排列
小顶堆：每个节点的值都小于或等于其子节点的值，在堆排序算法中用于降序排列
"""

