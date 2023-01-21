import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_add_to_basket_available_for_different_languages(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
    
    browser.get(link)
    WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn-add-to-basket"))
        )
   
    button = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")

    assert button.is_displayed() is True, "Нет кнопки для добавления в карзину"
    button_text = button.text
    print(f"Текст на кнопке для добавления в карзину: {button_text}")
    