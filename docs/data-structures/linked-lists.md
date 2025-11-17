# Linked Lists

**Status**: 🚧 In Development

Linked lists are linear data structures where elements are stored in nodes, and each node points to the next node in the sequence. Unlike arrays, linked lists don't require contiguous memory and can grow or shrink dynamically.

## Overview

A linked list consists of nodes where each node contains:

1. **Data**: The value stored in the node
2. **Pointer(s)**: Reference(s) to other nodes in the structure

## Coming Soon

This project will include professional implementations of various linked list types with modern Python practices.

### Singly Linked List

Each node points to the next node in the sequence.

**Planned Features:**

- Dynamic insertion and deletion
- O(1) head insertion
- O(1) head deletion
- Traversal operations
- Search functionality
- Reversal algorithm

**Example Usage (Planned):**

```python
from pythondatastructures.linkedlist import SinglyLinkedList

# Create a list
lst = SinglyLinkedList()

# Add elements
lst.append(10)
lst.append(20)
lst.append(30)

# Insert at specific position
lst.insert(1, 15)  # [10, 15, 20, 30]

# Search
node = lst.find(20)

# Remove
lst.remove(15)  # [10, 20, 30]
```

### Doubly Linked List

Each node points to both the next and previous nodes.

**Planned Features:**

- Bi-directional traversal
- O(1) insertion at both ends
- O(1) deletion at both ends
- Efficient reverse operations
- Better deletion performance (can access previous node)

**Example Usage (Planned):**

```python
from pythondatastructures.linkedlist import DoublyLinkedList

# Create a list
lst = DoublyLinkedList()

# Add elements
lst.append(1)
lst.append(2)
lst.prepend(0)  # [0, 1, 2]

# Traverse backwards
for value in lst.reverse_iter():
    print(value)  # 2, 1, 0
```

### Circular Linked List

The last node points back to the first node, creating a circle.

**Planned Features:**

- Continuous traversal
- Useful for round-robin scheduling
- No null references to handle
- Efficient for cyclic data

**Example Usage (Planned):**

```python
from pythondatastructures.linkedlist import CircularLinkedList

# Create a circular list for round-robin
players = CircularLinkedList(["Alice", "Bob", "Charlie"])

# Rotate through players infinitely
current = players.head
for _ in range(10):
    print(current.value)
    current = current.next  # Never becomes None!
```

## Advantages Over Arrays

| Feature | Linked List | Array |
|---------|-------------|-------|
| Dynamic size | ✅ Easy | ❌ Expensive resize |
| Insertion at start | ✅ O(1) | ❌ O(n) |
| Deletion at start | ✅ O(1) | ❌ O(n) |
| Random access | ❌ O(n) | ✅ O(1) |
| Memory efficiency | ❌ Extra pointers | ✅ Contiguous |
| Cache locality | ❌ Poor | ✅ Excellent |

## Common Use Cases

### When to Use Linked Lists

- **Frequent insertions/deletions at the beginning**: O(1) vs O(n) for arrays
- **Unknown or dynamic size**: No need to pre-allocate space
- **Memory fragmentation**: Can use non-contiguous memory blocks
- **Implementing other structures**: Foundation for stacks, queues, hash tables

### When NOT to Use Linked Lists

- **Need random access**: O(n) to access middle elements
- **Memory constrained**: Extra space for pointers
- **Cache performance critical**: Poor spatial locality
- **Small, fixed-size data**: Array overhead is minimal

## Performance Comparison

### Singly Linked List

| Operation | Time Complexity | Notes |
|-----------|----------------|-------|
| Access by index | O(n) | Must traverse from head |
| Search | O(n) | Linear search required |
| Insert at head | O(1) | Direct pointer manipulation |
| Insert at tail | O(n) | Without tail pointer |
| Insert at tail | O(1) | With tail pointer |
| Delete at head | O(1) | Direct pointer manipulation |
| Delete at tail | O(n) | Must traverse to find previous |
| Delete by value | O(n) | Must search then delete |

### Doubly Linked List

| Operation | Time Complexity | Notes |
|-----------|----------------|-------|
| Access by index | O(n) | Can traverse from nearest end |
| Search | O(n) | Can search from either end |
| Insert at head | O(1) | Update two pointers |
| Insert at tail | O(1) | With tail pointer |
| Delete at head | O(1) | Update two pointers |
| Delete at tail | O(1) | With tail pointer |
| Delete by value | O(n) | Search + O(1) deletion |

## Classic Algorithms

These algorithms will be implemented as part of the linked list module:

### Traversal

```python
def traverse(head):
    """Visit each node in the list."""
    current = head
    while current:
        process(current.value)
        current = current.next
```

### Reversal

```python
def reverse(head):
    """Reverse a singly linked list in-place."""
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev
```

### Cycle Detection (Floyd's Algorithm)

```python
def has_cycle(head):
    """Detect if the list has a cycle."""
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False
```

### Find Middle Element

```python
def find_middle(head):
    """Find the middle element in one pass."""
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow
```

### Merge Two Sorted Lists

```python
def merge_sorted(l1, l2):
    """Merge two sorted linked lists."""
    dummy = DirectedNode(0)
    current = dummy

    while l1 and l2:
        if l1.value <= l2.value:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    current.next = l1 or l2
    return dummy.next
```

## Implementation Roadmap

The linked list implementations will follow this timeline:

### Phase 1: Foundation ✅
- [x] Node structures (`DirectedNode`)
- [x] Basic node operations
- [x] Comprehensive tests for nodes

### Phase 2: Singly Linked List 🚧
- [ ] Core list structure
- [ ] Insertion operations (head, tail, index)
- [ ] Deletion operations (head, tail, value)
- [ ] Search and access methods
- [ ] Iterator support
- [ ] Comprehensive tests

### Phase 3: Doubly Linked List 🔜
- [ ] Bidirectional node structure
- [ ] Enhanced insertion/deletion
- [ ] Reverse iteration
- [ ] Comprehensive tests

### Phase 4: Advanced Features 🔜
- [ ] Circular linked lists
- [ ] Sorted linked lists
- [ ] Skip lists
- [ ] Advanced algorithms

## Learning Resources

Want to understand linked lists better? Check out these concepts:

- **Pointer manipulation**: Understanding references in Python
- **Memory management**: How Python handles object references
- **Time complexity analysis**: Why certain operations are O(1) or O(n)
- **Space-time tradeoffs**: Doubly vs singly linked lists

## From 2020 to Now

This project includes implementations from 2020 in the `old/` directory. Comparing them with the upcoming modern implementations showcases years of growth:

### 2020 Implementation Characteristics

```python
# From old/linkedlist.py
class llnode():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
```

- Basic functionality
- Minimal documentation
- No type hints
- Limited error handling

### Modern Implementation (Coming)

```python
# New implementation style
class SinglyLinkedList:
    """A singly-linked list implementation.

    This class provides a dynamic linear data structure where
    elements are stored in nodes with forward references.
    """

    def __init__(self) -> None:
        """Initialize an empty linked list."""
        self._head: Optional[DirectedNode] = None
        self._tail: Optional[DirectedNode] = None
        self._size: int = 0
```

- Professional architecture
- Comprehensive type hints
- NumPy-style docstrings
- Thorough testing
- Performance optimization

## See Also

- [Nodes Documentation](nodes.md) - Foundation for linked lists
- [Stacks and Queues](index.md) - Built on linked lists
- [API Reference](../api/linkedlist.md) - Detailed API (coming soon)
