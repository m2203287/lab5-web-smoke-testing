# Lab 5 Web Smoke Project

Автоматизированное дымовое тестирование публичного веб-сервиса `SauceDemo`
(Selenium WebDriver + webdriver-manager).

## Репозиторий

`https://github.com/m2203287/lab5-web-smoke-testing`

## Что делает сценарий

1. Открывает `https://www.saucedemo.com/`.
2. Заполняет поля `username` и `password`.
3. Нажимает кнопку `Login`.
4. Проверяет загрузку страницы товаров.
5. Нажимает `Add to cart` и проверяет badge корзины.
6. Прокручивает страницу к футеру по локатору `footer_copy`.
7. Сохраняет скриншоты в папку `artifacts/`.

## Запуск

```powershell
cd "c:\Users\mtche\Downloads\Методы тестирования и отладки\lab5\web_smoke_project"
python -m pip install -r requirements.txt
python smoke_test_saucedemo.py
```

## Результат прогона

Сценарий отработал без ошибок и сгенерировал 5 скриншотов. Дополнительный
снимок `06_terminal.png` — подтверждение успешного запуска из терминала.

| Файл | Шаг | Что зафиксировано |
| --- | --- | --- |
| `artifacts/01_login_page.png` | Старт | Открыта страница авторизации |
| `artifacts/02_fields_filled.png` | Ввод | Поля `username` и `password` заполнены |
| `artifacts/03_inventory_page.png` | После Login | Загружена страница `inventory.html` |
| `artifacts/04_cart_badge.png` | Add to cart | Появился badge корзины со значением 1 |
| `artifacts/05_footer_scroll.png` | Скролл | Страница прокручена к `footer_copy` |
| `artifacts/06_terminal.png` | Запуск | Терминал: сценарий завершился без исключений |
