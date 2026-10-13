# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 현재 노드 비교 -> 같으면, 왼쪽 자식 비교 -> 같으면, 오른쪽 자식 비교 -> true
        # 하나라도 다르면, false
        
        # 노드 존재 여부 먼저 확인
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        
        return (
            p.val == q.val
            and self.isSameTree(p.left, q.left)
            and self.isSameTree(p.right, q.right)
        )