Homework 21
Микросервисный склад/магазин 

Overview

Два проекта - warehouse и store.

На 30.08.2021 реализована следующая функциональность:

Warehouse:

- Созданы модели Book, Order, OrderLine
- Настроена админка для всех моделей (включая Inline для OrderLine) 

Store:

- Созданы модели Store, Book, Order, OrderLine
- Настроена админка для всех моделей (включая Inline для OrderLine)
- Настроено кеширование для вьюхи просмотра доступных книг
- Настроены следующие бизнес-процессы:
  - логин пользователя;
  - регистрация нового пользователя;
  - просмотр доступных книг (с логином и без);
  - просмотр заказов пользователя;
  - просмотр строк заказов;
  - создание заказов пользователя (пока без строк).


    В проекте Store существует дамп-файл с тестовыми данными store_app/fixtures/db.json
    Доступные пользователи: 
    "admin" with password "adm123456" - superuser
    "test" with password "tst123456" - user

    Open a browser to http://127.0.0.1:8000/admin/ to open the admin site.

    Open tab to http://127.0.0.1:8000/store_app/book/ to see book list.
