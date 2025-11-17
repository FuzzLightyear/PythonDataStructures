# Linked Lists API Reference

**Status**: 🚧 Coming Soon

::: pythondatastructures.linkedlist
    options:
      show_root_heading: true
      show_source: true
      heading_level: 2

---

## Note

The linked list module is currently under development. The API documentation will be automatically generated once the implementations are complete.

## Planned Classes

### SinglyLinkedList

A singly-linked list where each node points to the next node.

**Planned Methods:**
- `append(value)`: Add to the end
- `prepend(value)`: Add to the beginning
- `insert(index, value)`: Insert at specific position
- `remove(value)`: Remove first occurrence
- `pop(index)`: Remove and return at index
- `find(value)`: Search for a value
- `__len__()`: Get list length
- `__iter__()`: Iterate over values

### DoublyLinkedList

A doubly-linked list where each node points to both next and previous nodes.

**Planned Methods:**
- All SinglyLinkedList methods
- `reverse_iter()`: Iterate backwards
- More efficient deletion operations

### CircularLinkedList

A circular linked list where the last node points back to the first.

**Planned Methods:**
- Circular traversal methods
- Round-robin operations
- No null/None handling needed

## See Also

- [Nodes API](nodes.md) - Foundation for linked lists
- [Linked Lists Guide](../data-structures/linked-lists.md) - Conceptual documentation
