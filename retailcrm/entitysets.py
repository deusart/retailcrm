class EntitySets(object):
    def __init__(self, settings, formats=None):
        self.source_adress = settings.SOURCE
        self.version = settings.VERSION
        self.entityset = dict()
        self.url_base = f'https://{self.source_adress}/api/{self.version}'
        self.path_base = settings.FOLDER
        self.formats = formats
        self.prepare_dict()
        self.set_urls()
        self.set_paths()
        self.set_timestamps()
        self.set_names()
        self.set_entity_id()

    def prepare_dict(self):
        self.entityset['reference'] = {
            'sites': {},
            'stores': {},
            'statuses': {},
            'status_groups': {},
            'payment_types': {},
            'order_types': {},
            'order_methods': {},
            'delivery_types': {},
            'delivery_services': {}
        }
        self.entityset['users'] = {}
        self.entityset['user_groups'] = {}
        self.entityset['costs'] = {}
        self.entityset['customers'] = {}
        self.entityset['customers_corporate'] = {}
        self.entityset['orders'] = {}

    def set_urls(self):
        self.entityset['reference']['sites']['url'] = f'{self.url_base}/reference/sites'
        self.entityset['reference']['stores']['url'] = f'{self.url_base}/reference/stores'
        self.entityset['reference']['statuses']['url'] = f'{self.url_base}/reference/statuses'
        self.entityset['reference']['status_groups']['url'] = f'{self.url_base}/reference/status-groups'
        self.entityset['reference']['payment_types']['url'] = f'{self.url_base}/reference/payment-types'
        self.entityset['reference']['order_types']['url'] = f'{self.url_base}/reference/order-types'
        self.entityset['reference']['order_methods']['url'] = f'{self.url_base}/reference/order-methods'
        self.entityset['reference']['delivery_types']['url'] = f'{self.url_base}/reference/delivery-types'
        self.entityset['reference']['delivery_services']['url'] = f'{self.url_base}/reference/delivery-services'
        self.entityset['users']['url'] = f'{self.url_base}/users'
        self.entityset['user_groups']['url'] = f'{self.url_base}/user-groups'
        self.entityset['costs']['url'] = f'{self.url_base}/costs'
        self.entityset['customers']['url'] = f'{self.url_base}/customers'
        self.entityset['customers_corporate']['url'] = f'{self.url_base}/customers-corporate'
        self.entityset['orders']['url'] = f'{self.url_base}/orders'
    
    def set_paths(self):
        self.entityset['reference']['sites']['path'] = f'{self.path_base}references\\'
        self.entityset['reference']['stores']['path'] = f'{self.path_base}references\\'
        self.entityset['reference']['statuses']['path'] = f'{self.path_base}references\\'
        self.entityset['reference']['status_groups']['path'] = f'{self.path_base}references\\'
        self.entityset['reference']['payment_types']['path'] = f'{self.path_base}references\\'
        self.entityset['reference']['order_types']['path'] = f'{self.path_base}references\\'
        self.entityset['reference']['order_methods']['path'] = f'{self.path_base}references\\'
        self.entityset['reference']['delivery_types']['path'] = f'{self.path_base}references\\'
        self.entityset['reference']['delivery_services']['path'] = f'{self.path_base}references\\'
        self.entityset['users']['path'] = f'{self.path_base}users\\'
        self.entityset['user_groups']['path'] = f'{self.path_base}user_groups\\'
        self.entityset['costs']['path'] = f'{self.path_base}costs\\'
        self.entityset['customers']['path'] = f'{self.path_base}customers\\'
        self.entityset['customers_corporate']['path'] = f'{self.path_base}customers_corporate\\'
        self.entityset['orders']['path'] = f'{self.path_base}orders\\'

    def set_names(self):
        self.entityset['reference']['sites']['name'] = 'sites'
        self.entityset['reference']['stores']['name'] = 'stores'
        self.entityset['reference']['statuses']['name'] = 'statuses'
        self.entityset['reference']['status_groups']['name'] = 'status_groups'
        self.entityset['reference']['payment_types']['name'] = 'payment_types'
        self.entityset['reference']['order_types']['name'] = 'order_types'
        self.entityset['reference']['order_methods']['name'] = 'order_methods'
        self.entityset['reference']['delivery_types']['name'] = 'delivery_types'
        self.entityset['reference']['delivery_services']['name'] = 'delivery_services'
        self.entityset['users']['name'] = 'users'
        self.entityset['user_groups']['name'] = 'user_groups'
        self.entityset['costs']['name'] = 'costs'
        self.entityset['customers']['name'] = 'customers'
        self.entityset['customers_corporate']['name'] = 'customers_corporate'
        self.entityset['orders']['name'] = 'orders'

    def set_timestamps(self):
        self.entityset['reference']['sites']['timestamp'] = False
        self.entityset['reference']['stores']['timestamp'] = False
        self.entityset['reference']['statuses']['timestamp'] = False
        self.entityset['reference']['status_groups']['timestamp'] = False
        self.entityset['reference']['payment_types']['timestamp'] = False
        self.entityset['reference']['order_types']['timestamp'] = False
        self.entityset['reference']['order_methods']['timestamp'] = False
        self.entityset['reference']['delivery_types']['timestamp'] = False
        self.entityset['reference']['delivery_services']['timestamp'] = False
        self.entityset['users']['timestamp'] = False
        self.entityset['user_groups']['timestamp'] = False
        self.entityset['costs']['timestamp'] = False
        self.entityset['customers']['timestamp'] = False
        self.entityset['customers_corporate']['timestamp'] = False
        self.entityset['orders']['timestamp'] = True
    
    def set_entity_id(self):
        self.entityset['reference']['sites']['entity_id'] = 'sites'
        self.entityset['reference']['stores']['entity_id'] = 'stores'
        self.entityset['reference']['statuses']['entity_id'] = 'statuses'
        self.entityset['reference']['status_groups']['entity_id'] = 'statusGroups'
        self.entityset['reference']['payment_types']['entity_id'] = 'paymentTypes'
        self.entityset['reference']['order_types']['entity_id'] = 'orderTypes'
        self.entityset['reference']['order_methods']['entity_id'] = 'orderMethods'
        self.entityset['reference']['delivery_types']['entity_id'] = 'deliveryTypes'
        self.entityset['reference']['delivery_services']['entity_id'] = 'deliveryServices'
        self.entityset['users']['entity_id'] = 'False'
        self.entityset['user_groups']['entity_id'] = 'False'
        self.entityset['costs']['entity_id'] = 'False'
        self.entityset['customers']['entity_id'] = 'False'
        self.entityset['customers_corporate']['entity_id'] = 'False'
        self.entityset['orders']['entity_id'] = 'True'

    def set_formats(self):
        self.entityset['reference']['sites']['format'] = self.formats.sites
        self.entityset['reference']['stores']['format'] = self.formats.stores
        self.entityset['reference']['statuses']['format'] = self.formats.statuses
        self.entityset['reference']['status_groups']['format'] = self.formats.status_groups
        self.entityset['reference']['payment_types']['format'] = self.formats.payment_types
        self.entityset['reference']['order_types']['format'] = self.formats.order_types
        self.entityset['reference']['order_methods']['format'] = self.formats.order_methods
        self.entityset['reference']['delivery_types']['format'] = self.formats.delivery_types
        self.entityset['reference']['delivery_services']['format'] = self.formats.delivery_services
        self.entityset['users']['format'] = 'False'
        self.entityset['user_groups']['format'] = 'False'
        self.entityset['costs']['format'] = 'False'
        self.entityset['customers']['format'] = 'False'
        self.entityset['customers_corporate']['format'] = 'False'
        self.entityset['orders']['format'] = 'True'