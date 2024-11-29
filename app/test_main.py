from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word, expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
    ],
)
def test_main(word: str, expected: bool) -> None:
    assert expected == is_isogram(word)
