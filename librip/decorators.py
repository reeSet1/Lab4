# Здесь необходимо реализовать декоратор, print_result который принимает на вход функцию,
# вызывает её, печатает в консоль имя функции, печатает результат и возвращает значение
# Если функция вернула список (list), то значения должны выводиться в столбик
# Если функция вернула словарь (dict), то ключи и значения должны выводить в столбик через знак равно
def print_result(func_arg):
    def decorated_func(*args):
        print(func_arg.__name__)
        # Если возвращает список - печатать в столбик
        if type(func_arg(*args)) == list:
            for i in func_arg(*args):
                print(i)
        # Если словарь - печатать парами ключ-значение
        elif type(func_arg(*args)) == dict:
            for key, val in func_arg(*args).items():
                print('{} = {}'.format(key, val))
        # Во всех прочих случаях - выводить результат как есть
        else:
            print(func_arg(*args))
    return decorated_func
