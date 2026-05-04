"""
01 - Singly Linked List
========================
A complete implementation of a singly linked list with core operations:
insert (head, tail, at index), delete, search, reverse, and display.

Key Concepts:
    - Node-based data structures
    - Pointer manipulation
    - Traversal and reversal algorithms
"""


class Node:
    """Represents a single node in the linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Singly linked list with standard operations."""

    def __init__(self):
        self.head = None
        self.size = 0

    def insert_at_head(self, data):
        """Insert a new node at the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def insert_at_tail(self, data):
        """Insert a new node at the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def insert_at_index(self, index, data):
        """Insert a new node at a specific index (0-based)."""
        if index < 0 or index > self.size:
            raise IndexError(f"Index {index} out of bounds for list of size {self.size}")

        if index == 0:
            self.insert_at_head(data)
            return

        new_node = Node(data)
        current = self.head
        for _ in range(index - 1):
            current = current.next
        new_node.next = current.next
        current.next = new_node
        self.size += 1

    def delete(self, data):
        """Delete the first occurrence of a value from the list."""
        if not self.head:
            print("List is empty.")
            return False

        if self.head.data == data:
            self.head = self.head.next
            self.size -= 1
            return True

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                self.size -= 1
                return True
            current = current.next

        print(f"Value {data} not found in the list.")
        return False

    def search(self, data):
        """Search for a value and return its index, or -1 if not found."""
        current = self.head
        index = 0
        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1
        return -1

    def reverse(self):
        """Reverse the linked list in-place."""
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def display(self):
        """Return a string representation of the list."""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements) + " -> None"

    def __len__(self):
        return self.size

    def __repr__(self):
        return f"LinkedList({self.display()})"


if __name__ == "__main__":
    ll = LinkedList()

    # Build the list
    for val in [10, 20, 30, 40, 50]:
        ll.insert_at_tail(val)
    print(f"Initial list:  {ll.display()}")

    # Insert at head
    ll.insert_at_head(5)
    print(f"After head insert (5):  {ll.display()}")

    # Insert at index
    ll.insert_at_index(3, 25)
    print(f"After insert 25 at index 3:  {ll.display()}")

    # Search
    idx = ll.search(30)
    print(f"Search for 30: found at index {idx}")

    # Delete
    ll.delete(40)
    print(f"After deleting 40:  {ll.display()}")

    # Reverse
    ll.reverse()
    print(f"After reversing:  {ll.display()}")
    print(f"List size: {len(ll)}")
