import sqlite3


conn = sqlite3.connect('new_db.sqlite')

# обновим номер телефона у пользователя с ID=1
conn.execute('UPDATE `users` SET `phone` = "+375291234567" WHERE `id` = 1')
# обновим адрес у пользователя с фамилией Johns
conn.execute('UPDATE `users` SET `address` = "Park ave 16, apt. 3" WHERE `last_name` = "Johns"')
conn.commit()  # подтвердить изменения в таблице
print(f'Total number of rows affected: {conn.total_changes}')

# выведем изменения
c = conn.execute('SELECT * FROM `users`')
for row in c:
	print(row)
