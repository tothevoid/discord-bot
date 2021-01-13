# Бот для discord с интеграцеий различных сервисов

Предназачен для использования на одном сервере

## Для работы необходимо

1. Настроить config.py:  

    * token - [токен бота discord](https://discord.com/developers/applications/)
    * cmd_prefix - знак перед командой (н-р: !);
    * repo_url - репозиторий бота (н-р: <https://api.github.com/repos/:owner/:repo/commits>);
    * gmt - часовой пояс (н-р: 3);
    * datetime_format - паттерн даты (н-р: %H:%M %d-%m-%y);
    * admin_role - название роли на сервере, для которой будут разрешены команды (н-р: @everyone);
    * google_key - google api-токен;
    * google_search_id - id поисковой системы (для поиска по конкретному сайту) <https://cse.google.com/cse/create/new>.

2. Установить зависмости:

    Автоматически:
        pip install -r ./requirements.txt

    Вручную:

    * [discordpy 1.6.0](https://pypi.org/project/discord.py/1.6.0/)
    * [numpy 1.16.2](https://pypi.org/project/numpy/1.16.2/)
    * [pandas 0.24.2](https://pypi.org/project/pandas/0.24.2/)

## Команды

Фильмы:

* film_get - выводит случайный фильм из списка просмотра;
* films_last * - вывод определённого числа последних фильмов;
* film_add - добавить фильм в список просмотра;
* film_watched - установка фильма в режим 'просмотрен'.
* films_all - выводит все добавленные фильмы

Github:

* dev - вывод информации о репозитории.
