__author__: "730556602"


"""Unit tests for dictionary functions."""


from exercises.ex07.dictionary import invert, favorite_color, count

import pytest

def test_empty_dictionary() -> None:
    test_dict: dict[str, str] = {}
    assert invert(test_dict) == {}

def test_invert() -> None:
    test_dict: dict[str, str] = {"a": "1", "b": "2", "c": "3"}
    assert invert(test_dict) == {"3": "a", "2": "b", "3": "c"}

with pytest.raises(KeyError):
        my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
        invert(my_dictionary)




def test_multiple_colors() -> None:
    test_dict: dict[str, str] = {"Shivani": "green", "Meghan": "green", "Carly": "blue", "Grace": "pink"}
    assert favorite_color(test_dict) == "green"


def test_duplicate_colors() -> None:
    test_dict: dict[str, str] = {"Shivani": "green", "Meghan": "green", "Carly": "blue", "Grace": "blue"}
    assert favorite_color(test_dict) == "green"


def test_no_colors() -> None:
    test_dict: dict[str, str] = {}
    assert favorite_color(test_dict) == ""


def test_count() -> None:
    test_list: list[str] = ["a", "a", "b", "c"]
    assert count(test_list) == {"a": 2, "b": 1, "c": 1}


def test_none() -> None:
    test_list: list[str] = []
    assert count(test_list) == {}


def test_count() -> None:
    test_list: list[str] = ["a", "a", "a", "a"]
    assert count(test_list) == {"a": 3}