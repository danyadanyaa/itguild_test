# itguild_test


1. Написать генератор чисел **от 0 до 1000**, если число делится только на 3 вывести **"Марко"**, если только на 5 - **"Полло"**, если делится и на 3, и на 5 - обе фразы. Если число не подходит ни под одно из условий, выводить его.  
**_Решение_**: в файле generator.py представлено две функции, одна работает как функция которая принимает значение и выводит результат в зависимости от числа, вторая функция реализована как генератор.
2. Написать REST-сервис, который будет использовать код из 1. Должны быть методы делающие следующее:
    1) Выдать ответ **Марко\Полло\МаркоПолло** или число на отправленное число
    2) Выдать список ответов состоящий из **Марко\Полло\МаркоПолло** или число на отправленный массив чисел
    3) Выдать список ответов  состоящий из **Марко\Полло\МаркоПолло** или число на отправленные промежуток [a, b]

    Также, следует ограничить сервис авторизацией и написать для этого клиент.  
    **_Решение_**: в папке itguild реализован django rest service(для его функционирования необходимо создать .env в директории "itguild/" с переменной "SECRET_KEY=")  
    Доступны следующие эндпоинты:  
    ```
        ip:port/admin  # доступ к панели администратора  
        ip:port/api/token  # эндпоинт для получение JWT токена  
        ip:port/api/token/refresh  #  эндпоинт для обновление JWT токена  
        ip:port/api/markopolo  # эндпоинт с решением задачи  
        ip:port/api/users  # POST запрос на данный эндпоинт позволяет зарегистрироваться, GET запрос выводит данные обо всех пользователях пользователе
    ```
3. Написать websocket-сервер, который будет использовать код из 1 и отвечать на команды, аналогичные по результату методам REST-сервиса из пункта 2. Также, написать тестовый клиент (можно консольный) для демонстрации работа сервера.  
**_Решение_**: в папке Websocket/ расположены файлы сервера и клиента в которых реализован описанный выше функционал  
4. Используя любую удобную библиотеку получить топ 5 фильмов с IMDB\Кинопоиск\любого другого подобного сервиса с фильмами (по выбору)  
**_Решение_**: в файле parser.py реализован функционал парсинга 5 первых фильмов с IMDB
