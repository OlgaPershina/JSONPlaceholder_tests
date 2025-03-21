from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Настройки для использования драйвера браузера
driver = webdriver.Chrome(
)  # Убедитесь, что у вас установлен ChromeDriver и он находится в PATH

# URL сайта, на который вы хотите зайти
url = "https://www.saucedemo.com"  # Замените на реальный URL страницы входа

try:
    # Открываем страницу входа
    driver.get(url)

    # Находим поля для ввода логина и пароля
    username_field = driver.find_element(
        By.username, "username")  # Замените на реальный ID поля логина
    password_field = driver.find_element(
        By.password, "password")  # Замените на реальный ID поля пароля

    # Вводим логин и пароль
    username_field.send_keys("standard_user")
    password_field.send_keys("secret_sauce")

    # Находим кнопку входа и нажимаем на нее
    login_button = driver.find_element(
        By.loginbutton,
        "login-button")  # Замените на реальный ID кнопки входа
    login_button.click()

    # Ждем некоторое время для загрузки следующей страницы
    time.sleep(5)

    # Проверяем успешный вход
    # Например, проверяем наличие определенного элемента на странице, который появляется только после входа
    success_element = driver.find_element(
        By.welcome, "welcome-message")  # Замените на реальный ID элемента
    assert success_element.is_displayed(), "Login was not successful"

    print("Test passed: Login was successful")

except Exception as e:
    print(f"Test failed: {e}")

finally:
    # Закрываем браузер
    driver.quit()
