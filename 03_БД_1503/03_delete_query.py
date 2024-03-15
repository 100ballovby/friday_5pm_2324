import sqlite3


conn = sqlite3.connect('new_db.sqlite')

try:
	conn.execute('''INSERT INTO `users` (`id`, `first_name`, `last_name`, `phone`, `age`, `address`)
	VALUES (6, 'Test1', 'Test1', 'Test1', 35, 'Test1');''')
	conn.execute('''INSERT INTO `users` (`id`, `first_name`, `last_name`, `phone`, `age`, `address`)
	VALUES (7, 'Test2', 'Test2', 'Test2', 36, 'Test2');''')
except:
	pass

c = conn.execute('SELECT * FROM `users`;')
for row in c:
	print(row)
# удалим пользователя с id = 6 из таблицы users
conn.execute('DELETE FROM `users` WHERE `id` = 6;')

c = conn.execute('SELECT * FROM `users`;')
for row in c:
	print(row)
