# Quick Start Guide

Get up and running with Python Data Structures in minutes!

## Your First Node

The `DirectedNode` class is the foundation of linked data structures:

```python
from pythondatastructures.nodes import DirectedNode

# Create a node
node = DirectedNode(42)
print(node.value)  # Output: 42
print(node.next)   # Output: None
```

## Building a Simple Chain

Link nodes together to create a chain:

```python
from pythondatastructures.nodes import DirectedNode

# Create three nodes
first = DirectedNode("A")
second = DirectedNode("B")
third = DirectedNode("C")

# Link them together
first.next = second
second.next = third

# Traverse the chain
current = first
while current:
    print(current.value)
    current = current.next

# Output:
# A
# B
# C
```

## Node Equality

Nodes can be compared based on their values:

```python
from pythondatastructures.nodes import DirectedNode

node1 = DirectedNode(100)
node2 = DirectedNode(100)
node3 = DirectedNode(200)

print(node1 == node2)  # True (same value)
print(node1 == node3)  # False (different values)
```

## Type Safety

The library uses type hints for better IDE support and type checking:

```python
from pythondatastructures.nodes import DirectedNode
from typing import Optional

def find_value(head: DirectedNode, target: int) -> Optional[DirectedNode]:
    """Find a node with the given value."""
    current = head
    while current:
        if current.value == target:
            return current
        current = current.next
    return None

# Use the function
head = DirectedNode(1)
head.next = DirectedNode(2)
head.next.next = DirectedNode(3)

result = find_value(head, 2)
if result:
    print(f"Found: {result.value}")
```

## Error Handling

The library validates inputs and provides clear error messages:

```python
from pythondatastructures.nodes import DirectedNode

# This will raise a TypeError
try:
    invalid_node = DirectedNode(None)
except TypeError as e:
    print(e)  # Output: Node value cannot be None
```

## Next Steps

Now that you've learned the basics, explore more:

### Learn About Data Structures
- [Linked Lists](../data-structures/linked-lists.md)
- [Nodes Documentation](../data-structures/nodes.md)

### Dive Into the API
- [Node API Reference](../api/nodes.md)
- [Full API Documentation](../api/index.md)

### Advanced Topics

As more data structures are implemented, you'll be able to:

- Build stacks and queues
- Implement tree traversals
- Create graph algorithms
- Optimize with advanced data structures

## Common Patterns

### Creating a Linked List from a Python List

```python
from pythondatastructures.nodes import DirectedNode
from typing import Optional

def create_chain(values: list) -> Optional[DirectedNode]:
    """Create a linked chain from a list of values."""
    if not values:
        return None

    head = DirectedNode(values[0])
    current = head

    for value in values[1:]:
        current.next = DirectedNode(value)
        current = current.next

    return head

# Create a chain
chain = create_chain([1, 2, 3, 4, 5])
```

### Converting a Chain Back to a List

```python
def chain_to_list(head: Optional[DirectedNode]) -> list:
    """Convert a linked chain to a Python list."""
    result = []
    current = head
    while current:
        result.append(current.value)
        current = current.next
    return result

# Convert back
values = chain_to_list(chain)
print(values)  # Output: [1, 2, 3, 4, 5]
```

## Need Help?

- Check the [API Reference](../api/index.md) for detailed documentation
- Read about specific [data structures](../data-structures/index.md)
- View [examples and patterns](../data-structures/nodes.md)
- Open an issue on [GitHub](https://github.com/FuzzLightyear/PythonDataStructures/issues)
