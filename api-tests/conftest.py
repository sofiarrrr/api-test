import pytest
import os


@pytest.fixture(scope='session')
def url(request):
    return request.config.getoption('--url')
