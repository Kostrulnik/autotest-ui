import pytest


@pytest.mark.parametrize('number', [1, 2, 3, -1])
def test_numbers(number: int):
    assert number > 0


@pytest.mark.parametrize('number, expected', [(1, 1), (2, 4), (3, 9)])
def test_several_numbers(number, expected):
    assert number ** 2 == expected


@pytest.mark.parametrize('os', ['macos', 'windows', 'linux', 'debian'])
@pytest.mark.parametrize('browser', ['chrome', 'firefox', 'webkit'])
def test_multiplication_of_numbers(os, browser):
    assert len(os + browser) > 0


@pytest.fixture(params=['chrome', 'firefox', 'webkit'])
def browser(request):
    return request.param


def test_open_browser(browser):
    print(f'Running test on browser: {browser}')


@pytest.mark.parametrize('user', ['Alice', 'Zara'])
class TestOperations:
    @pytest.mark.parametrize('account', ['Credit card', 'Debit card'])
    def test_user_with_operation(self, user, account):
        print(f'User with operation: {user}')

    def test_user_without_operation(self, user):
        print(f'User without no operation: {user}')


users = {
    '+700000001': 'User with money on bank account',
    '+70000002': 'User without money on bank account',
    '+70000033': 'User with operations on bank account',
}


@pytest.mark.parametrize(
    'phone_number',
    users.keys(),
    ids=lambda phone_number: f'{phone_number}: {users[phone_number]}'
)
def test_identifiers(phone_number):
    ...
