from core import crm
import datetime

date_start = str(datetime.datetime.now().date() + datetime.timedelta(days = -1))
date_finish = str(datetime.datetime.now().date() + datetime.timedelta(days = +1))

customers = crm.Customers()
customers.store_period(date_start, date_finish)