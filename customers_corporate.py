from core import retailcrm
import datetime

date_start = str(datetime.datetime.now().date() + datetime.timedelta(days = -1))
date_finish = str(datetime.datetime.now().date() + datetime.timedelta(days = +1))

customers_corporate = crm.CustomersCorporate()
customers_corporate.store_period(date_start, date_finish)