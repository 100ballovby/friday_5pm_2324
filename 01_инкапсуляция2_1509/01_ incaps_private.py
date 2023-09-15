import string
import random


class Laptop:
    __battery_cycles = 0  # private параметр
    _serial_number = ''  # protected параметр
    def __init__(self, n):
        self.name = n  # публичный параметр
        self._set_serial_number()  # в момент создания экземпляра класса серийный номер назначается

    def charge(self):  # публичный метод
        print('Charing...')
        self.__battery_cycles += 1  # публичный метод может менять приватные параметры
        print(f'Charging cycles: {self.__battery_cycles}')

    def _set_serial_number(self):  # protected метод
        l = string.ascii_uppercase + string.digits  # весь алфавит (большие буквы) + цифры
        s_n = ''
        for i in range(10):
            s_n += random.choice(l)  # серийник собирается случайно из списка символов
        self._serial_number = s_n

    ### Добавим приватный метод для обнуления количества зарядок батареи и сервисный (защищенный) метод замены батареи
    def __reduce_battery_cycles(self):  # private метод
        self.__battery_cycles = 0  # обнуляет приватный параметр

    def _change_battery(self):
        self.__reduce_battery_cycles()


l1 = Laptop('Компьютер Андрея')
# l1.__charging_cycles = 500  # обращение к приватному параметру ничего не даст
l1.charge()
print(l1._serial_number)
l1._set_serial_number()
print(l1._serial_number)
l1._serial_number = 'привет'  # защищенным параметрам значение можно в том числе заменить вручную
print(l1._serial_number)

for i in range(1000):
    l1.charge()

# print(l1.__battery_cycles)  <- если обращаться так, то он будет кидаться ошибками
print(f'Charging cycles: {l1._Laptop__battery_cycles} before crack')
# l1._Laptop__reduce_battery_cycles()
l1._Laptop__battery_cycles = 0
print(f'Charging cycles after: {l1._Laptop__battery_cycles}')

