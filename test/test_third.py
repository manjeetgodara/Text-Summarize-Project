import sys

import pytest

@pytest.mark.smoke
def test_login():
    print("Login Test")

@pytest.mark.skip
def test_summarize():
    print("Summarize Test")


@pytest.mark.skipif(sys.version_info < (3, 14), reason="requires Python 3.14 or higher")
def test_logout():
    print("Logout Test")



@pytest.mark.parametrize("username, password",  # Corrected
                         [
                             ("Selenium", "WebDriver"),
                             ("Python", "Pytest"),
                             ("Manjeet", "Godara")
                         ])
def test_login_service(username, password):
    print(username, password)

