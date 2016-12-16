#!/usr/bin/env python3
import os.path
import json
import sys
from librip.ctxmngrs import timer
from librip.decorators import print_result
from librip.gen import field, gen_random
from librip.iterators import Unique as unique

path = os.path.abspath(sys.argv[1])

# Здесь необходимо в переменную path получить
# путь до файла, который был передан при запуске

with open(path, encoding="utf8") as f:
    data = json.load(f)

# Функция для вывода отсортированного списка профессий без повторений
def f1(arg):
    return(sorted([i for i in unique([j['job-name'] for j in arg], ignore_case = True)]))

# Функция для отбора профессий со словом "программист" в начале
def f2(arg):
	return(filter(lambda x: (x.lower().find('программист') == 0), arg))

# Функция модификации профессии
def f3(arg):
    return(["{} {}".format(x, "с опытом Python") for x in arg])

# Функция генерации размера зарплаты для профессий
@print_result
def f4(arg):
    return(["{}, {} {} {}".format(x,"зарплата", y, "руб.") for x, y in zip(arg, list(gen_random(100000, 200000, len(arg))))])


with timer():
	f4(f3(f2(f1(data))))
