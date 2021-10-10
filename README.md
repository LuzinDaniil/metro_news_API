# Metro API

Программа предназначена для получения новостей за заданный период.

## Запуск

### Docker


<details><summary><b>Показать</b></summary><br>

1. Перейти в директорию 'metro' и выполнить скрипт

```shell script
docker build -t metro_api .
```
2. Запусить контейнер

```shell script
docker run -p 5000:5000 metro_api
```

</details>

### Локально в linux

<details><summary><b>Показать</b></summary><br>

1. Перейти в директорию 'metro' и активировать env

```shell script
source venv2/bin/acivate
```

2. Запустить скрипт

```shell script
python app.py
```

</details>

### Переменные

PORT_SERVER - порт 

TIMEOUT_PARSE - timeout парисинга сайта

### API взаимодейтсвие описано в файле swagger.yml
