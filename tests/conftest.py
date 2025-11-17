"""Pytest configuration and shared fixtures."""

import pytest


@pytest.fixture
def sample_values():
    """
    Provide sample values for testing data structures.

    Returns
    -------
    list
        A list of mixed-type values for testing.
    """
    return [1, 2, 3, "hello", "world", 42, None, 3.14]


@pytest.fixture
def empty_list():
    """
    Provide an empty list for testing.

    Returns
    -------
    list
        An empty list.
    """
    return []
