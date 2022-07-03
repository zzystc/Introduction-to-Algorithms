from typing import *

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param root TreeNode类 the root of binary tree
# @return int整型二维数组
#
class Solution:
    def threeOrders(self , root: TreeNode) -> List[List[int]]:
        # write code here
        pre_order, in_order, post_order = [], [], []
        def find(root):
            if not root:
                return None
            pre_order.append(root.val) # 先序：根左右
            find(root.left)
            in_order.append(root.val) # 中序：左根右
            find(root.right)
            post_order.append(root.val) # 后序：左右根
        find(root)
        return [pre_order, in_order, post_order]

test = Solution()
test.threeOrders({1,2,3})
        