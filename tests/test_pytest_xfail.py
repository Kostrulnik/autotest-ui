import pytest


@pytest.mark.xfail(reason="найден баг")
def test_with_bug():
    assert 1 == 2


@pytest.mark.xfail(reason="баг исправлен")
def test_without_bug():
    pass
