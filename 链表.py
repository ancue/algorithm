class ListNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None


class LinkedList:
    '''
    03-从尾到头打印链表

    输入一个链表，从尾到头打印链表每个节点的值。
    '''

    def reverseTraversal(self, listNode):
        if listNode.val == None:
            return

        l = []
        head = listNode
        while head:
            # 插入在索引为0的位置
            l.insert(0, head.val)
            head = head.next
        return l

    '''
    14-链表中倒数第k个结点
    
    如果在只希望一次遍历的情况下, 寻找倒数第k个结点, 可以设置两个指针
    第一个指针先往前走k-1步, 然后从第k步开始第二个指针指向头结点
    然后两个指针一起遍历
    当地一个指针指向尾节点的时候, 第二个指针正好指向倒数第k个结点
    推广: 寻找中间节点, 两个指针一起, 第一个指针每次走两步, 第二个指针每次走一步,  快指针指到尾部, 慢指针正好指到中间
    '''

    def findKthToTail(self, head, k):
        if head == None or k < 0:
            return None

        pAhead = head
        for i in range(k - 1):
            if pAhead.next != None:
                pAhead = pAhead.next
            else:
                return None
        pBehind = head
        while pAhead.next != None:
            pAhead = pAhead.next
            pBehind = pBehind.next

    '''
    15-反转链表
    
    输入一个链表，反转链表后，输出链表的所有元素
    并没有要求打印，只需要返回反转之后的head
    '''

    def reverseList(self, head):
        reversed_head = None
        node = head
        prev = None

        while node is not None:
            next = node.next
            if next is None:
                reversed_head = node

            # 先确定结点的next
            node.next = prev

            # node 向后移动一步
            prev = node
            node = next
        return reversed_head

    '''
    16-合并两个排序的链表
    
    输入两个单调递增的链表，输出两个链表合成后的链表，
    当然我们需要合成后的链表满足单调不减规则。
    '''

    def merge(self, head1, head2):
        # 短路或
        # 当传入空结点时，head1.val is None
        # 当传入非空节点的next时，最后一个head is None
        if head1 is None or head1.val is None:
            return head2
        elif head2 is None or head2.val is None:  # 短路或
            return head1

        head = None
        if head1.val < head2.val:
            head = head1
            head.next = self.merge(head1.next, head2)
        else:
            head = head2
            head.next = self.merge(head1, head2.next)

        return head

    '''
    36-两个链表的第一个公共节点
    
    输入两个链表，找出它们的第一个公共结点。
    如果两个链表有公共节点，则它们的形状必然是一个Y字形。因为node只有一个next
    长链表先走，实现右对齐,然后同时开始往后走
    '''

    def firstCommonNode(self, head1, head2):
        if head1 is None or head2 is None:
            return None

        p1, p2 = head1, head2
        len1 = len2 = 0
        while p1:
            len1 += 1
            p1 = p1.next

        while p2:
            len2 += 1
            p2 = p2.next

        if len1 > len2:
            while len1 - len2:
                head1 = head1.next
                len1 -= 1
        else:
            while len2 - len1:
                head2 = head2.next
                len2 -= 1

        while head1 and head2:
            if head1 is head2:
                return head1
            head1 = head1.next
            head2 = head2.next

        return None

    '''
    55-链表中环的入口
    
    一个链表中包含环，请找出该链表的环的入口结点。
    '''

    def entryNode(self, head):
        if not head:
            return None

        '''
        如果能找到环的长度k，使用双指针法，
        一个从第k个结点出发，一个从head出发，相遇点即为环的入口
        
        使用双指针，一个每次走一步，一个每次走两步，当两个结点相遇时，记录相遇结点
        从相遇点出发，每次一步记录步数，再次回到相遇点时，即走过了一圈，得到环的长度
        '''
        slow = head.next
        if not slow:
            return None

        fast = slow.next

        # 双指针找到相遇点
        while fast is not slow:
            slow = slow.next
            fast = fast.next.next
        meet_node = slow

        # 环的长度
        length = 1
        flag = meet_node
        while flag.next is not meet_node:
            length += 1
            flag = flag.next

        # 双指针找到起始点
        p1 = head
        for i in range(length):
            p1 = p1.next
        p2 = head
        while p1 is not p2:
            p1 = p1.next
            p2 = p2.next
        return p2

    '''
    56-删除链表中重复的结点
    
    删除链表中重复的结点
    在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
    例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
    '''

    def delDup(self, head):
        if head is None or head.next is None:
            return head

        first = ListNode()
        first.next = head
        # 最后一个不重复的结点
        non_dup = first
        while head and head.next:
            if head.val == head.next.val:
                val = head.val
                # 直到最后一个重复结点
                while head and val == head.val:
                    head = head.next
                non_dup.next = head
            else:
                non_dup = head
                head = head.next
        return first.next


node1 = ListNode(9)
node2 = ListNode(11)
node3 = ListNode(13)
node4 = ListNode(14)
node1.next = node2
node2.next = node3
node3.next = node4  # 多元素链表

node5 = ListNode(9)
node6 = ListNode(11)
node7 = ListNode(13)
node5.next = node6
node6.next = node7

node8 = ListNode(10)
node9 = ListNode(12)
node10 = ListNode(14)
node8.next = node9
node9.next = node10

# 包含环的链表
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n3

singleNode = ListNode(10)  # 单元素链表
test = ListNode()  # 空链表

s = LinkedList()
print('\nreverseTraversal')
print(s.reverseTraversal(node1))
print(s.reverseTraversal(test))
print(s.reverseTraversal(singleNode))

print('\nfindKthToTail')
print(s.findKthToTail(node1, 2))
print(s.findKthToTail(test, 2))
print(s.findKthToTail(singleNode, 2))

print('\nreverseList')
print(s.reverseList(node1).val)
print(s.reverseList(test).val)
print(s.reverseList(singleNode).val)

print('\nmerge')
ss = s.merge(node5, node8)
print(ss.val)
print(ss.next.val)
print(ss.next.next.val)
print(ss.next.next.next.val)
print(ss.next.next.next.next.val)
print(ss.next.next.next.next.next.val)

ss = s.merge(test, node5)
print('\n', ss.val)
print(ss.next.val)
print(ss.next.next.val)

ss = s.merge(singleNode, node5)
print('\n', ss.val)
print(ss.next.val)
print(ss.next.next.val)
print(ss.next.next.next.val)
print(ss.next.next.next.next.val)

print('\nentryNode')
print(s.entryNode(n1).val)


n1 = ListNode(1)
n2 = ListNode(1)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
print('\ndelDup')
print(s.delDup(n1).val)
print(s.delDup(n1).next.val)
print(s.delDup(n1).next.next.val)
