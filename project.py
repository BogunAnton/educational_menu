# 4.Входные данные: текст. Результат работы алгоритма: массив анаграмм во входном тексте.
def is_int(choice):
    """ Проверка на то, что s - целое число"""
    try:
        if type(choice) is int:
            return True
        if choice is None:
            return False
        if not choice.isdecimal():
            return False
        int(choice)
        return True
    except (Exception, ValueError, TypeError):
        return False

def f1():
    """Функция, которая позволяет пользователь ввести или сгенерировать текст"""
    return "образец"

def f2():
    """ Выполнение алгоритма по заданию """
    return "образец"

def f3():
    """ Вывод результата """
    return "образец"

def menu():
    while True:
        print("Выберите пункт меню:\n"
              "1. Ввод исходного текста, вручную или сгенерированного случайным образом\n"
              "2. Выполнение алгоритма по поиску анограмм в исходном тексте\n"
              "3. Вывод результата алгоритма\n"
              "0. Выход из цикла")
        choice = input()
        if is_int(choice):
            choice = int(choice)
        if choice == 1:
            f1()
        elif choice == 2:
            f2()
        elif choice == 3:
            f3()
        elif choice == 0:
            break
        else:
            print('error')

if __name__ == "__menu__":
    menu()