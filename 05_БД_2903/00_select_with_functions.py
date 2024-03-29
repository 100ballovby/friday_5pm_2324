import sqlite3


db = sqlite3.connect('movie.sqlite')
cur = db.cursor()

cur.execute('SELECT `original_title`, `release_date`, `popularity` FROM `movies`;')  # выбрать все записи из таблицы movies
movies = cur.fetchall()  # преобразует все строки в список и сохрнает в переменной
for movie in movies:
	print(movie)


cur.execute('SELECT COUNT(*) FROM `movies` WHERE `popularity` > 300 AND `budget` > 158000000')
# этот запрос посчитает КОЛИЧЕСТВО фильмов, у которых в поле popularity значение больше 700
count_popul = cur.fetchall()
print(count_popul)

cur.execute('SELECT AVG(`budget`) FROM `movies`;')
avg_bud = cur.fetchall()
print(f'Average film budget is ${round(avg_bud[0][0], 2)}')

cur.execute('SELECT MAX(`budget`), MIN(`budget`), AVG(`budget`) FROM `movies`;')
budgets = cur.fetchall()
print(f'The max budget is ${budgets[0][0]}')
print(f'The min budget is ${budgets[0][1]}')
print(f'Average films budget is ${round(budgets[0][2], 2)}')

# я хочу найти всех режиссеров, имена которых начинаются на А
cur.execute('SELECT `id`, `name` FROM `directors` WHERE `name` LIKE "A%";')
direct = cur.fetchall()
print(direct)
# я хочу найти всех режиссеров, имена которых заканчиваются на nd
cur.execute('SELECT `id`, `name` FROM `directors` WHERE `name` LIKE "%and";')
direct = cur.fetchall()
print(direct)
# я хочу найти всех режиссеров, имена которых СОДЕРЖАТ строчку Nick или строчку Jackson
cur.execute('SELECT `id`, `name` FROM `directors` '
            'WHERE `name` '
            'LIKE "%Nick%" OR `name` LIKE "%Jackson%";')
direct = cur.fetchall()
print(direct)
