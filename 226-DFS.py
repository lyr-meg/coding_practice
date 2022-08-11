# leetcode 226
class Solution:
# allows to annotate parameters with their expected types
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        print(root)
        if root==None: return root
        # depth first search
        self.invertTree(root.left)
        self.invertTree(root.right)
        print('******HERE NOW', root)
        root.right, root.left = root.left, root.right

        return root

# stdout
# TreeNode{val: 4, left: TreeNode{val: 2, left: TreeNode{val: 1, left: None, right: None}, right: TreeNode{val: 3, left: None, right: None}}, right: TreeNode{val: 7, left: TreeNode{val: 6, left: None, right: None}, right: TreeNode{val: 9, left: None, right: None}}}
# TreeNode{val: 2, left: TreeNode{val: 1, left: None, right: None}, right: TreeNode{val: 3, left: None, right: None}}
# TreeNode{val: 1, left: None, right: None}
# None
# None
# ******HERE NOW TreeNode{val: 1, left: None, right: None}
# TreeNode{val: 3, left: None, right: None}
# None
# None
# ******HERE NOW TreeNode{val: 3, left: None, right: None}
# ******HERE NOW TreeNode{val: 2, left: TreeNode{val: 1, left: None, right: None}, right: TreeNode{val: 3, left: None, right: None}}
# TreeNode{val: 7, left: TreeNode{val: 6, left: None, right: None}, right: TreeNode{val: 9, left: None, right: None}}
# TreeNode{val: 6, left: None, right: None}
# None
# None
# ******HERE NOW TreeNode{val: 6, left: None, right: None}
# TreeNode{val: 9, left: None, right: None}
# None
# None
# ******HERE NOW TreeNode{val: 9, left: None, right: None}
# ******HERE NOW TreeNode{val: 7, left: TreeNode{val: 6, left: None, right: None}, right: TreeNode{val: 9, left: None, right: None}}
# ******HERE NOW TreeNode{val: 4, left: TreeNode{val: 2, left: TreeNode{val: 3, left: None, right: None}, right: TreeNode{val: 1, left: None, right: None}}, right: TreeNode{val: 7, left: TreeNode{val: 9, left: None, right: None}, right: TreeNode{val: 6, left: None, right: None}}}
