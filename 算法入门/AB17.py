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
# @param inorder int整型一维数组 中序遍历序列
# @param postorder int整型一维数组 后序遍历序列
# @return TreeNode类
#
def buildTree(inorder: List[int], postorder: List[int]) -> TreeNode:
        # write code here
        if not inorder or not postorder:
            return None
        root = TreeNode(postorder[-1])
        idx = inorder.index(postorder[-1])
        root.left = buildTree(inorder[:idx], postorder[:idx])
        root.right = buildTree(inorder[idx + 1:], postorder[idx: -1])
        return root
        

print(buildTree([2,1,4,3,5],[2,4,5,3,1]))