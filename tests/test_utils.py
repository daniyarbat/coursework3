import pytest

from src.utils import file_path, get_data, get_executed_operations, get_sorted_operations
from src.classes import Operation


def test_get_data():
    data = get_data(file_path)
    assert isinstance(data, list)
    assert len(data) > 0

def test_get_executed_operations():
    sample_data = [
        {"state": "EXECUTED", "date": "2023-08-22T10:30:00.000", "description": "Test 1", "from": "Account 1", "to": "Account 2", "operationAmount": {"amount": 100.0, "currency": {"name": "USD"}}},
        {"state": "CANCELED", "date": "2023-08-22T11:30:00.000", "description": "Test 2", "from": "Account 2", "to": "Account 3", "operationAmount": {"amount": 50.0, "currency": {"name": "EUR"}}},
    ]

    executed_operations = get_executed_operations(sample_data)
    assert len(executed_operations) == 1
    assert executed_operations[0].get_description() == "Test 1"

def test_get_sorted_operations():
    sample_operations = [
        Operation('2023-08-22T10:30:00.000', 'Test 1', 'Account 1', 'Account 2', 100.0, 'USD'),
        Operation('2023-08-22T11:30:00.000', 'Test 2', 'Account 2', 'Account 3', 50.0, 'EUR'),
    ]

    sorted_operations = get_sorted_operations(sample_operations)
    assert len(sorted_operations) == 2
    assert sorted_operations[0].get_description() == "Test 2"
