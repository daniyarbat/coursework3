import json
import os
from classes import Operation


# Получение пути к текущей директории
current_directory = os.path.dirname(os.path.abspath(__file__))

# Составление полного пути к файлу operations.json
file_path = os.path.join(current_directory, '..', 'data', 'operations.json')


def get_data(file_path):
    '''
    Получаем данные из файла
    :param file_path: имя json файла
    :return: возвращает список
    '''
    with open(file_path, 'r', encoding='UTF-8') as file:
        data = json.load(file)
    return data


def get_executed_operations(operations: list[dict]):
    '''
    Получаем список исполненных операций
    :param operations: список словарей с транзакциями
    :return: список элементов класса Operation
    '''
    operations = [op for op in operations if op and op['state'] == 'EXECUTED']
    return [
        Operation(
            op["date"],
            op["description"],
            op.get("from", None),
            op["to"],
            op["operationAmount"]["amount"],
            op["operationAmount"]["currency"]["name"]
        )
        for op in operations
    ]


def get_sorted_operations(operations: list[Operation]):
    '''
    Создаем функцию сортировки
    :param operations: список операций
    :return: сортированный список
    '''
    return sorted(operations, key=lambda op: op.get_date(), reverse=True)
