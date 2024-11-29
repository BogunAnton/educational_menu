# Входные данные: текст. Результат работы алгоритма: массив анаграмм во входном тексте.
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
    letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ ' + ' ' * 7
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
    if option == 1:
        full_text = self_input_text()
        print("Вы ввели следующий текст:")
        print(full_text)
    elif option == 2:
        full_text = random_input_text()
        print("Сгенерированный случайный текст:")
        print(full_text)
    else:
        print('error')
    return True  # Возвращаем True, чтобы указать, что текст был введен

def f2():
    """ Выполнение алгоритма по заданию """
    words = full_text.split()
    anagrams = {}
    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
    result = [group for group in anagrams.values() if len(group) > 1]
    print("Алгоритм выполнен")
    return result

def f3(anagrams):
    """ Вывод результата """
    if len(anagrams) == 0:
        print("Анаграмм в тексте нет!!!")
    else:
        for group in anagrams:
            print("Анаграммы:", group)

def menu():
    anagrams = []
    text_entered = False  # Флаг для отслеживания ввода текста
    algorithm_executed = False  # Флаг для отслеживания выполнения алгоритма
    while True:
        print("Выберите пункт меню:\n"
              "1. Ввод исходного текста, вручную или сгенерированного случайным образом\n"
              "2. Выполнение алгоритма по поиску анаграмм в исходном тексте\n"
              "3. Вывод результата алгоритма\n"
              "0. Выход из цикла")
        choice = input()
        if is_int(choice):
            choice = int(choice)
        if choice == 1:
            text_entered = f1()
        elif choice == 2:
            if text_entered:
                anagrams = f2()
                algorithm_executed = True
            else:
                print("Сначала введите текст (пункт 1).")
        elif choice == 3:
            if text_entered and algorithm_executed:
                f3(anagrams)
            else:
                print("Сначала выполните пункты 1 и 2.")
        elif choice == 0:
            break
        else:
            print('error')

if __name__ == "__main__":
    menu()