import datetime
import random
import pandas as pd
import numpy as np
from customer import Customer


class TransactionList(object):
    def __init__(self,
                 num_customers = 1000,
                 num_transactions = 50000,
                 avg_customer_lifetime = 1000,
                 avg_customer_transaction = 100.00,
                 start_date = datetime.datetime(2000, 1, 1),
                 end_date = datetime.datetime.now()):

        self.num_customers = num_customers
        self.num_transactions = num_transactions
        self.avg_customer_lifetime = avg_customer_lifetime
        self.avg_customer_transaction = avg_customer_transaction
        self.start_date = start_date
        self.end_date = end_date
        self.customers = None
        self.transaction_list = None



    def build_customer_set(self):
        self.customers = set()
        for i in xrange(self.num_customers):
            join_year, join_month, join_day = random.randint(self.start_date.year - 5, self.end_date.year), \
                                              random.randint(1, 12), \
                                              random.randint(1, 28)

            self.customers.add(Customer(cust_id = i,
                                        join_date = datetime.datetime(join_year, join_month, join_day),
                                        lifetime = random.gauss(self.avg_customer_lifetime, 300),
                                        transaction_avg = random.gauss(self.avg_customer_transaction, 20.00),
                                        transaction_std = 20.00))


    def build_transaction_list(self):
        transactions_left = self.num_transactions
        total_days = (self.end_date - self.start_date).days

        self.transaction_list = []
        while transactions_left > 0:
            for i in xrange(total_days + 1):
                current_day = self.start_date + datetime.timedelta(i)
                for customer in self.customers:
                    transaction = customer.purchase(current_day)
                    if transaction:
                        self.transaction_list.append([current_day, customer.cust_id, transaction])
                        transactions_left -= 1


    def to_df(self):
        df = pd.DataFrame(self.transaction_list)
        df.columns = ['date', 'cust_id', 'amount']
        return df



if __name__ == '__main__':
    t = TransactionList()
    t.build_customer_set()
    t.build_transaction_list()
    df = t.to_df()
