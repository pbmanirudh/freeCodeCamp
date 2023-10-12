class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

   def in_order_traversal(node):
     if node is not None:
        in_order_traversal(node.left)
        print(node.value, end=' ')
        in_order_traversal(node.right)

# Example usage:
# Create a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Perform in-order traversal
print("In-order traversal:", end=' ')
in_order_traversal(root)

