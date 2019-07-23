# 声明二叉树节点
# 首先应该先声明一个二叉树结点，包括它的元素及左右子结点

class BiNode(object):
    def __init__(self, element=None, left=None, right=None):
        """
        :param element: 元素
        :param left:  左子节点
        :param right:  右子节点
        """
        self.element = element
        self.left = left
        self.right = right
        self.ret = []

    def get_element(self):
        return self.element

    """
    将节点以字典的形式呈现
    """

    def dict_form(self):
        dict_set = {
            "element": self.element,
            "left": self.left,
            "right": self.right
        }

        return dict_set

    def __str__(self):
        return str(self.element)


# 初始化二叉树
class BiTree:
    def __init__(self, tree_node=BiNode):
        self.root = tree_node

    # 顺序构造二叉树，从上到下，从左到右
    def add_node_in_order(self, element):
        """
        判断根结点是否存在，如果不存在则插入根结点。
        否则从根结点开始
        判断左子结点是否存在，如果不存在插入,
        如果左子结点存在判断右结点，不存在插入。
        如果左右结点存在，再依次遍历左右子结点的子结点，直到插入成功。
        """
        node = BiNode(element)

        if self.root is None:
            self.root = node
        else:
            node_queue = list()
            node_queue.append(self.root)
            while len(node_queue):
                q_node = node_queue.pop(0)
                if q_node.left is None:
                    q_node.left = node
                    break
                elif q_node.right is None:
                    q_node.right = node
                    break
                else:
                    node_queue.append(q_node.left)
                    node_queue.append(q_node.right)

    '''
    dict_tree = {
        "element": 0,
        "left": {
            "element": 1,
            "left": {
                "element": 3,
                "left": 6,
                "right": 7,
            }
        },
        "right": {
            "element": 2,
            "left": 4,
            "right": {
                "element": 5,
                "left": 8,
                "right": 9,
            },
        },
    }
    '''

    # 从字典构造二叉树
    def set_up_from_dict(self, dict_instance):
        if not isinstance(dict_instance, dict):
            return None
        else:
            dict_queue = list()
            node_queue = list()
            # 根节点
            node = BiNode(dict_instance["element"])
            self.root = node
            node_queue.append(node)
            dict_queue.append(dict_instance)

            while len(dict_queue):
                dict_in = dict_queue.pop(0)
                node = node_queue.pop(0)

                if isinstance(dict_in.get("left", None), (dict, int, float, str)):
                    if isinstance(dict_in.get("left", None), dict):
                        dict_queue.append(dict_in.get("left", None))
                        left_node = BiNode(dict_in.get("left", None)["element"])
                        node_queue.append(left_node)
                    else:
                        left_node = BiNode(dict_in.get("left", None))
                    node.left = left_node

                if isinstance(dict_in.get("right", None), (dict, int, float, str)):
                    if isinstance(dict_in.get("right", None), dict):
                        dict_queue.append(dict_in.get("right", None))
                        right_node = BiNode(dict_in.get("right", None)["element"])
                        node_queue.append(right_node)
                    else:
                        right_node = BiNode(dict_in.get("right", None))
                    node.right = right_node

    # 将二叉树转为字典
    def pack_to_dict(self):
        if self.root is None:
            return None
        else:
            node_queue = list()
            dict_queue = list()
            node_queue.append(self.root)
            dict_pack = self.root.dict_form()
            dict_queue.append(dict_pack)

            while len(node_queue):
                q_node = node_queue.pop(0)
                dict_get = dict_queue.pop(0)
                if q_node.left is not None:
                    node_queue.append(q_node.left)
                    dict_get["left"] = q_node.left.dict_form()
                    dict_queue.append(dict_get["left"])
                if q_node.right is not None:
                    node_queue.append(q_node.right)
                    dict_get["right"] = q_node.right.dict_form()
                    dict_queue.append(dict_get["right"])
        return dict_pack

    # 求二叉树的深度
    # 1.如果树为空，返回0 。
    # 2.从根结点开始，将根结点拉入列。
    # 3.当列非空，记当前队列元素数（上一层节点数）。
    # 将上层节点依次出队，如果左右结点存在，依次入队。
    # 直至上层节点出队完成，深度加一。
    # 继续第三步，直至队列完全为空。
    def get_depth(self):
        if self.root is None:
            return 0
        else:
            node_queue = list()
            node_queue.append(self.root)
            depth = 0
            while len(node_queue):
                q_len = len(node_queue)
                while len(q_len):
                    q_node = node_queue.pop(0)
                    q_len = q_len - 1
                    if q_node.left is not None:
                        node_queue.append(q_node.left)
                    if q_node.right is not None:
                        node_queue.append(q_node.right)
                depth += 1
            return depth

    """
    前序遍历， 方法如下： 

    1. 如果树为空，返回None 。 
    2. 从根结点开始，如果当前结点左子树存在，则打印结点，并将该结点入栈。让当前结点指向左子树，继续步骤2直至当前结点左子树不存在。 
    3. 将当结点打印出来，如果当前结点的右子树存在，当前结点指向右子树，继续步骤2。否则进行步骤4. 
    4. 如果栈为空则遍历结束。若非空，从栈里面pop一个节点，从当前结点指向该结点的右子树。如果右子树存在继续步骤2，不存在继续步骤4直至结束。 
    """

    # 前序遍历（迭代）
    def pre_traversal(self):
        """method of traversing BiTree in pre-order"""
        if self.root is None:
            return None
        else:
            node_stack = list()
            output_list = list()
            node = self.root
            while node is not None or len(node_stack):
                # if node is None which means it comes from a leaf-node' right,
                # pop the stack and get it's right node.
                # continue the circulating like this
                if node is None:
                    node = node_stack.pop().right
                    continue
                #  save the front node and go next when left node exists
                while node.left is not None:
                    node_stack.append(node)
                    output_list.append(node.get_element())
                    node = node.left
                output_list.append(node.get_element())
                node = node.right
        return output_list

    """
    中序遍历的思想基本与前序遍历一样，只是最开始结点入栈时先不打印。
    只打印不存在左子树的当前结点，然后再出栈遍历右子树前再打印出来
    """

    # 中序遍历（迭代）
    def in_traversal(self):
        """method of traversing BiTree in in-order"""
        if self.root is None:
            return None
        else:
            node_stack = list()
            output_list = list()
            node = self.root
            while node is not None or len(node_stack):
                # if node is None which means it comes from a leaf-node' right,
                # pop the stack and get it's right node.
                # continue the circulating like this
                if node is None:
                    node = node_stack.pop()
                    # in in-order traversal, when pop up a node from stack , save it
                    output_list.append(node.get_element())
                    node = node.right
                    continue
                # go-next when left node exists
                while node.left is not None:
                    node_stack.append(node)
                    node = node.left
                # save the the last left node
                output_list.append(node.get_element())
                node = node.right
        return output_list

    # 后序遍历（迭代）
    def post_traversal(self):
        """method of traversing BiTree in post-order"""
        if self.root is None:
            return None
        else:
            node_stack = list()
            output_list = list()
            node = self.root
            while node is not None or len(node_stack):
                # if node is None which means it comes from a leaf-node' left,
                # pop the stack and get it's left node.
                # continue the circulating like this
                if node is None:
                    node = node_stack.pop().left
                    continue
                while node.right is not None:
                    node_stack.append(node)
                    output_list.append(node.get_element())
                    node = node.right
                output_list.append(node.get_element())
                node = node.left
        return output_list[::-1]

    # 翻转二叉树（迭代）
    def inverse_tree(self, root):
        if root is None:
            return root

        queue = []
        queue.append(root)

        while queue:
            next_queue = []
            for node in queue:
                node.left, node.right = node.right, node.left
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            queue = next_queue
        return root

    # 前序遍历（递归）
    def preorderTraversal(self, root):
        if root is not None:
            self.ret.append(root.val)
            self.preorderTraversal(root.left)
            self.preorderTraversal(root.right)
        return self.ret

    # 中序遍历（递归）
    def inTraversal(self, root):
        if root is not None:
            self.inTraversal(root.left)
            self.ret.append(root.val)
            self.inTraversal(root.right)
        return self.ret

    # 后续遍历（递归）
    def postTraversal(self, root):
        if root is not None:
            self.postTraversal(root.left)
            self.postTraversal(root.right)
            self.ret.append(root.val)
        return self.ret

    # 广度优先，层次遍历
    def levelTraversal(self, root):
        res = []
        if root == None:
            return res

        l = []
        l.append(root)
        while len(l) > 0:
            temp = []
            for i in range(len(l)):
                node = l[0]
                del l[0]
                temp.apped(node.left)
                if node.left:
                    l.append(node.left)
                if node.right:
                    l.append(node.right)
            res.append(temp)
        return res

    # 求叶子节点
    """
    求叶子节点有两种方法
    一种是广度搜索优先
    即如果当前节点存在左右子树将左右子树入队
    如果当前节点不存在子树，则该节点为叶节点
    继续出队访问下一个节点。直至队列为空，这个方法留给读者去实现。

    另外一种方法是，用深度搜索优先。
    采用前序遍历，当判断到一个结点不存在左右子树时叶子结点数加一。
    """

    def get_leaf_num(self):
        """method of getting leaf numbers of BiTree"""
        if self.root is None:
            return 0
        else:
            node_stack = list()
            node = self.root
            leaf_numbers = 0
            # only node exists and stack is not empty that will do this circulation
            while node is not None or len(node_stack):
                if node is None:
                    """node is None then pop the stack and get the node.right"""
                    node = node_stack.pop().right
                    continue
                while node.left is not None:
                    node_stack.append(node)
                    node = node.left
                # if there is not  node.right, leaf_number add 1
                node = node.right
                if node is None:
                    leaf_numbers += 1
            return leaf_numbers

    # 两个节点的最近公共祖先
    def lowestCommonAncestor(self, root, p, q):
        if root is None or root == p or root == q:
            return root
        # 如果两个节点分别在左右子树上，返回根节点
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        return root if l and r else l or r

    # 二叉树最小深度
    def minDepth(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1

        if not root.left or not root.right:
            #  左子结点或右子结点存在，不存在的那一边就为0 了，选另一边 
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1
        else:
            #  左右子结点都存在，选更浅的子树 
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

    # 二叉树的最大深度
    def maxDepth(self, root):
        if root is None:
            return 0

        ltree = self.maxDepth(root.left)
        rtree = self.maxDepth(root.right)

        return max(ltree, rtree) + 1

    """
    二叉搜索树(Binary Search Tree)，又名二叉排序树(Binary Sort Tree)。
  二叉搜索树是具有有以下性质的二叉树：
  （1）若左子树不为空，则左子树上所有节点的值均小于或等于它的根节点的值。
  （2）若右子树不为空，则右子树上所有节点的值均大于或等于它的根节点的值。
  （3）左、右子树也分别为二叉搜索树。
    """

    # 二叉搜索树的最小值
    def findMin(self, root):
        if root.left:
            return self.findMin(self.left)
        else:
            return root

    # 二叉搜索树的最大值
    def findMax(self, root):
        if root.right:
            return self.findMax(root.right)
        else:
            return root

    # 查找节点是否在二叉搜索树中
    def query(self, root, val):
        if not root:
            return False

        if root.val == val:
            return True

        if val < root.val:
            return self.query(root.left, val)
        elif val > root.val:
            return self.query(root.right, val)
