# API Reference

Complete API documentation for Python Data Structures.

## Overview

This section provides detailed API documentation for all modules, classes, and functions in the library. The documentation is automatically generated from the source code docstrings.

## Available Modules

### Core Modules

#### [Nodes](nodes.md)
Foundation classes for linked data structures.

- `DirectedNode`: Singly-linked node implementation

#### [Linked Lists](linkedlist.md) 🚧
Linked list implementations (coming soon).

- `SinglyLinkedList`: Basic linked list
- `DoublyLinkedList`: Bi-directional linked list
- `CircularLinkedList`: Circular linked list

## Using the API Documentation

Each module page includes:

- **Class definitions**: Complete class documentation with all methods
- **Method signatures**: Full type-annotated signatures
- **Parameters**: Detailed parameter descriptions
- **Return values**: What each method returns
- **Raises**: What exceptions can be raised
- **Examples**: Code examples showing usage
- **Notes**: Additional implementation details

## Quick Navigation

### By Category

**Data Structures**:
- [Nodes](nodes.md)
- [Linked Lists](linkedlist.md)

**Utilities** (Coming Soon):
- Iterators
- Comparators
- Validators

**Algorithms** (Coming Soon):
- Sorting algorithms
- Search algorithms
- Graph algorithms

### By Use Case

**Building Linear Structures**:
- Start with [DirectedNode](nodes.md#directednode)
- Build [Linked Lists](linkedlist.md)

**Implementing Stacks/Queues** (Coming Soon):
- Use linked list foundation
- Apply LIFO/FIFO operations

**Tree Operations** (Coming Soon):
- Tree node structures
- Traversal algorithms

## Code Examples

### Working with Nodes

```python
from pythondatastructures.nodes import DirectedNode

# Create and link nodes
head = DirectedNode(1)
head.next = DirectedNode(2)
head.next.next = DirectedNode(3)
```

See the [Nodes API reference](nodes.md) for complete documentation.

### Type Hints

All APIs use comprehensive type hints:

```python
from typing import Any, Optional
from pythondatastructures.nodes import DirectedNode

def process_chain(head: Optional[DirectedNode]) -> list[Any]:
    """Process a chain and return all values."""
    result = []
    current = head
    while current:
        result.append(current.value)
        current = current.next
    return result
```

## Docstring Format

All documentation follows the NumPy docstring style:

```python
def example_function(param1: int, param2: str) -> bool:
    """Brief one-line description.

    Longer description providing more context about what
    the function does and how to use it.

    Parameters
    ----------
    param1 : int
        Description of param1.
    param2 : str
        Description of param2.

    Returns
    -------
    bool
        Description of return value.

    Raises
    ------
    ValueError
        When parameter validation fails.

    Examples
    --------
    >>> example_function(42, "hello")
    True

    Notes
    -----
    Additional implementation details or complexity analysis.
    """
    ...
```

## Performance Documentation

Time and space complexity is documented where relevant:

- Big-O notation for time complexity
- Space complexity analysis
- Best, average, and worst-case scenarios
- Practical performance considerations

## Version Compatibility

**Python Version**: 3.11+

The library uses modern Python features:
- Type hints (PEP 484)
- Type unions with `|` syntax (PEP 604)
- Match statements (PEP 634) where applicable
- Structural pattern matching

## Getting Help

- For conceptual guides, see [Data Structures](../data-structures/index.md)
- For quick examples, see [Quick Start](../getting-started/quickstart.md)
- For installation help, see [Installation](../getting-started/installation.md)
- For issues or questions, visit [GitHub Issues](https://github.com/FuzzLightyear/PythonDataStructures/issues)
