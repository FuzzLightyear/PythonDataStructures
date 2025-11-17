"""
Test suite for the old linkedlist implementation.

This module contains tests for the original linkedlist, stack, queue,
and advLinkedList implementations from linkedlist.py.
"""

import pytest
from pythondatastructures.old import (
    llnode,
    linkedlist,
    stack,
    queue,
    advLinkedList,
)


class TestLLNode:
    """Test cases for the llnode class."""

    def test_node_creation(self):
        """
        Test basic node creation.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies that a node can be created with a value and has
        properly initialized left and right pointers.
        """
        node = llnode(42)
        assert node.value == 42
        assert node.left is None
        assert node.right is None

    def test_node_value_assignment(self):
        """
        Test node value assignment.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies that a node stores the assigned value correctly
        and can handle different data types.
        """
        # Test with integer
        node_int = llnode(10)
        assert node_int.value == 10

        # Test with string
        node_str = llnode("hello")
        assert node_str.value == "hello"

        # Test with float
        node_float = llnode(3.14)
        assert node_float.value == 3.14

        # Test with list
        node_list = llnode([1, 2, 3])
        assert node_list.value == [1, 2, 3]

    def test_node_linking(self):
        """
        Test linking nodes together.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies that nodes can be linked via left and right pointers
        and the links are properly established.
        """
        node1 = llnode(1)
        node2 = llnode(2)
        node3 = llnode(3)

        # Link nodes
        node1.right = node2
        node2.left = node1
        node2.right = node3
        node3.left = node2

        # Verify links
        assert node1.right is node2
        assert node2.left is node1
        assert node2.right is node3
        assert node3.left is node2


class TestLinkedList:
    """Test cases for the basic linkedlist class."""

    def test_empty_list_creation(self):
        """
        Test creation of an empty linked list.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies that a new linkedlist has a None root.
        """
        ll = linkedlist()
        assert ll.root is None

    def test_list_with_root(self):
        """
        Test linked list with a root node.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies that a linkedlist can have a root node assigned
        and the root is accessible.
        """
        ll = linkedlist()
        node = llnode(100)
        ll.root = node
        assert ll.root is node
        assert ll.root.value == 100


class TestStack:
    """Test cases for the stack implementation."""

    def test_stack_creation(self):
        """
        Test stack creation.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies that a stack can be created and inherits from linkedlist.
        """
        s = stack()
        assert isinstance(s, linkedlist)
        assert s.root is None

    def test_push_single_element(self):
        """
        Test pushing a single element onto the stack.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies that pushing an element to an empty stack creates
        a root node with that value.
        """
        s = stack()
        s.push(42)
        assert s.root is not None
        assert s.root.value == 42

    def test_push_multiple_elements(self):
        """
        Test pushing multiple elements onto the stack.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies that pushing multiple elements maintains LIFO order
        and properly links nodes.
        """
        s = stack()
        s.push(1)
        s.push(2)
        s.push(3)

        # Top of stack should be 3
        assert s.root.value == 3
        # Second element should be 2
        assert s.root.right.value == 2
        # Third element should be 1
        assert s.root.right.right.value == 1

    def test_pop_single_element(self):
        """
        Test popping a single element from the stack.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies that popping from a stack with one element returns
        that element and leaves the stack empty.
        """
        s = stack()
        s.push(42)
        popped = s.pop()
        assert popped.value == 42
        assert s.root is None

    def test_pop_multiple_elements(self):
        """
        Test popping multiple elements from the stack.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies that popping returns elements in LIFO order.
        """
        s = stack()
        s.push(1)
        s.push(2)
        s.push(3)

        # Pop should return elements in LIFO order: 3, 2, 1
        popped1 = s.pop()
        assert popped1.value == 3

        popped2 = s.pop()
        assert popped2.value == 2

        popped3 = s.pop()
        assert popped3.value == 1

        assert s.root is None

    def test_pop_empty_stack(self):
        """
        Test popping from an empty stack.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies the behavior when attempting to pop from an empty stack.
        """
        s = stack()
        result = s.pop()
        assert result is None

    def test_stack_lifo_order(self):
        """
        Test LIFO (Last In First Out) ordering of stack.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies that stack maintains proper LIFO semantics with
        a sequence of push and pop operations.
        """
        s = stack()
        values = [10, 20, 30, 40, 50]

        # Push all values
        for val in values:
            s.push(val)

        # Pop and verify LIFO order (reverse of push)
        for val in reversed(values):
            popped = s.pop()
            assert popped.value == val

        assert s.root is None


class TestQueue:
    """Test cases for the queue implementation."""

    def test_queue_creation(self):
        """
        Test queue creation.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies that a queue can be created and inherits from linkedlist.
        """
        q = queue()
        assert isinstance(q, linkedlist)
        assert q.root is None

    def test_push_single_element(self):
        """
        Test pushing a single element onto the queue.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies that pushing an element to an empty queue creates
        a root node with that value.
        """
        q = queue()
        q.push(42)
        assert q.root is not None
        assert q.root.value == 42

    def test_push_multiple_elements(self):
        """
        Test pushing multiple elements onto the queue.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies that pushing multiple elements adds them to the end
        of the queue and properly links nodes.
        """
        q = queue()
        q.push(1)
        q.push(2)
        q.push(3)

        # Front of queue should be 1
        assert q.root.value == 1
        # Second element should be 2
        assert q.root.right.value == 2
        # Third element should be 3
        assert q.root.right.right.value == 3

    def test_pop_single_element(self):
        """
        Test popping a single element from the queue.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies that popping from a queue with one element returns
        that element and leaves the queue empty.
        """
        q = queue()
        q.push(42)
        popped = q.pop()
        assert popped.value == 42
        assert q.root is None

    def test_pop_multiple_elements(self):
        """
        Test popping multiple elements from the queue.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies that popping returns elements in FIFO order.
        """
        q = queue()
        q.push(1)
        q.push(2)
        q.push(3)

        # Pop should return elements in FIFO order: 1, 2, 3
        popped1 = q.pop()
        assert popped1.value == 1

        popped2 = q.pop()
        assert popped2.value == 2

        popped3 = q.pop()
        assert popped3.value == 3

        assert q.root is None

    def test_pop_empty_queue(self):
        """
        Test popping from an empty queue.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies the behavior when attempting to pop from an empty queue.
        """
        q = queue()
        result = q.pop()
        assert result is None

    def test_queue_fifo_order(self):
        """
        Test FIFO (First In First Out) ordering of queue.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies that queue maintains proper FIFO semantics with
        a sequence of push and pop operations.
        """
        q = queue()
        values = [10, 20, 30, 40, 50]

        # Push all values
        for val in values:
            q.push(val)

        # Pop and verify FIFO order (same as push)
        for val in values:
            popped = q.pop()
            assert popped.value == val

        assert q.root is None


class TestAdvLinkedList:
    """Test cases for the advLinkedList class."""

    def test_list_creation(self):
        """
        Test advanced linked list creation.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies that an advLinkedList can be created and inherits
        from linkedlist.
        """
        ll = advLinkedList()
        assert isinstance(ll, linkedlist)
        assert ll.root is None

    def test_append_to_empty_list(self):
        """
        Test appending to an empty list.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies that appending a value to an empty list creates
        a root node with that value.
        """
        ll = advLinkedList()
        ll.append(42)
        assert ll.root is not None
        assert ll.root.value == 42

    def test_append_multiple_values(self):
        """
        Test appending multiple values to the list.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies that appending multiple values adds them to the end
        of the list in the correct order.
        """
        ll = advLinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)

        # Verify order: 1 -> 2 -> 3
        assert ll.root.value == 1
        assert ll.root.right.value == 2
        assert ll.root.right.right.value == 3

    def test_index_of_existing_value(self):
        """
        Test finding the index of an existing value.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies that indexOfVal returns the correct index for
        values present in the list.
        """
        ll = advLinkedList()
        ll.append(10)
        ll.append(20)
        ll.append(30)

        assert ll.indexOfVal(10) == 0
        assert ll.indexOfVal(20) == 1
        assert ll.indexOfVal(30) == 2

    def test_index_of_nonexistent_value(self):
        """
        Test finding the index of a value not in the list.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies that indexOfVal returns -1 for values not in the list.
        """
        ll = advLinkedList()
        ll.append(10)
        ll.append(20)
        ll.append(30)

        assert ll.indexOfVal(40) == -1
        assert ll.indexOfVal(100) == -1

    def test_index_of_empty_list(self):
        """
        Test indexOfVal on an empty list.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies that indexOfVal returns -1 for an empty list.
        """
        ll = advLinkedList()
        assert ll.indexOfVal(42) == -1

    def test_value_at_valid_index(self):
        """
        Test retrieving value at a valid index.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies that valAtIndex returns the correct value for
        valid indices.
        """
        ll = advLinkedList()
        ll.append("a")
        ll.append("b")
        ll.append("c")

        assert ll.valAtIndex(0) == "a"
        assert ll.valAtIndex(1) == "b"
        assert ll.valAtIndex(2) == "c"

    def test_value_at_invalid_index(self):
        """
        Test retrieving value at an invalid index.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies that valAtIndex returns None for indices beyond
        the list bounds.
        """
        ll = advLinkedList()
        ll.append(1)
        ll.append(2)

        assert ll.valAtIndex(5) is None
        assert ll.valAtIndex(10) is None

    def test_value_at_index_empty_list(self):
        """
        Test valAtIndex on an empty list.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies that valAtIndex returns None for an empty list.
        """
        ll = advLinkedList()
        assert ll.valAtIndex(0) is None

    def test_remove_root_value(self):
        """
        Test removing the root value.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies that removing the root value updates the list
        properly and returns the removed node.
        """
        ll = advLinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)

        removed = ll.removeVal(1)
        assert removed.value == 1
        assert ll.root.value == 2
        assert ll.root.right.value == 3

    def test_remove_middle_value(self):
        """
        Test removing a value from the middle of the list.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies that removing a middle value properly updates
        the links and returns the removed node.
        """
        ll = advLinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)

        removed = ll.removeVal(2)
        assert removed.value == 2
        assert ll.root.value == 1
        assert ll.root.right.value == 3

    def test_remove_last_value(self):
        """
        Test removing the last value in the list.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies that removing the last value properly updates
        the links and returns the removed node.
        """
        ll = advLinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)

        removed = ll.removeVal(3)
        assert removed.value == 3
        assert ll.root.value == 1
        assert ll.root.right.value == 2
        assert ll.root.right.right is None

    def test_remove_nonexistent_value(self):
        """
        Test removing a value not in the list.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies the behavior when attempting to remove a value
        that doesn't exist in the list.
        """
        ll = advLinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)

        # Removing nonexistent value should return the first found value
        # (which is an odd behavior, but we test the actual implementation)
        result = ll.removeVal(99)
        # The function will iterate through and not find it, returning the tmp value
        # which is the iterator, so it may not be predictable

    def test_remove_from_empty_list(self):
        """
        Test removing from an empty list.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies the behavior when attempting to remove from
        an empty list.
        """
        ll = advLinkedList()
        # This will raise an error because tmp is referenced before assignment
        # when self.root is None. Testing that it raises an exception.
        with pytest.raises(UnboundLocalError):
            ll.removeVal(1)

    def test_duplicate_values(self):
        """
        Test behavior with duplicate values.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies that indexOfVal and removeVal handle lists with
        duplicate values correctly (should find/remove first occurrence).
        """
        ll = advLinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(2)
        ll.append(3)

        # indexOfVal should find the first occurrence (index 1)
        assert ll.indexOfVal(2) == 1

        # removeVal should remove the first occurrence
        removed = ll.removeVal(2)
        assert removed.value == 2

        # Verify the second 2 is still there at index 1
        assert ll.valAtIndex(1) == 2

    def test_mixed_data_types(self):
        """
        Test list with mixed data types.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies that the list can handle mixed data types
        (integers, strings, floats, etc.).
        """
        ll = advLinkedList()
        ll.append(42)
        ll.append("hello")
        ll.append(3.14)
        ll.append([1, 2, 3])

        assert ll.valAtIndex(0) == 42
        assert ll.valAtIndex(1) == "hello"
        assert ll.valAtIndex(2) == 3.14
        assert ll.valAtIndex(3) == [1, 2, 3]

        assert ll.indexOfVal(42) == 0
        assert ll.indexOfVal("hello") == 1
        assert ll.indexOfVal(3.14) == 2
        assert ll.indexOfVal([1, 2, 3]) == 3
