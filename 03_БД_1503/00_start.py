import sqlite3


conn = sqlite3.connect('new_db.sqlite')
print('Connected')

conn.execute('''CREATE TABLE IF NOT EXISTS `users`
(`id` INT PRIMARY KEY NOT NULL,
`first_name` TEXT NOT NULL,
`last_name` TEXT NOT NULL,
`phone` TEXT NOT NULL,
`age` INT NOT NULL,
`address` CHAR(50)
);''')  # запрос на создание таблицы с полями id, first_name, last_name, phone, age и address
print('Table created!')

conn.execute('''INSERT INTO `users` (`id`, `first_name`, `last_name`, `phone`, `age`, `address`)
VALUES (3, 'Paul', 'Lagerfeld', '+74992550189', 22, 'Pol st. 22, apt 67');''')
# запросы на добавление новых данных в таблицу
conn.execute('''INSERT INTO `users` (`id`, `first_name`, `last_name`, `phone`, `age`, `address`)
VALUES (4, 'Kelly', 'Johns', '+228993428201', 29, 'Kale av. 5, apt 28');''')
conn.execute('''INSERT INTO `users` (`id`, `first_name`, `last_name`, `phone`, `age`, `address`)
VALUES (5, 'Brad', 'Nolan', '+5777229222', 90, 'Jupyter st. 12, suite 22');''')
conn.commit()
conn.close()
