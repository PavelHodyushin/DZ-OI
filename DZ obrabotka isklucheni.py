

def string_to_int(s):
    try:
        return int(s)
    except ValueError:
        return f"Ошибка: невозможно преобразовать '{s}' в целое число."
    finally:
        print(f"Программа string_to_int выполнена, блок FINALLY выполняется всегда!")


def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return f"Ошибка: файл '{filename}' не найден."
    except IOError:
        return f"Ошибка ввода/вывода при работе с файлом '{filename}'."
    finally:
        print(f"Программа read_file выполнена, блок FINALLY выполняется всегда!")


def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Ошибка: деление на ноль."
    except TypeError:
        return "Ошибка: аргументы должны быть числами."
    finally:
        print(f"Программа divide_numbers выполнена, блок FINALLY выполняется всегда!")


def access_list_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return f"Ошибка: индекс {index} вне диапазона списка."
    except TypeError:
        return f"Ошибка: индекс должен быть целым числом."
    finally:
        print(f"Программа access_list_element выполнена, блок FINALLY выполняется всегда!")

try:
    10 * (1/0)
except Exception:
    print('Exception - отлавливает все исключения которые входят в него!')
else:
    print('деление выполненно!')
finally:
    print('блок FINALLY выполняется всегда!!')


