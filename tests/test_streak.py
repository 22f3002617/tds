import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Tests that an empty list returns a streak of 0."""
    assert longest_positive_streak([]) == 0

def test_single_positive_streak():
    """Tests a simple case with a single positive streak."""
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_multiple_streaks_longest_at_end():
    """Tests multiple streaks, with the longest streak at the end."""
    assert longest_positive_streak([1, 2, -1, 3, 4, 5]) == 3

def test_multiple_streaks_longest_at_beginning():
    """Tests multiple streaks, with the longest streak at the beginning."""
    assert longest_positive_streak([1, 2, 3, 4, -1, 5, 6]) == 4

def test_with_zeros():
    """Tests that zeros break the streak."""
    assert longest_positive_streak([1, 2, 0, 3, 4, 5]) == 3

def test_with_negatives():
    """Tests that negative numbers break the streak."""
    assert longest_positive_streak([1, 2, -5, 3, 4, 5]) == 3

def test_no_positive_numbers():
    """Tests a list with no positive numbers."""
    assert longest_positive_streak([-1, -2, -3, 0]) == 0

def test_all_ones():
    """Tests a streak of all ones."""
    assert longest_positive_streak([1, 1, 1, 1]) == 4

def test_example_from_prompt():
    """Tests the example provided in the problem description."""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3
