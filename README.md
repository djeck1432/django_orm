# Пульт охраны банка
Это внутренний репозиторий для сотрудников банка «Сияние». Если вы попали в этот репозиторий случайно, то вы не сможете его запустить, т.к. у вас нет доступа к БД, но можете свободно использовать код вёрстки или посмотреть как реализованы запросы к БД.

Пульт охраны — это сайт, который можно подключить к удалённой базе данных с визитами и карточками пропуска сотрудников нашего банка.

# Как установить
Запросите доступ к БД у менеджера вашего банка. Для доступа вам понадобятся внести данные, которые даст вам мендержер банка в файл
```settings.py``` <br>
```DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': ****,
        'PORT': ****,
        'NAME': ****,
        'USER': ****,
        'PASSWORD': ****,
    }
}
```
Вместо ```****``` - вставте данные, которые вам передал менеджер.<br>

Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:<br>

``` git clone https://github.com/djeck1432/django_orm.git ```

После того, как скачали репозиторий, откройте в терминали(MacOs) или в консоле(Linux) папку ```django_orm``` следющей командой:<br>

```cd django_orm```

Для того, что бы запустить сайт, нужно установить необходимые библиотеки:<br>

```pip install -r requirements.txt ```

Готово, мы установили проект и все необходимые библиотеки у нас на компютере.

# Как запустить сайт 

Для того, что бы запустить сайт, выполните следующую команду в терминали(MacOs) или в консоле(Linux):<br>

```python manage.py runserver 0.0.0.0:8000 ```

В брауезере можете посмотреть на результат по ссылке :``` localhost:8000```


# Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.