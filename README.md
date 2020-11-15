# Проект многофакторной аунтефикации
===============================================================

## Для работы нейронной сети проведите данные действия:
#### 1.Установить Microsoft Visual Studio C++ и Инструменты Visual C++ для CMake
#### 2.Следующее, что вам нужно сделать, это установить CMake. 
#### Перейдите на страницу загрузки CMake (https://cmake.org/download/), загрузите установщик (Windows win64-x64 Installer) и запустите установку.
#### При установке обязательно добавьте CMake в системный путь.
#### 3.Установить Anaconda (https://www.anaconda.com/products/individual)
#### 4.После установки Anaconda, открываем Anaconda Prompt и прописываем следующие команды 
#### conda create --name dlib-py37 python=3.7 anaconda
#### conda create --name dlib-py37 python=3.7 anaconda opencv tensorflow-gpu
#### conda activate dlib-py37
#### pip install pywin32
#### pip install dlib

#### Если не получается установить dlib прописываем эту команду conda install -c conda-forge dlib  

## Для работы бота, отрисовки интерфейса и работы с БД установите данные библиотеки в python:
#### telebot (pip install pyTelegramBotAPI)
#### psycopg2 (pip install psycopg2)
#### schedule (pip install schedule)
#### multiprocessing (pip install multiprocess)
#### tkinter (pip install tkintertable)
#### easygui (pip install easygui)

  
### Для регистрации прописываем в консоль в корне проекта команду python registration.py 
### Для авторизации открывает две консоли и прописываем в первую python bottemp.py 
### Во вторую прописываем python login.py
### Для более удобной работы с ботом его лучше сделать службой (примерный [гайд](https://admin-gu.ru/os/windows/upravlenie-sluzhbami-v-windows-iz-konsoli-upravleniya-mmc-i-komandnoj-stroki-utilita-sc) 

## Создание БД:
### Скачиваете программу [postgresql 13](https://www.enterprisedb.com/postgresql-tutorial-resources-training?cid=437)
### Пароль ставите 12345678 или который вам удобно, но в файле config меняете значение пароля на свой
### По очереди прописать в SQL shell:
### CREATE DATABASE moreauth;
### \c moreauth;
```
CREATE TABLE users
(
    id integer NOT NULL PRIMARY KEY,
    login text  ,
    paswrd text ,
    messenger text ,
    is_login_today boolean,
    key_messenger text ,
    id_user_messenger integer,
    face double precision[],
    first_name text 
)
```

## Для работы бота:
### Находите в телеграмме аккаунт @BotFather
### Пишете /start
### Проходите все нужные вам действия
### Выключаете возможность добавлять бота в группы(в настройках BotFather)
### Копируете выданный вам токен и вставляете его в файле config в поле TOKEN
