import json
import os

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

def get_executed_operations(operations:list[dict]):
    '''
    Получаем список исполненных операций
    :param operations: список словарей с транзакциями
    :return: список элементов класса Operation
    '''
    operations = [op for op in operations if op and op['state'] == 'EXECUTED']
    return operations

def get_transaction_info(account:str):
    '''
    Создаем маску для счетов
    :param account: строка с замаскированным счетом
    :return:
    '''
    account_list = account.split()
    account_name = account_list[0:-1]
    account_number = account_list[-1]
    if len(account_number) == 16:
        print(f'{" ".join(account_name)} {account_number[:4]} {account_number[4:6]}** **** {account_number[-4:]}')
    else:
        print(f'Счет **{account_number[-4:]}')

def get_sorted_operations(operations:list):
    '''
    Создаем функцию сортировки
    :param operations: список операций
    :return: сортированный список
    '''
    return sorted(operations, key=lambda op: op.get_datetime)



