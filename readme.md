# Бот для discord с интеграцеий различных сервисов

Предназачен для использования на одном сервере

## Для работы необходимо

1. Добавить файл config.py c переменными:  

    * token = токен бота;
    * sign = знак перед командой (н-р: !);
    * repo_url = н-р: <https://api.github.com/repos/:owner/:repo/commits>;
    * gmt = Часовой пояс (н-р: 3);
    * datetime_format = 'формат форматирования даты (н-р: %H:%M %d-%m-%y)';
    * admin_role = 'название роли на сервере, для которой будут разрешены команды (н-р: @everyone)'.

2. Добавить файлы watch.txt и watched.txt
3. Установить зависмости:

    * [discordpy](https://pypi.org/project/discord.py/)
    * [numpy](https://pypi.org/project/numpy/)
    * [pandas](https://pypi.org/project/pandas/)

## Команды

Фильмы:

* film_get - выводит случайный фильм из списка просмотра;
* films_last * - вывод определённого числа последних фильмов;
* film_add - добавить фильм в список просмотра;
* film_watched - установка фильма в режим 'просмотрен'.
* google_key
* google_search_id

Github:

* dev - вывод информации о репозитории.
