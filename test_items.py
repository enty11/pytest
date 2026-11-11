import time
from selenium.webdriver.common.by import By

def test_product_page_contains_add_to_cart_button(browser):
    # Открываем страницу товара
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    
    # ОБЯЗАТЕЛЬНОЕ УСЛОВИЕ: Пауза 30 секунд для визуальной проверки языка проверяющим
    time.sleep(30)
    
    # Ищем кнопку добавления в корзину. 
    # Класс "btn-add-to-basket" уникален для этой кнопки на сайте.
    button = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
    
    # Проверяем, что кнопка найдена и отображается на странице
    assert button.is_displayed(), "Кнопка добавления в корзину не найдена!"