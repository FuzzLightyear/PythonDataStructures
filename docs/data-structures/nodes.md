# Nodes

Nodes are the fundamental building blocks of linked data structures. This module provides professionally implemented node classes that serve as the foundation for more complex data structures like linked lists, trees, and graphs.

## Overview

A node is a basic unit that contains:

1. **Data/Value**: The actual information stored in the node
2. **References**: Pointers to other nodes (e.g., next, previous, children)

## DirectedNode

The `DirectedNode` class implements a singly-linked node structure where each node points to at most one next node.

### Features

- ✅ Type-safe with comprehensive type hints
- ✅ Professional NumPy-style documentation
- ✅ Value validation (prevents `None` values)
- ✅ Equality comparison based on values
- ✅ Clean string representation

### Basic Usage

```python
from pythondatastructures.nodes import DirectedNode

# Create a node
node = DirectedNode(42)
print(node.value)  # 42
print(node.next)   # None
```

### Attributes

#### `value: Any`

The data stored in the node. Can be any type except `None`.

```python
node1 = DirectedNode(10)         # Integer
node2 = DirectedNode("hello")    # String
node3 = DirectedNode([1, 2, 3])  # List
node4 = DirectedNode({"a": 1})   # Dictionary
```

#### `next: Optional[DirectedNode]`

Reference to the next node in the linked structure. Initially `None`.

```python
node1 = DirectedNode(1)
node2 = DirectedNode(2)

node1.next = node2
print(node1.next.value)  # 2
```

### Methods

#### `__init__(value: Any) -> None`

Creates a new DirectedNode with the given value.

**Parameters:**
- `value`: The value to store (cannot be `None`)

**Raises:**
- `TypeError`: If value is `None`

```python
# Valid
node = DirectedNode(42)

# Invalid - raises TypeError
try:
    invalid = DirectedNode(None)
except TypeError as e:
    print(e)  # "Node value cannot be None"
```

#### `__repr__() -> str`

Returns a string representation of the node.

```python
node = DirectedNode(100)
print(repr(node))  # DirectedNode(100)
print(node)        # DirectedNode(100)
```

#### `__eq__(other: object) -> bool`

Compares nodes based on their values.

```python
node1 = DirectedNode(42)
node2 = DirectedNode(42)
node3 = DirectedNode(99)

print(node1 == node2)  # True (same value)
print(node1 == node3)  # False (different values)
```

**Note:** Equality is based on values, not identity. Two separate nodes with the same value are considered equal.

### Common Patterns

#### Building a Chain

```python
from pythondatastructures.nodes import DirectedNode

def build_chain(values):
    """Build a chain of nodes from a list."""
    if not values:
        return None

    head = DirectedNode(values[0])
    current = head

    for value in values[1:]:
        current.next = DirectedNode(value)
        current = current.next

    return head

# Create a chain: 1 -> 2 -> 3 -> 4 -> 5
head = build_chain([1, 2, 3, 4, 5])
```

#### Traversing a Chain

```python
def traverse(head):
    """Print all values in a chain."""
    current = head
    while current:
        print(current.value)
        current = current.next

traverse(head)
# Output:
# 1
# 2
# 3
# 4
# 5
```

#### Finding a Value

```python
def find(head, target):
    """Find a node with the given value."""
    current = head
    while current:
        if current.value == target:
            return current
        current = current.next
    return None

# Find node with value 3
node = find(head, 3)
if node:
    print(f"Found: {node.value}")
```

#### Calculating Length

```python
def length(head):
    """Calculate the length of a chain."""
    count = 0
    current = head
    while current:
        count += 1
        current = current.next
    return count

chain = build_chain([10, 20, 30])
print(length(chain))  # 3
```

#### Inserting After a Node

```python
def insert_after(node, new_value):
    """Insert a new node after the given node."""
    new_node = DirectedNode(new_value)
    new_node.next = node.next
    node.next = new_node

head = build_chain([1, 2, 4])
second_node = head.next

# Insert 3 between 2 and 4
insert_after(second_node, 3)
# Chain is now: 1 -> 2 -> 3 -> 4
```

#### Removing After a Node

```python
def remove_after(node):
    """Remove the node after the given node."""
    if node.next:
        node.next = node.next.next

head = build_chain([1, 2, 3, 4])
first_node = head

# Remove second node (value 2)
remove_after(first_node)
# Chain is now: 1 -> 3 -> 4
```

#### Reversing a Chain

```python
def reverse(head):
    """Reverse a chain of nodes."""
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev

head = build_chain([1, 2, 3, 4, 5])
reversed_head = reverse(head)
traverse(reversed_head)
# Output:
# 5
# 4
# 3
# 2
# 1
```

#### Detecting Cycles

```python
def has_cycle(head):
    """Detect if a chain has a cycle using Floyd's algorithm."""
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False

# Normal chain
head = build_chain([1, 2, 3, 4])
print(has_cycle(head))  # False

# Create a cycle
head.next.next.next.next = head.next
print(has_cycle(head))  # True
```

## Performance Characteristics

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Create node | O(1) | O(1) |
| Access value | O(1) | O(1) |
| Set next | O(1) | O(1) |
| Equality check | O(1) | O(1) |

**Note**: These complexities are for individual node operations. Traversal operations on chains have O(n) time complexity.

## Design Decisions

### Why No `None` Values?

Nodes explicitly reject `None` as a value to avoid confusion between:
- An uninitialized node
- A node with no next reference
- A node containing the value `None`

This makes the API clearer and prevents subtle bugs.

### Why Value-Based Equality?

Nodes compare based on values rather than identity because:
1. It's more intuitive for most use cases
2. It allows for easy testing and validation
3. It supports algorithms that search for specific values

If you need identity comparison, use `is`:

```python
node1 = DirectedNode(42)
node2 = DirectedNode(42)

print(node1 == node2)  # True (equal values)
print(node1 is node2)  # False (different objects)
```

## Future Methods

The `DirectedNode` class includes placeholder methods for future implementation:

- `insert()`: Insert a node at a relative index
- `append()`: Append a node at the end
- `pop()`: Remove and return a node at a relative index
- `pop_value()`: Remove and return the first node with a specific value
- `dequeue()`: Remove from front or back (for queue operations)

These methods are currently declared but raise `NotImplementedError`. They will be implemented as part of higher-level data structures.

## See Also

- [Linked Lists](linked-lists.md) - Build on nodes to create full linked list structures
- [API Reference](../api/nodes.md) - Complete API documentation
- [Quick Start](../getting-started/quickstart.md) - Get started with nodes
