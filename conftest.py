
def pytest_addoption(parser):

    parser.addoption(
        '--url', action='store', default='https://api.mocklets.com/p68393/songs',
        help='Type in desirable URL.')
    parser.addoption(
        '--browser', action='store', default='firefox',
        help='Type in browser type.')
