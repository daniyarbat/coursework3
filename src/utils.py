import json
import os

# Получение пути к текущей директории
current_directory = os.path.dirname(os.path.abspath(__file__))

# Составление полного пути к файлу operations.json
file_path = os.path.join(current_directory, '..', 'data', 'operations.json')

def get_data(file_path):
    '''

    :param file_path: имя json файла
    :return: возвращает список
    '''
    with open(file_path, 'r', encoding='UTF-8') as file:
        data = json.load(file)
    return data
