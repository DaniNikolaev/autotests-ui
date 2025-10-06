import pytest


@pytest.mark.parametrize('number', [
    pytest.param(1),
    pytest.param(2),
    pytest.param(3),
    pytest.param(-1, marks=pytest.mark.skip(reason="Negative value"))])
def test_numbers(number: int):
    assert number > 0


@pytest.mark.parametrize('number, expected', [
    (1, 1),
    (2, 8),
    (3, 27),
    (4, 64)
])
def test_several_numbers(number: int, expected: int):
    assert number ** 3 == expected


@pytest.mark.parametrize('browser', ['chromium', 'webkit', 'firefox'])
@pytest.mark.parametrize('os', ['windows', 'macOS', 'linux', 'debian', 'ubuntu'])
def test_combination(browser: str, os: str):
    ...


users = {
    '123': 'User1',
    '456': 'User2',
    '789': 'User3'
}


@pytest.mark.parametrize('phone_number',
                         users.keys(),
                         ids=lambda phone_number: f'{users[phone_number]}: {phone_number}'
                         )
def test_identifiers(phone_number: str):
    ...


@pytest.mark.parametrize("role", ["AAA", "BBB"], ids=["ADMIN", "USER"])
def test_roles(role):
    ...
