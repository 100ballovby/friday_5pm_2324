SELECT movies.title, directors.name
FROM movies
INNER JOIN directors  /* привязываю таблицу с режиссерами */
ON movies.director_id = directors.id;  /* по условию: id режиссера из
                                                    таблицы movies совпадает c id
                                                    режиссера из таблицы режиссеров */


