class Solution:
    def subtreeWithAllDeepest(self, root)
        return self.subtreeWithAllDeepestHelp(root, 0)[0]
    def subtreeWithAllDeepestHelp(self, node, depth):
        if node == None:
            return (None, None)
        if node.left == None and node.right == None:
            return (node, depth)
        (left_node, left_depth) = self.subtreeWithAllDeepestHelp(node.left, depth+1)
        (right_node, right_depth) = self.subtreeWithAllDeepestHelp(node.right, depth+1)
        if left_depth != None and right_depth != None:
            if left_depth == right_depth:
                return (node, left_depth)
            elif left_depth > right_depth:
                return (left_node, left_depth)
            else: return (right_node, right_depth)
        elif left_depth == None:
            return (right_node, right_depth)
        else: return (left_node, left_depth)
