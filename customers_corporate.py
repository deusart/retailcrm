import retailcrm
import datetime

customers_corporate = retailcrm.v5.customers_corporate

date_start = str(datetime.datetime.now().date() + datetime.timedelta(days = -1))
date_finish = str(datetime.datetime.now().date() + datetime.timedelta(days = +1))

customers_corporate.store_period(date_start, date_finish)