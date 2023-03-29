__author__: "730556602"


"""Unit tests for dictionary functions."""


from exercises.ex07.dictionary import invert, favorite_color, count

import pytest

def test_empty_dictionary() -> None:
    """Tests empty dictionary."""
    test_dict: dict[str, str] = {}
    assert invert(test_dict) == {}

def test_invert() -> None:
    """Tests a basic dictionary."""
    test_dict: dict[str, str] = {"a": "1", "b": "2", "c": "3"}
    assert invert(test_dict) == {"1": "a", "2": "b", "3": "c"}

with pytest.raises(KeyError):
    """Tests for KeyError"""
    my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
    invert(my_dictionary)


def test_multiple_colors() -> None:
    """Tests mulitple colors."""
    test_dict: dict[str, str] = {"Shivani": "green", "Meghan": "green", "Carly": "blue", "Grace": "pink"}
    assert favorite_color(test_dict) == "green"


def test_duplicate_colors() -> None:
    """Tests duplicate most common colors."""
    test_dict: dict[str, str] = {"Shivani": "green", "Meghan": "green", "Carly": "blue", "Grace": "blue"}
    assert favorite_color(test_dict) == "green"


def test_no_colors() -> None:
    """Tests empty dictionary."""
    test_dict: dict[str, str] = {}
    assert favorite_color(test_dict) == ""


def test_count() -> None:
    """Tests basic list."""
    test_list: list[str] = ["a", "a", "b", "c"]
    assert count(test_list) == {"a": 2, "b": 1, "c": 1}


def test_none() -> None:
    """Tests for empty list."""
    test_list: list[str] = []
    assert count(test_list) == {}


def test_count() -> None:
    """Tests for one value in list."""
    test_list: list[str] = ["a", "a", "a", "a"]
    assert count(test_list) == {"a": 3}