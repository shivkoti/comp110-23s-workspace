__author__: "730556602"

"""Unit tests for dictionary functions."""

from exercises.ex07.dictionary import invert, favorite_colors, count

def test_empty_dictionary() -> None:
    test_dict: dict[str, str] = {}
    assert invert(test_dict) == {}

def test_multiple_colors() -> None:
    test_dict: dict[str, str] = {"Shivani": "green", "Meghan": "green", "Carly": "blue", "Grace": "pink"}
    assert favorite_colors(test_dict) == "green"

def test_count() -> None:
    test_list: list[str] = ["a", "a", "b", "c"]
    assert count(test_list) == {"a": 2, "b": 1, "c": 1}