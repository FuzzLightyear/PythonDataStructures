# Python Data Structures

Welcome to **Python Data Structures** - a comprehensive collection of professionally implemented fundamental data structures in Python.

## Overview

This project provides clean, efficient, and thoroughly documented implementations of essential data structures that every computer scientist and software engineer should know. Each implementation is built from scratch to demonstrate the underlying concepts and mechanics of these fundamental building blocks of computer science.

## Why This Project?

**Python Data Structures** is designed to be:

- **Educational**: Clear, well-documented code that explains not just the "how" but also the "why"
- **Professional**: Modern Python practices with type hints, comprehensive docstrings, and thorough testing
- **Extensible**: Modular design that makes it easy to build upon existing implementations
- **Practical**: Real-world implementations that can be used in production code

## Project Evolution

This project represents years of dedication to mastering Python and software engineering best practices.

!!! info "A Journey of Growth"
    The original implementations in this repository date back to **2020** and represent my early exploration of data structures. Since then, I've spent years tirelessly learning and mastering Python both at work and in my free time. The new implementations showcase this growth with:

    - Modern Python 3.11+ features
    - Comprehensive type annotations
    - Professional documentation standards (NumPy-style docstrings)
    - Thorough test coverage
    - Clean, maintainable architecture

## Current Implementations

### ✅ Available Now

- **Nodes**: Foundation classes for linked data structures
  - `DirectedNode`: Singly-linked node with forward traversal

### 🚧 Coming Soon

The project is actively being expanded with vastly improved implementations of:

- **Linked Lists**: Singly-linked, doubly-linked, and circular variants
- **Stacks**: LIFO data structures with various backing implementations
- **Queues**: FIFO data structures including priority queues
- **Trees**: Binary trees, BSTs, AVL trees, and more
- **Graphs**: Adjacency lists, adjacency matrices, and graph algorithms
- **Hash Tables**: Custom hash table implementations
- **Heaps**: Min-heaps, max-heaps, and heap-based algorithms

## Quick Start

```python
from pythondatastructures.nodes import DirectedNode

# Create a simple linked structure
node1 = DirectedNode(10)
node2 = DirectedNode(20)
node3 = DirectedNode(30)

node1.next = node2
node2.next = node3

# Traverse the structure
current = node1
while current:
    print(current.value)  # Output: 10, 20, 30
    current = current.next
```

## Installation

```bash
# Clone the repository
git clone https://github.com/FuzzLightyear/PythonDataStructures.git
cd PythonDataStructures

# Install with uv (recommended)
uv pip install -e .

# Or with pip
pip install -e .
```

## Contributing

This project welcomes contributions! Whether you're fixing bugs, improving documentation, or proposing new features, your help is appreciated. See the [Contributing Guide](about/contributing.md) for more information.

## License

This project is open source and available for educational and commercial use.

---

<div align="center">
  <p>Built with ❤️ and Python</p>
  <p><strong>From early explorations to professional implementations</strong></p>
</div>
