import requests as req
import sqlite3


def get_list(url):
	response = req.get(url)
	res = response.json()
	return res


users = get_list('https://jsonplaceholder.typicode.com/users')

conn = sqlite3.connect('users_hw.sqlite')
conn.execute('''CREATE TABLE IF NOT EXISTS `users`
(`id` INT PRIMARY KEY NOT NULL,
`name` TEXT NOT NULL,
`username` TEXT NOT NULL,
`email` TEXT NOT NULL
);''')

for i in range(len(users)):
	user = users[i]
	print(user)
	conn.execute('''INSERT INTO `users` (`id`, `name`, `username`, `email`)
		VALUES (?, ?, ?, ?);''',
	             (user["id"], user["name"], user["username"], user["email"])
	             )

conn.close()
