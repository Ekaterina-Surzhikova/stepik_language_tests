
import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--language",
        action="store",
        default="en",
        help="Choose language: en, es, fr, etc."
    )


@pytest.fixture
def browser(request):
    language = request.config.getoption("language")

    options = webdriver.ChromeOptions()
    options.add_experimental_option(
        "prefs",
        {"intl.accept_languages": language}
    )
    options.add_argument(f"--lang={language}")

    browser = webdriver.Chrome(options=options)

    yield browser

    browser.quit()
