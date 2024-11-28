# 4.Входные данные: текст. Результат работы алгоритма: массив анаграмм во входном тексте.
import random

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

def self_input_text():
    # Функция, которая позволяет пользователю самостоятельно ввести текст
    print("Введите текст (для завершения ввода введите пустую строку):")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    # Объединяем все строки в один текст
    return " ".join(lines)

def random_input_text(min_length=10, max_length=1000):
    # Генерация случайного текста на русском языке
    letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ ' * 5 + ' ' * 10
    length = random.randint(min_length, max_length)  # Генерация случайной длины
    return ''.join(random.choice(letters) for _ in range(length))

def f1():
    """Функция меню для ввода текста текст"""
    global full_text
    print("Выберите опцию 1-2:\n"
          "1. Ввести текст самостоятельно\n"
          "2. Сгенерировать случайный текст\n")
    option = input()
    if is_int(option):
        option = int(option)
    if option == '1':
        full_text = self_input_text()
        print("Вы ввели следующий текст:")
        print(full_text)
    elif option == '2':
        full_text = random_input_text()
        print("Сгенерированный случайный текст:")
        print(full_text)
    else:
        print('error')

def f2(anagramms):
    """ Выполнение алгоритма по заданию """
    for i in range(len(full_text)):
        for j in range(len(full_text)):
            if i == j:
                continue
            if sorted(full_text[i]) == sorted(full_text[j]):
                anagramms = anagramms + (full_text[i],)
    print("Алгоритм выполнен")
    return anagramms

def f3(anagramms):
    """ Вывод результата """
    for word in anagramms:
        print(word)

def menu():

    anagramms = ()
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
            f2(anagramms)
        elif choice == 3:
            f3(anagramms)
        elif choice == 0:
            break
        else:
            print('error')

if __name__ == "__main__":
    menu()
