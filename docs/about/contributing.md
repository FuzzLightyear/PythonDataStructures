# Contributing

Thank you for your interest in contributing to Python Data Structures! This guide will help you get started.

## How to Contribute

There are many ways to contribute to this project:

- 🐛 **Report bugs** and issues
- 💡 **Suggest features** or improvements
- 📝 **Improve documentation**
- 🧪 **Write tests**
- 💻 **Implement data structures**
- 🎨 **Enhance examples**

## Getting Started

### 1. Fork and Clone

```bash
# Fork the repository on GitHub, then:
git clone https://github.com/YOUR_USERNAME/PythonDataStructures.git
cd PythonDataStructures
```

### 2. Set Up Development Environment

```bash
# Install uv (recommended)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies
uv pip install -e ".[dev,docs]"
```

### 3. Create a Branch

```bash
# Create a feature branch
git checkout -b feature/your-feature-name

# Or a bugfix branch
git checkout -b fix/bug-description
```

## Development Guidelines

### Code Style

Follow these Python best practices:

#### Type Hints

Always use type hints:

```python
from typing import Any, Optional

def process_value(value: int, default: Optional[int] = None) -> int:
    """Process a value with an optional default."""
    return value if value is not None else (default or 0)
```

#### Docstrings

Use NumPy-style docstrings:

```python
def example_function(param1: int, param2: str) -> bool:
    """Brief description of the function.

    More detailed description explaining what the function
    does and how to use it.

    Parameters
    ----------
    param1 : int
        Description of param1.
    param2 : str
        Description of param2.

    Returns
    -------
    bool
        Description of what is returned.

    Raises
    ------
    ValueError
        When validation fails.

    Examples
    --------
    >>> example_function(42, "hello")
    True

    Notes
    -----
    Additional implementation notes or complexity analysis.
    """
    ...
```

#### Code Organization

- One class per file (for major classes)
- Group related functionality
- Keep functions focused and single-purpose
- Use meaningful variable names

#### Example: Good Code

```python
from __future__ import annotations

from typing import Any, Optional


class DirectedNode:
    """A singly-linked node with forward traversal.

    Attributes
    ----------
    value : Any
        The value stored in the node.
    next : DirectedNode or None
        Reference to the next node.
    """

    def __init__(self, value: Any) -> None:
        """Initialize a new DirectedNode.

        Parameters
        ----------
        value : Any
            The value to store (cannot be None).

        Raises
        ------
        TypeError
            If value is None.
        """
        if value is None:
            raise TypeError("Node value cannot be None")
        self.value: Any = value
        self.next: Optional[DirectedNode] = None

    def __repr__(self) -> str:
        """Return a string representation."""
        return f"DirectedNode({self.value!r})"
```

### Testing

Write comprehensive tests for all code:

#### Test Structure

```python
import pytest
from pythondatastructures.nodes import DirectedNode


class TestDirectedNode:
    """Tests for DirectedNode class."""

    def test_creation(self):
        """Test node creation with valid value."""
        node = DirectedNode(42)
        assert node.value == 42
        assert node.next is None

    def test_none_value_raises_error(self):
        """Test that None value raises TypeError."""
        with pytest.raises(TypeError, match="cannot be None"):
            DirectedNode(None)

    def test_equality(self):
        """Test node equality based on values."""
        node1 = DirectedNode(10)
        node2 = DirectedNode(10)
        node3 = DirectedNode(20)

        assert node1 == node2
        assert node1 != node3

    @pytest.mark.parametrize("value", [
        42,
        "hello",
        [1, 2, 3],
        {"key": "value"},
    ])
    def test_various_value_types(self, value):
        """Test nodes can store various types."""
        node = DirectedNode(value)
        assert node.value == value
```

#### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src/pythondatastructures

# Run specific test file
pytest tests/test_nodes.py

# Run specific test
pytest tests/test_nodes.py::TestDirectedNode::test_creation
```

### Documentation

Update documentation when adding features:

#### Code Documentation

- Add docstrings to all public classes and methods
- Include examples in docstrings
- Document time/space complexity for algorithms

#### User Documentation

Update relevant markdown files:

- `docs/data-structures/*.md`: Conceptual guides
- `docs/api/*.md`: API references
- `docs/getting-started/*.md`: Tutorials

#### Building Docs Locally

```bash
# Serve documentation
mkdocs serve

# Build documentation
mkdocs build
```

Visit `http://127.0.0.1:8000` to preview.

## Pull Request Process

### 1. Ensure Quality

Before submitting:

- ✅ All tests pass
- ✅ Code follows style guidelines
- ✅ Documentation is updated
- ✅ Commit messages are clear

### 2. Write Good Commit Messages

```bash
# Good commit messages
git commit -m "Add insert method to DirectedNode"
git commit -m "Fix off-by-one error in list traversal"
git commit -m "Update documentation for linked lists"

# Include details in the body for complex changes
git commit -m "Implement doubly linked list

- Add DoublyLinkedNode class
- Implement bidirectional traversal
- Add comprehensive tests
- Update documentation"
```

### 3. Submit Pull Request

1. Push your branch to GitHub
2. Open a Pull Request
3. Fill out the PR template
4. Link any related issues

### 4. Code Review

- Respond to feedback promptly
- Make requested changes
- Keep the discussion focused and professional
- Be open to suggestions

## What to Work On

### Good First Issues

Look for issues labeled `good first issue`:

- Documentation improvements
- Adding examples
- Writing tests
- Small bug fixes

### Data Structures Needed

Help implement these data structures:

- ✅ Nodes (Complete)
- 🚧 Linked Lists (In Progress)
- 🔜 Stacks
- 🔜 Queues
- 🔜 Trees
- 🔜 Graphs
- 🔜 Hash Tables
- 🔜 Heaps

### Documentation Improvements

- More examples
- Performance comparisons
- Visual diagrams
- Tutorial content
- API reference clarity

## Code of Conduct

### Be Respectful

- Treat everyone with respect
- Welcome newcomers
- Be patient with questions
- Give constructive feedback
- Celebrate contributions

### Be Professional

- Focus on technical merit
- Avoid personal attacks
- Keep discussions on-topic
- Follow community guidelines

### Be Helpful

- Share knowledge
- Answer questions
- Review pull requests
- Mentor contributors

## Getting Help

Need help contributing?

- 💬 Open a discussion on GitHub
- 📧 Reach out to maintainers
- 📖 Read the documentation
- 💡 Look at existing code for examples

## Recognition

Contributors are recognized in:

- Git commit history
- Pull request comments
- Future CONTRIBUTORS.md file
- Release notes

## Thank You!

Every contribution, no matter how small, helps make this project better. Thank you for your time and effort!

---

**Happy Coding! 🐍**
