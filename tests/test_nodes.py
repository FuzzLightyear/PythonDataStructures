"""Comprehensive test suite for the nodes module.

This module contains unit tests for DirectedNode and related node structures.
Tests cover initialization, representation, equality, and interface methods.
"""

import pytest
from pythondatastructures.nodes import DirectedNode


class TestDirectedNodeInitialization:
    """Test cases for DirectedNode initialization."""

    def test_node_creation_with_integer(self):
        """Test creating a node with an integer value.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies that a node can be created with an integer value
        and has a None next pointer.
        """
        node = DirectedNode(42)
        assert node.value == 42
        assert node.next is None

    def test_node_creation_with_string(self):
        """Test creating a node with a string value.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies that a node can store string values.
        """
        node = DirectedNode("hello")
        assert node.value == "hello"
        assert node.next is None

    def test_node_creation_with_float(self):
        """Test creating a node with a float value.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies that a node can store float values.
        """
        node = DirectedNode(3.14)
        assert node.value == 3.14
        assert node.next is None

    def test_node_creation_with_list(self):
        """Test creating a node with a list value.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies that a node can store complex types like lists.
        """
        test_list = [1, 2, 3]
        node = DirectedNode(test_list)
        assert node.value == test_list
        assert node.next is None

    def test_node_creation_with_dict(self):
        """Test creating a node with a dictionary value.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies that a node can store dictionary values.
        """
        test_dict = {"key": "value"}
        node = DirectedNode(test_dict)
        assert node.value == test_dict
        assert node.next is None

    def test_node_creation_with_zero(self):
        """Test creating a node with zero value.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies that a node can store falsy values like 0.
        """
        node = DirectedNode(0)
        assert node.value == 0
        assert node.next is None

    def test_node_creation_with_empty_string(self):
        """Test creating a node with an empty string.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies that a node can store falsy string values.
        """
        node = DirectedNode("")
        assert node.value == ""
        assert node.next is None

    def test_node_creation_with_none_raises_error(self):
        """Test that creating a node with None value raises TypeError.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies that None is not allowed as a node value to prevent
        confusion with the next pointer being None.
        """
        with pytest.raises(TypeError, match="Node value cannot be None"):
            DirectedNode(None)

    def test_node_creation_with_custom_object(self):
        """Test creating a node with a custom object.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies that a node can store arbitrary custom objects.
        """
        class CustomObject:
            def __init__(self, data):
                self.data = data

        obj = CustomObject("test")
        node = DirectedNode(obj)
        assert node.value is obj
        assert node.value.data == "test"


class TestDirectedNodeRepresentation:
    """Test cases for DirectedNode string representation."""

    def test_repr_with_integer(self):
        """Test __repr__ with integer value.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies that repr shows DirectedNode class name and value.
        """
        node = DirectedNode(42)
        assert repr(node) == "DirectedNode(42)"

    def test_repr_with_string(self):
        """Test __repr__ with string value.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies that repr properly quotes string values.
        """
        node = DirectedNode("hello")
        assert repr(node) == "DirectedNode('hello')"

    def test_repr_with_float(self):
        """Test __repr__ with float value.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies that repr displays float values correctly.
        """
        node = DirectedNode(3.14)
        assert repr(node) == "DirectedNode(3.14)"

    def test_repr_with_list(self):
        """Test __repr__ with list value.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies that repr displays list values correctly.
        """
        node = DirectedNode([1, 2, 3])
        assert repr(node) == "DirectedNode([1, 2, 3])"

    def test_repr_with_none_value_not_in_node(self):
        """Test that we cannot create a node with None to test repr.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        This test verifies the ValueError is raised before repr is called.
        """
        with pytest.raises(TypeError):
            node = DirectedNode(None)

    def test_repr_idempotent(self):
        """Test that repr returns consistent strings.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies that calling repr multiple times returns the same string.
        """
        node = DirectedNode(42)
        repr1 = repr(node)
        repr2 = repr(node)
        assert repr1 == repr2


class TestDirectedNodeEquality:
    """Test cases for DirectedNode equality comparison."""

    def test_equality_same_value(self):
        """Test equality of nodes with the same value.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies that two nodes with the same value are equal.
        """
        node1 = DirectedNode(42)
        node2 = DirectedNode(42)
        assert node1 == node2

    def test_equality_different_value(self):
        """Test inequality of nodes with different values.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies that two nodes with different values are not equal.
        """
        node1 = DirectedNode(42)
        node2 = DirectedNode(43)
        assert node1 != node2

    def test_equality_with_string_values(self):
        """Test equality comparison with string values.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies that equality works correctly for string values.
        """
        node1 = DirectedNode("hello")
        node2 = DirectedNode("hello")
        node3 = DirectedNode("world")
        assert node1 == node2
        assert node1 != node3

    def test_equality_ignores_next_pointer(self):
        """Test that equality only compares values, not next pointers.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies that two nodes with the same value are equal even if
        their next pointers differ.
        """
        node1 = DirectedNode(42)
        node2 = DirectedNode(42)
        node3 = DirectedNode(100)

        node1.next = node3
        # node2.next is still None

        assert node1 == node2  # Still equal because values match

    def test_equality_with_non_node_object(self):
        """Test equality comparison with non-DirectedNode objects.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies that comparing a node with a non-node object returns
        NotImplemented (which Python converts to False).
        """
        node = DirectedNode(42)
        assert node != 42
        assert node != "DirectedNode(42)"
        assert node != [42]

    def test_equality_reflexive(self):
        """Test that a node equals itself.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies reflexive property of equality: x == x.
        """
        node = DirectedNode(42)
        assert node == node

    def test_equality_symmetric(self):
        """Test that equality is symmetric.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies symmetric property of equality: if x == y then y == x.
        """
        node1 = DirectedNode(42)
        node2 = DirectedNode(42)
        assert node1 == node2
        assert node2 == node1

    def test_equality_transitive(self):
        """Test that equality is transitive.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies transitive property of equality:
        if x == y and y == z then x == z.
        """
        node1 = DirectedNode(42)
        node2 = DirectedNode(42)
        node3 = DirectedNode(42)
        assert node1 == node2
        assert node2 == node3
        assert node1 == node3


class TestDirectedNodeLinking:
    """Test cases for linking DirectedNode instances."""

    def test_link_two_nodes(self):
        """Test linking two nodes together.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies that the next pointer can be set to link nodes.
        """
        node1 = DirectedNode(1)
        node2 = DirectedNode(2)
        node1.next = node2
        assert node1.next is node2
        assert node2.next is None

    def test_create_chain(self):
        """Test creating a chain of three nodes.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies that multiple nodes can be linked in a chain.
        """
        node1 = DirectedNode(1)
        node2 = DirectedNode(2)
        node3 = DirectedNode(3)

        node1.next = node2
        node2.next = node3

        assert node1.next is node2
        assert node2.next is node3
        assert node3.next is None

    def test_traverse_chain(self):
        """Test traversing a chain of nodes.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies that we can traverse a chain of linked nodes.
        """
        node1 = DirectedNode(1)
        node2 = DirectedNode(2)
        node3 = DirectedNode(3)

        node1.next = node2
        node2.next = node3

        # Traverse and collect values
        current = node1
        values = []
        while current is not None:
            values.append(current.value)
            current = current.next

        assert values == [1, 2, 3]

    def test_reassign_next_pointer(self):
        """Test reassigning the next pointer.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies that the next pointer can be reassigned to different nodes.
        """
        node1 = DirectedNode(1)
        node2 = DirectedNode(2)
        node3 = DirectedNode(3)

        node1.next = node2
        assert node1.next is node2

        node1.next = node3
        assert node1.next is node3

    def test_break_chain(self):
        """Test breaking a chain by setting next to None.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies that a chain can be broken by setting next to None.
        """
        node1 = DirectedNode(1)
        node2 = DirectedNode(2)

        node1.next = node2
        assert node1.next is node2

        node1.next = None
        assert node1.next is None

    def test_circular_reference(self):
        """Test creating a circular reference.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies that nodes can point to previous nodes (though this
        would create infinite loops in traversal).
        """
        node1 = DirectedNode(1)
        node2 = DirectedNode(2)

        node1.next = node2
        node2.next = node1

        assert node1.next is node2
        assert node2.next is node1


class TestDirectedNodeInterfaceMethods:
    """Test cases for DirectedNode interface methods."""

    def test_insert_not_implemented(self):
        """Test that insert() raises NotImplementedError.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies that insert() is an abstract method that must be
        implemented by subclasses.
        """
        node1 = DirectedNode(1)
        node2 = DirectedNode(2)
        with pytest.raises(
            NotImplementedError, match="does not implement insert"
        ):
            node1.insert(node2)

    def test_insert_with_relative_index_not_implemented(self):
        """Test that insert() with relative_index raises NotImplementedError.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies that insert() with custom relative_index is also abstract.
        """
        node1 = DirectedNode(1)
        node2 = DirectedNode(2)
        with pytest.raises(NotImplementedError):
            node1.insert(node2, relative_index=1)

    def test_append_not_implemented(self):
        """Test that append() raises NotImplementedError.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies that append() is an abstract method that must be
        implemented by subclasses.
        """
        node1 = DirectedNode(1)
        node2 = DirectedNode(2)
        with pytest.raises(
            NotImplementedError, match="does not implement append"
        ):
            node1.append(node2)

    def test_pop_not_implemented(self):
        """Test that pop() raises NotImplementedError.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies that pop() is an abstract method that must be
        implemented by subclasses.
        """
        node = DirectedNode(1)
        with pytest.raises(NotImplementedError, match="does not implement pop"):
            node.pop()

    def test_pop_with_relative_index_not_implemented(self):
        """Test that pop() with relative_index raises NotImplementedError.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies that pop() with custom relative_index is also abstract.
        """
        node = DirectedNode(1)
        with pytest.raises(NotImplementedError):
            node.pop(relative_index=2)

    def test_pop_value_not_implemented(self):
        """Test that pop_value() raises NotImplementedError.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies that pop_value() is an abstract method that must be
        implemented by subclasses.
        """
        node = DirectedNode(1)
        with pytest.raises(
            NotImplementedError, match="does not implement pop_value"
        ):
            node.pop_value(1)

    def test_dequeue_not_implemented(self):
        """Test that dequeue() raises NotImplementedError.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies that dequeue() is an abstract method that must be
        implemented by subclasses.
        """
        node = DirectedNode(1)
        with pytest.raises(
            NotImplementedError, match="does not implement dequeue"
        ):
            node.dequeue()

    def test_dequeue_with_direct_flag_not_implemented(self):
        """Test that dequeue() with direct=True raises NotImplementedError.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies that dequeue() with direct=True is also abstract.
        """
        node = DirectedNode(1)
        with pytest.raises(NotImplementedError):
            node.dequeue(direct=True)


class TestDirectedNodeEdgeCases:
    """Test cases for edge cases and special scenarios."""

    def test_node_with_boolean_value(self):
        """Test creating a node with a boolean value.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies that boolean values (True, False) can be stored.
        """
        node_true = DirectedNode(True)
        node_false = DirectedNode(False)
        assert node_true.value is True
        assert node_false.value is False

    def test_node_with_negative_number(self):
        """Test creating a node with a negative number.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies that negative numbers can be stored.
        """
        node = DirectedNode(-42)
        assert node.value == -42

    def test_node_with_tuple(self):
        """Test creating a node with a tuple value.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies that immutable types like tuples can be stored.
        """
        node = DirectedNode((1, 2, 3))
        assert node.value == (1, 2, 3)

    def test_node_with_set(self):
        """Test creating a node with a set value.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies that set types can be stored.
        """
        node = DirectedNode({1, 2, 3})
        assert node.value == {1, 2, 3}

    def test_multiple_references_to_same_node(self):
        """Test multiple references pointing to the same node.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies that multiple variables can point to the same node.
        """
        node = DirectedNode(42)
        ref1 = node
        ref2 = node
        assert ref1 is ref2
        assert ref1 is node

    def test_large_value(self):
        """Test creating a node with a large integer.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies that nodes can store arbitrarily large integers.
        """
        large_number = 10**100
        node = DirectedNode(large_number)
        assert node.value == large_number

    def test_long_chain_traversal(self):
        """Test traversing a chain of many nodes.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Verifies that nodes can be chained and traversed in sequence.
        """
        # Create a chain of 100 nodes
        nodes = [DirectedNode(i) for i in range(100)]
        for i in range(99):
            nodes[i].next = nodes[i + 1]

        # Traverse and verify
        current = nodes[0]
        count = 0
        while current is not None:
            count += 1
            current = current.next

        assert count == 100
