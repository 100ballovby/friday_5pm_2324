import sqlite3


conn = sqlite3.connect('new_db.sqlite')

# запрос на выгрузку всех записей из таблицы users
c = conn.execute('SELECT * FROM `users`')
for row in c:
	print(row)

# запрос на выгрузку только Имен, фамилий и возраста из таблицы user
c = conn.execute('SELECT `first_name`, `last_name`, `age` FROM `users`')
for row in c:
	print(f'Name: {row[0]}\nSurname: {row[1]}\nAge: {row[2]}\n')

