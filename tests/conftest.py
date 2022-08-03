import pytest

pytest_plugins = [
    'fixtures.fixtures'
]


@pytest.fixture()
def used_imported_fixture(make_string):
    make_string
