from utils import get_data, get_executed_operations, get_sorted_operations, file_path

def main():
    '''
    Перебирает список тразакций и выводит последние 5
    :return:
    '''
    data = get_data(file_path)
    executed_operations = get_executed_operations(data)
    last_operations = get_sorted_operations(executed_operations)[:5]

    for operation in last_operations:
        print(f'{operation.get_converted_date()} {operation.get_description()}\n'
              f'{operation.get_from_operation()} -> {operation.get_to_operation()}\n'
              f'{operation.get_amount()}\n')


if __name__ == '__main__':
    main()
