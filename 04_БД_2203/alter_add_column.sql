ALTER TABLE `users`
ADD COLUMN `address` TEXT DEFAULT '';
/* DEFAULT указывает, что именно вы хоите добавить
   в новое поле для старых записей в таблице  */