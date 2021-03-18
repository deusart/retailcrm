from core import crm
import datetime

date_start = str(datetime.datetime.now().date() + datetime.timedelta(days = -1))
date_finish = str(datetime.datetime.now().date() + datetime.timedelta(days = +1))

orders = crm.Orders()
orders.store_period(date_start, date_finish)
# orders.store_id(234584)
# orders.save_json_pages(1, 300)