"""
04 - Binary Search Tree (BST)
==============================
A complete BST implementation with insert, search, delete, and
four traversal strategies (in-order, pre-order, post-order, level-order).

Key Concepts:
    - Tree data structure fundamentals
    - Recursive insertion and search
    - Node deletion (three cases)
    - Depth-first and breadth-first traversals
"""

from collections import deque


class TreeNode:
    """Represents a single node in the BST."""

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    """Binary Search Tree with standard operations."""

    def __init__(self):
        self.root = None

    def insert(self, key):
        """Insert a key into the BST."""
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return TreeNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        # Duplicate keys are ignored
        return node

    def search(self, key):
        """Search for a key in the BST. Returns True if found."""
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def delete(self, key):
        """Delete a key from the BST."""
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return None

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # Case 1: Leaf node or single child
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            # Case 2: Two children — replace with in-order successor
            successor = self._find_min(node.right)
            node.key = successor.key
            node.right = self._delete(node.right, successor.key)

        return node

    def _find_min(self, node):
        """Find the node with the smallest key in a subtree."""
        while node.left:
            node = node.left
        return node

    # --- Traversals ---

    def inorder(self):
        """In-order traversal (sorted order)."""
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.key)
            self._inorder(node.right, result)

    def preorder(self):
        """Pre-order traversal (root first)."""
        result = []
        self._preorder(self.root, result)
        return result

    def _preorder(self, node, result):
        if node:
            result.append(node.key)
            self._preorder(node.left, result)
            self._preorder(node.right, result)

    def postorder(self):
        """Post-order traversal (root last)."""
        result = []
        self._postorder(self.root, result)
        return result

    def _postorder(self, node, result):
        if node:
            self._postorder(node.left, result)
            self._postorder(node.right, result)
            result.append(node.key)

    def level_order(self):
        """Level-order (breadth-first) traversal."""
        if not self.root:
            return []

        result = []
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            result.append(node.key)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

    def height(self):
        """Calculate the height of the tree."""
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return -1
        return 1 + max(self._height(node.left), self._height(node.right))


if __name__ == "__main__":
    bst = BinarySearchTree()

    # Build the tree
    values = [50, 30, 70, 20, 40, 60, 80]
    for v in values:
        bst.insert(v)

    print("--- Binary Search Tree ---")
    print(f"In-order:    {bst.inorder()}")
    print(f"Pre-order:   {bst.preorder()}")
    print(f"Post-order:  {bst.postorder()}")
    print(f"Level-order: {bst.level_order()}")
    print(f"Height:      {bst.height()}")

    # Search
    print(f"\nSearch 40: {bst.search(40)}")
    print(f"Search 99: {bst.search(99)}")

    # Delete
    bst.delete(30)
    print(f"\nAfter deleting 30:")
    print(f"In-order:    {bst.inorder()}")
    print(f"Level-order: {bst.level_order()}")
