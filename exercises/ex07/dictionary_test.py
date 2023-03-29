"""Unit tests for dictionary functions."""
__author__: "730556602"

from exercises.ex07.dictionary import invert, favorite_color, count


def test_empty_dictionary() -> None:
    """Tests empty dictionary."""
    test_dict: dict[str, str] = {}
    assert invert(test_dict) == {}


def test_invert() -> None:
    """Tests a basic dictionary."""
    test_dict: dict[str, str] = {"a": "1", "b": "2", "c": "3"}
    assert invert(test_dict) == {"1": "a", "2": "b", "3": "c"}


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


def test_count_2() -> None:
    """Tests for one value in list."""
    test_list: list[str] = ["a", "a", "a", "a"]
    assert count(test_list) == {"a": 4}