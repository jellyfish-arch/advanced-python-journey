"""
02 - Stack (LIFO)
==================
Implementation of a Stack data structure with a practical application:
balanced parentheses checker.

Key Concepts:
    - Last-In, First-Out (LIFO) principle
    - Push, Pop, Peek operations
    - Real-world application: expression validation
"""


class Stack:
    """Stack data structure implemented using a Python list."""

    def __init__(self):
        self._items = []

    def push(self, item):
        """Push an item onto the top of the stack."""
        self._items.append(item)

    def pop(self):
        """Remove and return the top item. Raises IndexError if empty."""
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        return self._items.pop()

    def peek(self):
        """Return the top item without removing it."""
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self._items[-1]

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self._items) == 0

    def size(self):
        """Return the number of items in the stack."""
        return len(self._items)

    def __repr__(self):
        return f"Stack({self._items})"


def is_balanced(expression):
    """
    Check if an expression has balanced parentheses, brackets, and braces.

    Args:
        expression: A string containing brackets to validate.

    Returns:
        True if all brackets are properly matched and nested, False otherwise.
    """
    stack = Stack()
    matching = {")": "(", "]": "[", "}": "{"}

    for char in expression:
        if char in "([{":
            stack.push(char)
        elif char in ")]}":
            if stack.is_empty() or stack.pop() != matching[char]:
                return False

    return stack.is_empty()


def reverse_string(text):
    """Reverse a string using a stack."""
    stack = Stack()
    for char in text:
        stack.push(char)

    reversed_chars = []
    while not stack.is_empty():
        reversed_chars.append(stack.pop())

    return "".join(reversed_chars)


if __name__ == "__main__":
    # --- Stack basics ---
    s = Stack()
    for val in [10, 20, 30, 40]:
        s.push(val)
    print(f"Stack: {s}")
    print(f"Peek: {s.peek()}")
    print(f"Pop:  {s.pop()}")
    print(f"After pop: {s}")
    print(f"Size: {s.size()}")

    print("\n--- Balanced Parentheses Checker ---")
    test_expressions = [
        ("({[]})", True),
        ("((()))", True),
        ("({[}])", False),
        ("((()",   False),
        ("",       True),
        ("{[()]}[]{}", True),
    ]
    for expr, expected in test_expressions:
        result = is_balanced(expr)
        status = "✅" if result == expected else "❌"
        print(f"  {status} '{expr}' -> Balanced: {result}")

    print("\n--- Reverse String ---")
    original = "Hello, DSA!"
    print(f"  Original: {original}")
    print(f"  Reversed: {reverse_string(original)}")
