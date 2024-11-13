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
    print("Введите текст (для завершения ввода введите пустую строку):")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    # Объединяем все строки в один текст
    global full_text
    full_text = " ".join(lines)

def f2(anagramms):
    """ Выполнение алгоритма по заданию """
    for i in range(len(full_text)):
        for j in range(len(full_text)):
            if i == j:
                continue
            if full_text[i] == full_text[j]:
                anagramms = anagramms + (full_text[i],)
    return anagramms

def f3(anagramms):
    """ Вывод результата """
    for word in anagramms:
        print(word)

def menu():
    global anagramms
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