import retailcrm
import datetime

orders = retailcrm.v5.customers_corporate

date_start = str(datetime.datetime.now().date() + datetime.timedelta(days = -20))
date_finish = str(datetime.datetime.now().date() + datetime.timedelta(days = +1))

orders.store_period(date_start, date_finish)