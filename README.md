# Lab 5 Web Smoke Project

Автоматизированное дымовое тестирование публичного веб-сервиса `SauceDemo`.

## Репозиторий

После публикации используйте этот URL в отчете:

`https://github.com/m2203287/lab5-web-smoke-testing`

## Что делает сценарий

1. Открывает `https://www.saucedemo.com/`.
2. Заполняет поля `username` и `password`.
3. Нажимает кнопку `Login`.
4. Проверяет загрузку страницы товаров.
5. Нажимает `Add to cart`.
6. Проверяет badge корзины.
7. Прокручивает страницу к футеру по локатору.
8. Сохраняет скриншоты в папку `artifacts/`.

## Запуск

```powershell
cd "c:\Users\mtche\Downloads\Методы тестирования и отладки\lab5\web_smoke_project"
python -m pip install -r requirements.txt
python smoke_test_saucedemo.py
```

## Артефакты

- `artifacts/01_login_page.png`
- `artifacts/02_fields_filled.png`
- `artifacts/03_inventory_page.png`
- `artifacts/04_cart_badge.png`
- `artifacts/05_footer_scroll.png`
