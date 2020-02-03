import pytest
import requests
@pytest.fixture(scope="function")
def init_session():
    return requests.sessions.Session()