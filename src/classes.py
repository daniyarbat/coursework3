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



