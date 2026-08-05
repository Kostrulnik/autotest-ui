import pytest


@pytest.mark.smoke
def test_some_case():
    pass


@pytest.mark.regression
def test_regression_case():
    pass


@pytest.mark.smoke
class TestSuite:
    def test_suite(self):
        pass

    def test_suite_with_registration(self):
        pass


class TestUserAuth:
    @pytest.mark.smoke
    def test_login(self):
        pass

    @pytest.mark.slow
    def test_password_reset(self):
        pass

    def test_logout(self):
        pass
