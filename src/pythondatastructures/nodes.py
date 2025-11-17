"""Implementations of linked list node structures.

This module provides base classes and implementations for singly-linked node
structures that can be used to build various linear data structures.
"""

from __future__ import annotations

from typing import Any, Optional


class DirectedNode:
    """A node in a singly-linked list with forward traversal capability.

    This class represents a single node in a linked list structure that can
    reference a single next node. It serves as a base class for various linked
    list implementations and provides an interface for common operations.

    Attributes
    ----------
    value : Any
        The value stored in this node.
    next : DirectedNode or None
        Reference to the next node in the linked structure, or None if this
        is the last node.

    Examples
    --------
    >>> node1 = DirectedNode(10)
    >>> node2 = DirectedNode(20)
    >>> node1.next = node2
    >>> repr(node1)
    'DirectedNode(10)'
    """

    def __init__(self, value: Any) -> None:
        """Initialize a new DirectedNode.

        Parameters
        ----------
        value : Any
            The value to store in this node.

        Raises
        ------
        TypeError
            If value is None (nodes must store explicit values).
        """
        if value is None:
            raise TypeError("Node value cannot be None")
        self.value: Any = value
        self.next: Optional[DirectedNode] = None

    def __repr__(self) -> str:
        """Return a string representation of the node.

        Returns
        -------
        str
            A string representation showing the node class and value.
        """
        return f"DirectedNode({self.value!r})"

    def __eq__(self, other: object) -> bool:
        """Check equality based on node value.

        Parameters
        ----------
        other : object
            The object to compare with.

        Returns
        -------
        bool
            True if both objects are DirectedNode instances with equal values,
            False otherwise.
        """
        if not isinstance(other, DirectedNode):
            return NotImplemented
        return self.value == other.value

    def insert(
        self, node: DirectedNode, relative_index: int = 0
    ) -> None:
        """Insert a node at a specified relative index from the current node.

        This method inserts a node at the given relative position within the
        linked structure starting from the current node.

        Parameters
        ----------
        node : DirectedNode
            The node to be inserted.
        relative_index : int, optional
            The index relative to the current node where the new node should
            be inserted. A value of 0 means insert immediately after this node
            (default is 0).

        Raises
        ------
        ValueError
            If the relative index is negative or out of bounds.
        TypeError
            If node is not a DirectedNode instance.
        NotImplementedError
            This method must be implemented by subclasses.

        Notes
        -----
        Subclasses must implement this method to provide specific insertion
        behavior based on their linked structure type.
        """
        raise NotImplementedError(
            f"{self.__class__.__name__} does not implement insert()"
        )

    def append(self, node: DirectedNode) -> None:
        """Append a node at the end of the linked structure.

        This method appends a node at the end of the chain starting from the
        current node. It traverses to the last node and appends after it.

        Parameters
        ----------
        node : DirectedNode
            The node to be appended.

        Raises
        ------
        TypeError
            If node is not a DirectedNode instance.
        NotImplementedError
            This method must be implemented by subclasses.

        Notes
        -----
        Subclasses must implement this method to provide specific append
        behavior based on their linked structure type.
        """
        raise NotImplementedError(
            f"{self.__class__.__name__} does not implement append()"
        )

    def pop(self, relative_index: int = 0) -> Optional[DirectedNode]:
        """Remove and return the node at a specified relative index.

        This method removes and returns the node at the given relative position
        within the linked structure starting from the current node.

        Parameters
        ----------
        relative_index : int, optional
            The index relative to the current node of the node to be removed.
            A value of 0 means remove the node immediately after this node
            (default is 0).

        Returns
        -------
        DirectedNode or None
            The removed node, or None if no node exists at the specified index.

        Raises
        ------
        ValueError
            If the relative index is negative or out of bounds.
        NotImplementedError
            This method must be implemented by subclasses.

        Notes
        -----
        Subclasses must implement this method to provide specific removal
        behavior based on their linked structure type.
        """
        raise NotImplementedError(
            f"{self.__class__.__name__} does not implement pop()"
        )

    def pop_value(self, value: Any) -> Optional[DirectedNode]:
        """Remove and return the first node with the specified value.

        This method searches for and removes the first node with a value
        matching the provided value, starting from the current node.

        Parameters
        ----------
        value : Any
            The value of the node to be removed.

        Returns
        -------
        DirectedNode or None
            The removed node, or None if no node with the specified value exists.

        Raises
        ------
        TypeError
            If the value type cannot be compared with node values.
        NotImplementedError
            This method must be implemented by subclasses.

        Notes
        -----
        Subclasses must implement this method to provide specific value-based
        removal behavior based on their linked structure type.
        """
        raise NotImplementedError(
            f"{self.__class__.__name__} does not implement pop_value()"
        )

    def dequeue(self, direct: bool = False) -> Optional[DirectedNode]:
        """Remove and return a node from the structure.

        This method removes and returns either the node immediately after the
        current node (if direct=True) or the last node in the chain
        (if direct=False).

        Parameters
        ----------
        direct : bool, optional
            If True, dequeue from the front (node immediately after current).
            If False, dequeue from the back (last node in chain).
            Default is False.

        Returns
        -------
        DirectedNode or None
            The removed node, or None if the structure is empty.

        Raises
        ------
        NotImplementedError
            This method must be implemented by subclasses.

        Notes
        -----
        Subclasses must implement this method to provide specific dequeue
        behavior based on their linked structure type and use case
        (e.g., FIFO for queues, LIFO for stacks).
        """
        raise NotImplementedError(
            f"{self.__class__.__name__} does not implement dequeue()"
        )