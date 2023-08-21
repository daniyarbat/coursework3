import datetime


class Operation:
    def __init__(self, op_date, op_descr, op_from, op_to, op_amount, op_currency):
        '''
        Инициализация класса
        :param op_date: дата
        :param op_descr: описание
        :param op_from: операция откуда
        :param op_to: операция куда
        :param op_amount: сумма
        :param op_currency: валюта
        '''
        self.op_date = datetime.datetime.strptime(op_date, '%Y-%m-%dT%H:%M:%S.%f')
        self.op_descr = op_descr
        self.op_from = op_from
        self.op_to = op_to
        self.op_amount = op_amount
        self.op_currency = op_currency

    def __repr__(self):
        return f'{self.op_date} {self.op_descr} {self.op_from} {self.op_to} {self.op_amount} {self.op_currency}'

    def get_converted_date(self):
        '''
        Получаем дату в нужном формате
        :return: строка с датой
        '''
        return self.op_date.strftime('%d.%m.%Y')

    def get_description(self):
        '''
        Получаем описание операции
        :return: строка с описанием
        '''
        return self.op_descr

    @staticmethod
    def _get_transaction_info(account: str):
        '''
        Создаем маску для счетов
        :param account: строка с замаскированным счетом
        :return: строка с замаскированным значением
        '''
        account_list = account.split()
        account_name = account_list[0:-1]
        account_number = account_list[-1]
        if len(account_number) == 16:
            return f'{" ".join(account_name)} {account_number[:4]} {account_number[4:6]}** **** {account_number[-4:]}'
        else:
            return f'Счет **{account_number[-4:]}'

    def get_from_operation(self):
        '''
        Получает данные исходящей транзакции
        :return: Данные карты или счет
        '''
        return Operation._get_transaction_info(self.op_from)

    def get_to_operation(self):
        '''
        Получает данные входящей транзакции
        :return: Данные карты или счет
        '''
        if self.op_from is None:
            return "Нет данных"
        return Operation._get_transaction_info(self.op_to)

    def get_date(self):
        '''
        Получает дату
        :return:Дата транзакции
        '''
        return self.op_date

    def get_amount(self):
        '''
        Получает сумму пеервода
        :return: сумма и валюта перевода
        '''
        return f'{self.op_amount} {self.op_currency}'
