# chatQT - чат для общения

###### Проект создан для того, чтобы познакомиться с сокетами и вспомнить pyqt:)

### Главное окно приложения

![Главное окно](https://github.com/neeearina/chatQT/raw/main/screens/main.jpg)

### Окно чата

![Окно чата](https://github.com/neeearina/chatQT/raw/main/screens/chat.jpg)

# Инструкция по запуску

### Склонируйте репозиторий с помощью git команды:

```commandline
git clone https://github.com/neeearina/eduAPI.git
```

### Создайте виртуальное окружение и активируйте его:

```commandline
python3 -m venv venv 
```

```commandline
source venv/bin/activate 
```

### Установите зависимости проекта:

```commandline
pip install -r requirements.txt
```

### Перейдите в папку с основными фалами:

```commandline
cd app
```

### Запустите код сервера:

```commandline
python server.py
```

### Откройте новый терминал и запустите файл с кодом приложения:

```commandline
python client.py
```

###### После открытия главного окна введите свое имя в поле и нажмите *start*.

###### После открытия чата можно писать и отправлять сообщения.

###### Для теста двух чатов можно еще запустить файл *test_client*;)

# Заметки

1. Организовать запуск через docker контейнер
2. Кнопка *изменить цвет* пока что ничего не делает, кроме того, что меняет цвет при нажатии
