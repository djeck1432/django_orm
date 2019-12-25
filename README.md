# Пульт охраны банка
Это внутренний репозиторий для сотрудников банка «Сияние». Если вы попали в этот репозиторий случайно, то вы не сможете его запустить, т.к. у вас нет доступа к БД, но можете свободно использовать код вёрстки или посмотреть как реализованы запросы к БД.

Пульт охраны — это сайт, который можно подключить к удалённой базе данных с визитами и карточками пропуска сотрудников нашего банка.

# Переменные окружения 

 ```DB_HOST ``` - хост;
<br>
 ```DB_PORT```- порт;
<br>
 ```DB_NAME```-  имя базы данных;
<br>
 ```DB_USER```- пользователь;
<br>
 ```DB_PASSWORD```- пароль;
<br>
 ```SECRET_KEY```- секретный ключ шифрования;
<br>
 ```DEBUG```- отладочный режим (```False```- отключенный,```True```- включенный );

# Как установить

Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:<br>

``` git clone https://github.com/djeck1432/django_orm.git ```

После того, как скачали репозиторий, откройте в терминале(MacOs) или в консоли(Linux) папку ```django_orm``` следующей командой:<br>

```cd django_orm```

Для того, что бы запустить сайт, нужно установить необходимые библиотеки:<br>

```pip install -r requirements.txt ```

Готово, мы установили проект и все необходимые библиотеки у нас на компьютере.

# Как запустить сайт 

Для того, что бы запустить сайт, выполните следующую команду в терминале(MacOs) или в консоли(Linux):<br>

```python manage.py runserver 0.0.0.0:8000 ```

В браузере можете посмотреть на результат по ссылке: <a href="http://localhost:8000">http://localhost:8000</a>


# Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.
