# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковые строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ разные строки
        #           ignore_case = False, Aбв и АБВ одинаковые строки, одна из них удалится
        # По-умолчанию ignore_case = False

        # Проверка наличия ключевого аргумента 'ignore_case' и его значения
        if ('ignore_case' in kwargs.keys()) and (kwargs['ignore_case']):
            # Игнорирование регистра - приведение всех строк из списка к нижнему регистру
        	self.items = [str(i).lower() for i in items]
        else:
        	self.items = items
        self.index = 0
        self.used = []

    def __next__(self):
        # Нужно реализовать __next__
        # Проходим по списку использованныъэлементов - если текущего элемента в нём нет, то добавляем его и выводим
        while self.items[self.index] in self.used:
        	if self.index == len(self.items) - 1:
        	    raise StopIteration
        	self.index += 1

        self.used.append(self.items[self.index])
        return self.items[self.index]

    def __iter__(self):
        return self
