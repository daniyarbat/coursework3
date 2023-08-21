import pytest

from src.utils import get_data, get_executed_operations, get_sorted_operations

# Тестирование get_data
def test_get_data():
    data = get_data(file_path)
    assert isinstance(data, list)
    assert len(data) > 0
    # Дополнительные проверки по вашему выбору

# Тестирование get_executed_operations
def test_get_executed_operations():
    data = get_data(file_path)
    operations = get_executed_operations(data)
    assert len(operations) > 0
    assert all(op.get_date() is not None for op in operations)
    assert all(op.get_description() == "Перевод организации" for op in operations)
    # Дополнительные проверки по вашему выбору

# Тестирование get_sorted_operations
def test_get_sorted_operations():
    data = get_data(file_path)
    operations = get_executed_operations(data)
    sorted_operations = get_sorted_operations(operations)
    assert len(sorted_operations) == len(operations)
    # Проверьте, что операции упорядочены по убыванию даты
    assert all(sorted_operations[i].get_date() >= sorted_operations[i+1].get_date() for i in range(len(sorted_operations)-1))
    # Дополнительные проверки по вашему выбору