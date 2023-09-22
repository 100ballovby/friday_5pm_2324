class Book:
    def __init__(self):
        self.__title = ''
        self.__author = ''
        self.__year = 0
        self.__is_available = True

    def set_title(self, title):
        self.__title = title

    def get_title(self):
        return self.__title

    """остальные по той же схеме создаются"""
    def switch_avail(self):
        if self.__is_available:  # если книжка доступна для выдачи
            self.__is_available = False  # переключаем ее доступность в False
            print('книга не доступна для выдачи (уже выдана)')
        else:  # если книга не доступна, то при вызове этого метода
            self.__is_available = True  # переключаем ее доступность в True
            print('книга доступна для выдачи')

b1 = Book()
b1.set_title('Dandelion wine')
b1.switch_avail()
b1.switch_avail()

