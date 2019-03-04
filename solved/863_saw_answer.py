# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        def getParentMap(root, parents):
            if root.left:
                parents[root.left] = root
                getParentMap(root.left, parents)
            if root.right:
                parents[root.right] = root
                getParentMap(root.right, parents)
        def dfs(node, parents, K, res, visited):
            if node in visited:
                return
            visited.add(node)
            if K == 0:
                res.append(node.val)
                return
            if node.left != None:
                dfs(node.left, parents, K-1, res, visited)
            if node.right != None:
                dfs(node.right, parents, K-1, res, visited)
            if parents[node] != None:
                dfs(parents[node], parents, K-1, res, visited)
        parentMap = {}
        parentMap[root] = None
        getParentMap(root, parents)
        res = []
        visited = set()
        dfs(target, parentMap, K, res, visited)
        return res


