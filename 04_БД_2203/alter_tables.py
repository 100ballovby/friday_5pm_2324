import requests as req
import sqlite3


def get_list(url):
	response = req.get(url)
	res = response.json()
	return res


def create_table(cursor):
	# читаем содержимое файла с запросом SQL
	with open('create_users.sql', 'r') as file:
		sql_script = file.read()
	# выполняем запрос SQL
	cursor.executescript(sql_script)


def insert_start_values(cursor, users_list):
	with open('insert_users.sql', 'r') as file:
		sql_script = file.read()
	for i in range(len(users_list)):
		user = users[i]
		cursor.execute(sql_script,
			(user["id"], user["name"], user["username"], user["email"])
		)
		cursor.commit()


def add_column(cursor):
	with open('alter_add_column.sql', 'r') as file:
		sql_script = file.read()
	cursor.executescript(sql_script)


def update_data(cursor, addresses_list):
	with open('update_data.sql', 'r') as file:
		sql_script = file.read()
	for id, address in addresses_list:
		cursor.execute(sql_script, (address, id))
		cursor.commit()


def make_address_list(userslist):
	lst = []
	for user in userslist:
		address = user["address"]["street"] + user["address"]["suite"] + user["address"]["city"]
		tup = (user['id'], address)
		lst.append(tup)
	return lst


users = get_list('https://jsonplaceholder.typicode.com/users')

conn = sqlite3.connect('users_hw.sqlite')
# для вызова скрипта SQL, вызываем функцию и передаем ей подключение к БД
#create_table(conn)

# заполним таблицу с пользователями данными
#insert_start_values(conn, users)

# добавим новое поле в таблицу user
#add_column(conn)

ad_list = make_address_list(users)
update_data(conn, ad_list)

conn.close()
