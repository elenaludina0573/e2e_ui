# E2E UI тест для SauceDemo

Этот проект содержит тест (E2E), который моделирует процесс покупки товара на сайте [SauceDemo](https://www.saucedemo.com/). 
Тест использует Selenium  с Python для автоматизации действий в браузере, начиная от авторизации и до успешного завершения покупки.

# Структура проекта

- test_selenium.py: Основной скрипт, содержащий сценарий E2E теста.
- .venv/: Виртуальное окружение для управления зависимостями (не включено в репозиторий).
- README.md: Документация по настройке и запуску проекта.

# Инструкции по настройке

# 1. Клонируйте репозиторий

```
git clone https://github.com/elenaludina0573/e2e_ui
cd <директория_проекта>
```
# 2. Виртуальное окружение
## На Windows
```
python -m venv venv
venv\Scripts\activate
```
## На macOS/Linux:
```
python3 -m venv venv
source venv/bin/activate
```

# 3. Зависимости
Можно через requirements.txt
```
pip install -r requirements.txt
```
Или вручную 
```
pip install selenium 
selenium  install
```
# 4. Запуск
```
python test_selenium .py
```

# Сценарий теста
## Тест выполняет следующие действия:

## Авторизация: 
Использует тестовые учётные данные для входа на сайт SauceDemo.
```
Имя пользователя: standard_user
Пароль: secret_sauce
```
## Выбор товара: 
Выбирает "Sauce Labs Backpack" и добавляет его в корзину.
## Оформление покупки: 
Переходит на страницу оформления заказа и заполняет необходимые данные (имя, фамилия и почтовый индекс).
## Завершение покупки:
Завершает заказ и проверяет успешность заказа по сообщению "Thank you for your order!".

# Настройка
Вы можете изменить товар, добавляемый в корзину, или обновить другие части теста, изменив соответствующие селекторы или значения в скрипте test_playwright.py.
