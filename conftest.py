import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption(
        "--language", 
        action="store", 
        default="en", 
        help="Choose language: en, es, fr, etc."
    )

@pytest.fixture(scope="function")
def browser(request):
    # Получаем значение параметра --language из командной строки
    user_language = request.config.getoption("language")
    
    # Настраиваем опции для Chrome, чтобы он открывался с нужным языком
    options = webdriver.ChromeOptions()
    options.add_experimental_option(
        'prefs', {'intl.accept_languages': user_language}
    )
    
    print(f"\nЗапуск браузера Chrome с языком: {user_language}")
    browser = webdriver.Chrome(options=options)
    
    yield browser
    
    print("\nЗакрываем браузер")
    browser.quit()