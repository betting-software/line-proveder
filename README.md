# line-provider

## Описание

Данный микросервис позволяет взаимодействовать с БД events, в которой хранятся данные о событиях.
Я разделил docker compose на 2 разных файла. Это связано с тем, что с БД чаще всего связаны и другие 
микросервисы, поэтому при тестировке и внесению фичей в этот микросервис, это не должно ронять БД

## Установка 

Скачайте репозиторий командой 
`git clone https://github.com/betting-software/line-provider`

Добавьте в корень проекта папку config и положите туда файл conf.env. 
Вот пример данных в файле conf.env

```
DB_HOST = "postgres-events"
DB_PORT = 5432
DB_NAME = "events"
DB_USERNAME = "postgres"
DB_PASSWORD = "postgres"
DB_TABLE_NAME = "events"

POSTGRES_DB = "events"
POSTGRES_USER = "postgres"
POSTGRES_PASSWORD = "postgres"

BET_MAKER_URL = "http://bet_maker:8000"
```

Запустите контейнер с БД events 
`docker compose -f docker-compose-postgres.yaml up`

Далее запустите контейнер с микросервисом
`docker compose -f docker-compose-core.yaml up`

После этой команды должны пройти миграции и все должно запутситься.

## Описание точек

Перейдите на свагер http://localhost:9055/docs#/

Там я реализовал 4 точки
1. /events - получение всех неоконченных событий
2. /events/{id_event} - получение 1 события по id
3. /add_events - добавление новый событий
4. /update_events - Обновление статуса события, когда событие прошло

При вызове /update_events также отправляется запрос на другой микросервис, чтобы обновить
все ставки на это событие

