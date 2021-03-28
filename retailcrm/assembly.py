from collections import namedtuple

from retailcrm.entitysets import EntitySets
from retailcrm.engine import CrmEngine
from retailcrm.debug import Debug
from retailcrm import crm, formats
from config import settings

debug = Debug(settings.OUTPUT)
entitysets = EntitySets(settings, formats).entityset
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
        'delivery_services',
        'cost_groups',
        'cost_items',
        'countries',
        'couriers',
        'legal_entities',
        'mg_channels',
        'payment_statuses',
        'units'
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
    delivery_services = crm.Reference(entitysets['reference']['delivery_services'], engine),

    cost_groups = crm.Reference(entitysets['reference']['cost_groups'], engine),
    cost_items = crm.Reference(entitysets['reference']['cost_items'], engine),
    countries = crm.Reference(entitysets['reference']['countries'], engine),
    couriers = crm.Reference(entitysets['reference']['couriers'], engine),
    legal_entities = crm.Reference(entitysets['reference']['legal_entities'], engine),
    mg_channels = crm.Reference(entitysets['reference']['mg_channels'], engine),
    payment_statuses = crm.Reference(entitysets['reference']['payment_statuses'], engine),
    units = crm.Reference(entitysets['reference']['units'], engine)
)

orders = crm.Entity(entitysets['orders'], engine)
customers = crm.Entity(entitysets['customers'], engine)
customers_corporate = crm.Entity(entitysets['customers_corporate'], engine)
users = crm.Users(entitysets['users'], engine)
user_groups = crm.Users(entitysets['user_groups'], engine)
costs = 'costs'