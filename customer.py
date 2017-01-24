import numpy as np
import datetime
import random


class Customer(object):
    def __init__(self,
                 cust_id,
                 join_date = datetime.datetime(2000, 1, 1),
                 lifetime = 1000, transaction_avg = 100.00,
                 transaction_std = 20.00,
                 region = None,
                 daily_prob = 0.2):

        self.cust_id = cust_id
        self.join_date = join_date
        self.lifetime = datetime.timedelta(lifetime)
        self.churn_date = join_date + self.lifetime
        self.transaction_avg = transaction_avg
        self.transaction_std = transaction_std
        self.region = region
        self._multiplier = .001 ** (1 / float(lifetime))
        self._dailyprob = daily_prob


    def purchase(self, date):
        make_purchase = np.random.choice([True, False], p = [self._dailyprob, 1 - self._dailyprob])
        if make_purchase and date >= self.join_date and date <= self.churn_date:
            return round(random.gauss(self.transaction_avg, self.transaction_std), 2)
        else:
            return None


if __name__ == '__main__':
    pass
