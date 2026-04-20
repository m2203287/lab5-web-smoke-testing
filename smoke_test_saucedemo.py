"""Smoke test for SauceDemo.

Requirements covered:
- fill input fields
- click buttons
- take screenshots
- scroll page to a locator
"""
from __future__ import annotations

from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

ARTIFACTS = Path(__file__).resolve().parent / "artifacts"
BASE_URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"


def build_driver() -> webdriver.Chrome:
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=options)


def wait(driver: webdriver.Chrome, seconds: int = 15) -> WebDriverWait:
    return WebDriverWait(driver, seconds)


def save(driver: webdriver.Chrome, name: str) -> None:
    ARTIFACTS.mkdir(exist_ok=True)
    driver.save_screenshot(str(ARTIFACTS / name))


def main() -> None:
    driver = build_driver()
    try:
        driver.get(BASE_URL)
        save(driver, "01_login_page.png")

        username = wait(driver).until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        )
        password = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")

        username.clear()
        username.send_keys(USERNAME)
        password.clear()
        password.send_keys(PASSWORD)
        save(driver, "02_fields_filled.png")

        login_button.click()
        wait(driver).until(EC.url_contains("inventory.html"))
        save(driver, "03_inventory_page.png")

        add_button = wait(driver).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
        )
        add_button.click()
        badge = wait(driver).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
        )
        assert badge.text == "1", "Badge should be 1 after adding product"
        save(driver, "04_cart_badge.png")

        footer = driver.find_element(By.CLASS_NAME, "footer_copy")
        driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'instant', block: 'center'});",
            footer,
        )
        wait(driver).until(EC.visibility_of(footer))
        save(driver, "05_footer_scroll.png")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
