import pytest

@pytest.fixture
def client():
    print("start browser")
    yield
    print("end browser")

def test_login(client):
    # print("start browser")
    print("Login Test")


def test_summarize(client):
    # print("start browser")
    print("Summarize Test")
    # print("close browser")

def test_logout(client):
    # print("start browser")
    print("Logout Test")
    # print("close browser")

