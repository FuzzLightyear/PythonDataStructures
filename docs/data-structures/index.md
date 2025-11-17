# Data Structures Overview

This page provides an overview of all data structures implemented in this library, their use cases, and performance characteristics.

## Available Structures

### Nodes

**Status**: ✅ Implemented

Nodes are the fundamental building blocks for linked data structures. They store a value and references to other nodes.

- **DirectedNode**: A singly-linked node that references the next node in a sequence
- **Use Cases**: Foundations for linked lists, stacks, queues, and trees
- **Time Complexity**: O(1) for attribute access
- **Space Complexity**: O(1) per node

[Learn more about Nodes →](nodes.md){ .md-button }

## Coming Soon

### Linked Lists

**Status**: 🚧 In Development

Linked lists are linear data structures where elements are stored in nodes that point to the next node in the sequence.

**Planned Implementations**:

- **Singly Linked List**: Each node points to the next node
  - Efficient insertion/deletion at head: O(1)
  - Sequential access: O(n)

- **Doubly Linked List**: Nodes point to both next and previous nodes
  - Bi-directional traversal
  - Efficient insertion/deletion at both ends: O(1)

- **Circular Linked List**: Last node points back to the first
  - Useful for round-robin scheduling
  - Continuous traversal

[Learn more about Linked Lists →](linked-lists.md){ .md-button }

### Stacks

**Status**: 🔜 Planned

A Last-In-First-Out (LIFO) data structure.

**Planned Features**:

- Push/Pop operations: O(1)
- Peek operation: O(1)
- Array-based and linked-list-based implementations
- Applications: Function call stack, undo mechanisms, expression evaluation

### Queues

**Status**: 🔜 Planned

A First-In-First-Out (FIFO) data structure.

**Planned Variants**:

- **Simple Queue**: Basic FIFO operations
- **Circular Queue**: Space-efficient queue using circular buffer
- **Priority Queue**: Elements dequeued based on priority
- **Deque**: Double-ended queue supporting operations at both ends

**Applications**: Task scheduling, BFS traversal, request handling

### Trees

**Status**: 🔜 Planned

Hierarchical data structures with a root node and child nodes.

**Planned Implementations**:

- **Binary Tree**: Each node has at most two children
- **Binary Search Tree (BST)**: Ordered binary tree for efficient searching
- **AVL Tree**: Self-balancing BST with guaranteed O(log n) operations
- **B-Tree**: Self-balancing tree for databases and file systems
- **Trie**: Tree structure for string prefix operations

**Applications**: Hierarchical data, fast searching, autocomplete, routing

### Graphs

**Status**: 🔜 Planned

Structures representing networks of connected nodes.

**Planned Implementations**:

- **Adjacency List**: Memory-efficient sparse graph representation
- **Adjacency Matrix**: Dense graph representation with O(1) edge lookup
- **Directed/Undirected variants**
- **Weighted graph support**

**Classic Algorithms to Include**:

- Depth-First Search (DFS)
- Breadth-First Search (BFS)
- Dijkstra's shortest path
- A* pathfinding
- Minimum spanning tree (Prim's, Kruskal's)

### Hash Tables

**Status**: 🔜 Planned

Key-value data structures with O(1) average-case operations.

**Planned Features**:

- Custom hash functions
- Collision resolution (chaining and open addressing)
- Dynamic resizing
- Load factor management

**Applications**: Caching, counting, lookups, deduplication

### Heaps

**Status**: 🔜 Planned

Complete binary trees satisfying the heap property.

**Planned Implementations**:

- **Min Heap**: Parent is smaller than children
- **Max Heap**: Parent is larger than children
- **Binary Heap**: Array-based implementation
- **Fibonacci Heap**: Advanced heap with better amortized complexity

**Applications**: Priority queues, heap sort, finding k-th largest/smallest elements

## Design Philosophy

All data structures in this library follow these principles:

### 1. **Type Safety**

Modern Python type hints throughout:

```python
def insert(self, value: int, index: int) -> None:
    """Insert a value at the specified index."""
    ...
```

### 2. **Comprehensive Documentation**

NumPy-style docstrings with:

- Clear parameter descriptions
- Return value documentation
- Examples and use cases
- Time and space complexity notes

### 3. **Thorough Testing**

Every data structure includes:

- Unit tests for all operations
- Edge case testing
- Performance benchmarks
- Property-based testing where appropriate

### 4. **Clean Architecture**

- Single responsibility principle
- Composition over inheritance
- Clear separation of concerns
- Extensible design

## Performance Comparison

Here's a quick reference for common operations:

| Data Structure | Access | Search | Insertion | Deletion | Space |
|---------------|--------|--------|-----------|----------|-------|
| Array/List | O(1) | O(n) | O(n) | O(n) | O(n) |
| Linked List | O(n) | O(n) | O(1)* | O(1)* | O(n) |
| Stack | O(n) | O(n) | O(1) | O(1) | O(n) |
| Queue | O(n) | O(n) | O(1) | O(1) | O(n) |
| Hash Table | O(1)† | O(1)† | O(1)† | O(1)† | O(n) |
| BST | O(log n)‡ | O(log n)‡ | O(log n)‡ | O(log n)‡ | O(n) |
| AVL Tree | O(log n) | O(log n) | O(log n) | O(log n) | O(n) |
| Binary Heap | O(1)§ | O(n) | O(log n) | O(log n) | O(n) |

*With pointer to insertion/deletion point
†Average case; O(n) worst case
‡Balanced tree; O(n) worst case for unbalanced
§For min/max element only

## Roadmap

The project is actively being developed with the following priorities:

1. **Phase 1** (Current): Nodes and foundational components
2. **Phase 2** (Next): Linked lists with comprehensive variants
3. **Phase 3**: Stacks and queues
4. **Phase 4**: Tree structures
5. **Phase 5**: Graph structures and algorithms
6. **Phase 6**: Hash tables and heaps

Each phase includes:

- Implementation
- Comprehensive testing
- Documentation
- Performance benchmarking
- Example use cases

## Contributing

Want to help implement these data structures? Check out the [Contributing Guide](../about/contributing.md) to get started!
