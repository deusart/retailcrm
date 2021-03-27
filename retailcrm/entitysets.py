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
        self.set_formats()
        self.set_entity_id()
        self.set_entity()

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
            'delivery_services': {},
            # new
            'cost_groups': {},
            'cost_items': {},
            'countries': {},
            'couriers': {},
            'legal_entities': {},
            'mg_channels': {},            
            'payment_statuses': {},
            'units': {}
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
        #new
        self.entityset['reference']['cost_groups']['url'] = f'{self.url_base}/reference/cost-groups'
        self.entityset['reference']['cost_items']['url'] = f'{self.url_base}/reference/cost-items'
        self.entityset['reference']['countries']['url'] = f'{self.url_base}/reference/countries'
        self.entityset['reference']['couriers']['url'] = f'{self.url_base}/reference/couriers'
        self.entityset['reference']['legal_entities']['url'] = f'{self.url_base}/reference/legal-entities'
        self.entityset['reference']['mg_channels']['url'] = f'{self.url_base}/reference/mg-channels'
        self.entityset['reference']['payment_statuses']['url'] = f'{self.url_base}/reference/payment-statuses'
        self.entityset['reference']['units']['url'] = f'{self.url_base}/reference/units'

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
        #new
        self.entityset['reference']['cost_groups']['path'] = f'{self.path_base}references\\'
        self.entityset['reference']['cost_items']['path'] = f'{self.path_base}references\\'
        self.entityset['reference']['countries']['path'] = f'{self.path_base}references\\'
        self.entityset['reference']['couriers']['path'] = f'{self.path_base}references\\'
        self.entityset['reference']['legal_entities']['path'] = f'{self.path_base}references\\'
        self.entityset['reference']['mg_channels']['path'] = f'{self.path_base}references\\'
        self.entityset['reference']['payment_statuses']['path'] = f'{self.path_base}references\\'
        self.entityset['reference']['units']['path'] = f'{self.path_base}references\\'

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
        #new
        self.entityset['reference']['cost_groups']['name'] = 'cost_groups'
        self.entityset['reference']['cost_items']['name'] = 'cost_items'
        self.entityset['reference']['countries']['name'] = 'countries'
        self.entityset['reference']['couriers']['name'] = 'couriers'
        self.entityset['reference']['legal_entities']['name'] = 'legal_entities'
        self.entityset['reference']['mg_channels']['name'] = 'mg_channels'
        self.entityset['reference']['payment_statuses']['name'] = 'payment_statuses'
        self.entityset['reference']['units']['name'] = 'units'

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
        #new
        self.entityset['reference']['cost_groups']['timestamp'] = False
        self.entityset['reference']['cost_items']['timestamp'] = False
        self.entityset['reference']['countries']['timestamp'] = False
        self.entityset['reference']['couriers']['timestamp'] = False
        self.entityset['reference']['legal_entities']['timestamp'] = False
        self.entityset['reference']['mg_channels']['timestamp'] = False
        self.entityset['reference']['payment_statuses']['timestamp'] = False
        self.entityset['reference']['units']['timestamp'] = False

        self.entityset['users']['timestamp'] = False
        self.entityset['user_groups']['timestamp'] = False
        self.entityset['costs']['timestamp'] = False
        self.entityset['customers']['timestamp'] = True
        self.entityset['customers_corporate']['timestamp'] = True
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
        #new
        self.entityset['reference']['cost_groups']['entity_id'] = 'costGroups'
        self.entityset['reference']['cost_items']['entity_id'] = 'costItems'
        self.entityset['reference']['countries']['entity_id'] = 'countriesIso'
        self.entityset['reference']['couriers']['entity_id'] = 'couriers'
        self.entityset['reference']['legal_entities']['entity_id'] = 'legalEntities'
        self.entityset['reference']['mg_channels']['entity_id'] = 'mgChannels'
        self.entityset['reference']['payment_statuses']['entity_id'] = 'paymentStatuses'
        self.entityset['reference']['units']['entity_id'] = 'units'

        self.entityset['users']['entity_id'] = 'users'
        self.entityset['user_groups']['entity_id'] = 'userGroups'
        self.entityset['costs']['entity_id'] = 'costs'
        self.entityset['customers']['entity_id'] = 'customers'
        self.entityset['customers_corporate']['entity_id'] = 'customersCorporate'
        self.entityset['orders']['entity_id'] = 'orders'

    def set_formats(self):
        self.entityset['reference']['sites']['format'] = self.formats.no_format
        self.entityset['reference']['stores']['format'] = self.formats.no_format
        self.entityset['reference']['statuses']['format'] = self.formats.no_format
        self.entityset['reference']['status_groups']['format'] = self.formats.no_format
        self.entityset['reference']['payment_types']['format'] = self.formats.no_format
        self.entityset['reference']['order_types']['format'] = self.formats.no_format
        self.entityset['reference']['order_methods']['format'] = self.formats.no_format
        self.entityset['reference']['delivery_types']['format'] = self.formats.no_format
        self.entityset['reference']['delivery_services']['format'] = self.formats.no_format
        #new
        self.entityset['reference']['cost_groups']['format'] = self.formats.no_format
        self.entityset['reference']['cost_items']['format'] = self.formats.no_format
        self.entityset['reference']['countries']['format'] = self.formats.no_format
        self.entityset['reference']['couriers']['format'] = self.formats.no_format
        self.entityset['reference']['legal_entities']['format'] = self.formats.no_format
        self.entityset['reference']['mg_channels']['format'] = self.formats.no_format
        self.entityset['reference']['payment_statuses']['format'] = self.formats.no_format
        self.entityset['reference']['units']['format'] = self.formats.no_format

        self.entityset['users']['format'] = self.formats.no_format
        self.entityset['user_groups']['format'] = self.formats.no_format
        self.entityset['costs']['format'] = self.formats.no_format
        self.entityset['customers']['format'] = self.formats.no_format
        self.entityset['customers_corporate']['format'] = self.formats.no_format
        self.entityset['orders']['format'] = self.formats.no_format

    def set_entity(self):
        '''Single entity name in history results'''
        self.entityset['reference']['sites']['entity'] = 'sites'
        self.entityset['reference']['stores']['entity'] = 'stores'
        self.entityset['reference']['statuses']['entity'] = 'statuses'
        self.entityset['reference']['status_groups']['entity'] = 'statusGroups'
        self.entityset['reference']['payment_types']['entity'] = 'paymentTypes'
        self.entityset['reference']['order_types']['entity'] = 'orderTypes'
        self.entityset['reference']['order_methods']['entity'] = 'orderMethods'
        self.entityset['reference']['delivery_types']['entity'] = 'deliveryTypes'
        self.entityset['reference']['delivery_services']['entity'] = 'deliveryServices'
        #new
        self.entityset['reference']['cost_groups']['entity'] = 'costGroups'
        self.entityset['reference']['cost_items']['entity'] = 'costItems'
        self.entityset['reference']['countries']['entity'] = 'countriesIso'
        self.entityset['reference']['couriers']['entity'] = 'couriers'
        self.entityset['reference']['legal_entities']['entity'] = 'legalEntities'
        self.entityset['reference']['mg_channels']['entity'] = 'mgChannels'
        self.entityset['reference']['payment_statuses']['entity'] = 'paymentStatuses'
        self.entityset['reference']['units']['entity'] = 'units'

        self.entityset['users']['entity'] = 'user'
        self.entityset['user_groups']['entity'] = 'user'
        self.entityset['costs']['entity'] = 'cost'
        self.entityset['customers']['entity'] = 'customer'
        self.entityset['customers_corporate']['entity'] = 'customer'
        self.entityset['orders']['entity'] = 'order'