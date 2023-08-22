import datetime
from src.classes import Operation

def test_operation_get_converted_date():
    op_date = '2023-08-22T10:30:00.000'
    operation = Operation(op_date, '', '', '', 0, '')

    converted_date = operation.get_converted_date()

    assert converted_date == '22.08.2023'

def test_operation_get_description():
    op_date = '2023-08-22T10:30:00.000'
    operation = Operation(op_date, 'Test Description', '', '', 0, '')

    description = operation.get_description()

    assert description == 'Test Description'

def test_operation_get_from_operation():
    op_date = '2023-08-22T10:30:00.000'
    op_from = 'Account Name 9876 5432 1098 7654' or 'Счет 12349876543210987654'
    operation = Operation(op_date, '', op_from, '', 0, '')

    from_operation = operation.get_from_operation()

    assert from_operation == 'Account Name 9876 54** **** 7654' or 'Cчет **7654'

def test_operation_get_to_operation():
    op_date = '2023-08-22T10:30:00.000'
    op_to = 'Account Name 9876 5432 1098 7654' or 'Счет 12349876543210987654'
    operation = Operation(op_date, '', '', op_to, 0, '')

    to_operation = operation.get_to_operation()

    assert to_operation == 'Account Name 9876 54** **** 7654' or 'Cчет **7654'

def test_operation_get_date():
    op_date = '2023-08-22T10:30:00.000'
    operation = Operation(op_date, '', '', '', 0, '')

    date = operation.get_date()

    assert date == datetime.datetime(2023, 8, 22, 10, 30)

def test_operation_get_amount():
    op_date = '2023-08-22T10:30:00.000'
    operation = Operation(op_date, '', '', '', 100.0, 'USD')

    amount = operation.get_amount()

    assert amount == '100.0 USD'
