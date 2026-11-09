from typing import Optional,List

class TreeNode:
    def __init__(self,val:int):
        self.val = val
        self.left:Optional['TreeNode'] = None
        self.right:Optional['TreeNode'] = None


class TwoTree:
    def __init__(self,root:Optional[TreeNode]=None):
        self.root = root

    def insert(self,val:int):
        if not self.root:
            self.root = TreeNode(val)
            return
        self._insert(self.root,val)

    def _insert(self,node:TreeNode,val:int) -> TreeNode:
        if not node:
            return TreeNode(val)
        if val < node.val:
            node.left = self._insert(node.left,val)
        else:
            node.right = self._insert(node.right,val)
        return node