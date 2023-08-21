import datetime


class Operation:
    def __init__(self, op_date, op_description, op_from, op_to, op_amount, op_currency):

        self.op_date = datetime.datetime.strptime(op_date, '%Y-%m-%dT%H:%M:%S.%f')
        self.op_description = op_description
        self.op_from = op_from
        self.op_to = op_to
        self.op_amount = op_amount
        self.op_currency = op_currency

    def __repr__(self):
        return f'{self.op_date} {self.op_description} {self.op_from} {self.op_to} {self.op_amount} {self.op_currency}'

