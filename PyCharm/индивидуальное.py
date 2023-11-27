#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def help1():
    """"
    Функция для вывода списка команд
    """
    # Вывести справку о работе с программой.
    print("Список команд:\n")
    print("add - добавить информацию;")
    print("list - вывести список ;")
    print("select <тип> - вывод на экран фамилия, имя; знак Зодиака; дата рождения ")
    print("help - отобразить справку;")
    print("exit - завершить работу с программой.")


def add1():
    """"
    Функция для добавления информации о новых рейсах
    """
    # Запросить данные о работнике.
    name = input("Фамилия и имя? ")
    zodiac = input("Знак зодиака? ")
    date = input("дата рождения? ")
    # Создать словарь.
    i = {
        'name': name,
        'zodiac': zodiac,
        'data': date,
    }

    return i


def error1():
    """"
    функция для неопознанных команд
    """
    print(f"Неизвестная команда {command}")


def list(birthday):
    """"
    Функция для вывода списка добавленных рейсов
    """
    # Заголовок таблицы.
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 20,
        '-' * 8
    )
    print(line)

    # Вывести данные о всех сотрудниках.
    for idx, i in enumerate(birthday, 1):
        print(
            '| {:>4} | {:<30} | {:<20} | {:>8} |'.format(
                idx,
                i.get('name', ''),
                i.get('zodiac', ''),
                i.get('data', '')
            )
        )
    print(line)


def select(command, birthday):
    """""
    Функция для получения фамилии и знака зодиака.
    """
    # Разбить команду на части для выделения номера года.
    parts = input("Введите значение: ")
    # Проверить сведения работников из списка.
    count = 0

    for i in birthday:
        for k, v in i.items():

            if v == parts:
                print("Пункт назначения - ", i["name"])
                print("знак зодиака - ", i["zodiac"])
                count += 1
    # Если счетчик равен 0, то работники не найдены.

    if count == 0:
        print("информации не найдено.")


def main():
    """"
    Главная функция программы.
    """
    print("Список команд:\n")
    print("add - добавить информацию;")
    print("list - вывести список ;")
    print("select <тип> - ввывод на экран фамилия, имя; знак Зодиака; дата рождения")
    print("help - отобразить справку;")
    print("exit - завершить работу с программой.")
    # Список работников.
    birthday = []
    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()
        # Выполнить действие в соответствие с командой.

        match command:
            case 'exit':
                break

            case 'add':
                # Добавить словарь в список.
                i = add1()
                birthday.append(i)
                # Отсортировать список в случае необходимости.
                if len(birthday) > 1:
                    birthday.sort(key=lambda item: item.get('data', ''))

            case 'list':
                list(birthday)

            case 'select':
                select(command, birthday)

            case 'help':
                help1()

            case _:
                error1()


if __name__ == '__main__':
    main()