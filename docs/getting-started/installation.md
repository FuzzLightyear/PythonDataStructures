# Installation

This guide will help you get Python Data Structures installed and ready to use.

## Requirements

- Python 3.11 or higher
- pip or [uv](https://github.com/astral-sh/uv) package manager

## Installation Methods

### Using uv (Recommended)

[uv](https://github.com/astral-sh/uv) is a fast Python package installer and resolver written in Rust.

```bash
# Install uv if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone the repository
git clone https://github.com/FuzzLightyear/PythonDataStructures.git
cd PythonDataStructures

# Install the package and dependencies
uv pip install -e .
```

### Using pip

```bash
# Clone the repository
git clone https://github.com/FuzzLightyear/PythonDataStructures.git
cd PythonDataStructures

# Install the package and dependencies
pip install -e .
```

## Development Installation

If you want to contribute to the project or run tests, install with development dependencies:

```bash
# Using uv
uv pip install -e ".[dev]"

# Using pip
pip install -e ".[dev]"
```

## Documentation Installation

To build the documentation locally:

```bash
# Using uv
uv pip install -e ".[docs]"

# Using pip
pip install -e ".[docs]"

# Serve the documentation
mkdocs serve
```

Then visit `http://127.0.0.1:8000` in your browser.

## Verify Installation

After installation, verify everything is working:

```python
from pythondatastructures.nodes import DirectedNode

# Create a test node
node = DirectedNode(42)
print(node)  # Output: DirectedNode(42)
print("Installation successful!")
```

## Troubleshooting

### Python Version Issues

If you encounter Python version errors, ensure you're using Python 3.11 or higher:

```bash
python --version
```

If you need to use a specific Python version:

```bash
# With uv
uv pip install -e . --python 3.11

# With pip
python3.11 -m pip install -e .
```

### Dependency Conflicts

If you experience dependency conflicts, try creating a fresh virtual environment:

```bash
# Create a virtual environment
python -m venv venv

# Activate it (Unix/macOS)
source venv/bin/activate

# Activate it (Windows)
venv\Scripts\activate

# Install the package
pip install -e .
```

## Next Steps

- [Quick Start Guide](quickstart.md) - Learn the basics
- [Data Structures Overview](../data-structures/index.md) - Explore available structures
- [API Reference](../api/index.md) - Detailed API documentation
