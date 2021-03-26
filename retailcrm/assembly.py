from collections import namedtuple

from retailcrm.entitysets import EntitySets
from retailcrm.engine import CrmEngine
from retailcrm.debug import Debug
from retailcrm import crm

from config import settings

debug = Debug(settings.OUTPUT)
entitysets = EntitySets(settings).entityset
engine = CrmEngine(settings, debug)

__Reference = namedtuple('Reference', [
        'sites',
        'stores',
        'statuses',
        'status_groups',    
        'payment_types',
        'order_types',
        'order_methods',
        'delivery_types',
        'delivery_services'
    ])

reference =  __Reference(
    sites = crm.Reference(entitysets['reference']['sites'], engine),
    stores = crm.Reference(entitysets['reference']['stores'], engine),
    statuses = crm.Reference(entitysets['reference']['statuses'], engine),
    status_groups = crm.Reference(entitysets['reference']['status_groups'], engine),
    payment_types = crm.Reference(entitysets['reference']['payment_types'], engine),
    order_types = crm.Reference(entitysets['reference']['order_types'], engine),
    order_methods = crm.Reference(entitysets['reference']['order_methods'], engine),
    delivery_types = crm.Reference(entitysets['reference']['delivery_types'], engine),
    delivery_services = crm.Reference(entitysets['reference']['delivery_services'], engine)
)

orders = 'orders'
customers = 'customers'
customers_corporate = 'customers_corporate'
users = 'users'
user_groups = 'user_groups'
costs = 'costs'