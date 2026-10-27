# Проверка и поиск почтовых индексов (6 цифр)
import re
import requests


def is_valid_index(text):
    # Проверяем что 6 цифр
    if len(text) == 6 and text.isdigit():
        return True
    return False


def find_indexes_in_text(text):
    # Ищем в тексте любые группы из 6 цифр подряд
    potential = re.findall(r'\b\d{6}\b', text)
    # Отбираем только те что прошли проверку
    correct = []
    for item in potential:
        if is_valid_index(item):
            correct.append(item)
    return correct


def main():
    print("Проверка почтовых индексов")
    print("1 - Ввести с клавиатуры")
    print("2 - Прочитать из файла")
    print("3 - Найти на сайте")

    choice = input("Выберите пункт (1, 2 или 3): ")

    if choice == "1":
        val = input("Введите индекс для проверки: ")
        if is_valid_index(val):
            print("ИНДЕКС КОРРЕКТЕН")
        else:
            print("ОШИБКА: индекс должен состоять из 6 цифр")

    elif choice == "2":
        path = input("Введите имя файла (например, test.txt): ")
        try:
            f = open(path, "r", encoding="utf-8")
            content = f.read()
            f.close()
            result = find_indexes_in_text(content)
            print("Найденные индексы:", result)
        except Exception as ex:
            print("Не удалось открыть файл:", ex)

    elif choice == "3":
        url = input("Введите адрес сайта: ")
        try:
            resp = requests.get(url)
            result = find_indexes_in_text(resp.text)
            print("Найденные на сайте индексы:", result)
        except Exception as ex:
            print("Ошибка при запросе к сайту:", ex)

    else:
        print("Такого пункта нет")


if __name__ == "__main__":
    main()