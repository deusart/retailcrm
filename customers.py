import retailcrm
import datetime

customers = retailcrm.v5.customers

date_start = str(datetime.datetime.now().date() + datetime.timedelta(days = -1))
date_finish = str(datetime.datetime.now().date() + datetime.timedelta(days = +1))

customers.store_period(date_start, date_finish)