from config import crm, crm_references as references
from templates import filter_templates
import engine

class Reference(object):
    ''''''
    def __init__(self, entities = references,
        source=crm['source'], version=crm['version'], api_key=crm['api_key'],
        output=crm['output'], encoding=crm['encoding'], path =crm['path']):       

        self.debug = engine.Debug(output)
        self.encoding = encoding
        self.entities = entities
        self.source = source
        self.version = version
        self.api_key = api_key
        self.path = f'{path}/crm/references/'

        self.debug.trace(f'References initialization completed.')      

    def store_period(self):
        ''''''
        for item in self.entities:
            url = engine.create_crm_url(self.source, self.version, f'reference/{item[1]}', self.api_key)
            json = engine.get_json(url)
            engine.save_json(self.path, item[1].replace('-','_'), json[f'{item[0]}'], self.encoding)  

            self.debug.trace(f'Entity {item[1]} is saved.')

        self.debug.trace(f'Jason saving completed.', True)

class Entity(object):

    def __init__(self, source=crm['source'], version=crm['version'], api_key=crm['api_key'],
        output=crm['output'], encoding=crm['encoding'], path =crm['path']):

        self.debug = engine.Debug(output)
        self.encoding = encoding
        self.source = source
        self.version = version
        self.api_key = api_key
        self.entity = None
        self.entities = None
        self.path = f'{path}/crm/'
        self.timestamp = True
        self.limit = 100
        self._entity_setup()

    # init extension
    def _entity_setup(self):
        self.debug.trace(f'Undentified Entity.')

    def _get_history(self, date_start, date_finish):

        history = list()
        filters = filter_templates['period'] % (date_start.date(), date_finish.date())        
        url_history = engine.create_crm_url(self.source, self.version, f'{self.entities}/history', self.api_key, filters)
        pages = self._count_pages(url_history)
        self.debug.trace(f'History pages counted: {pages}.')
        
        for page in range(1, pages+1):
            filters = filter_templates['page_period'] % (page, date_start.date(), date_finish.date())
            url_history_page = engine.create_crm_url(self.source, self.version, f'{self.entities}/history', self.api_key, filters)
            json_response = engine.get_json(url_history_page) 
            json_data = json_response['history']

            page_result = list()
            for item in range(0, len(json_data)):                
                result = dict()                
                result['id'] = json_data[item][self.entity]['id']      
                page_result.append(result)
          
            page_result = engine.remove_duclicates(page_result)
            history += page_result

        return engine.remove_duclicates(history)

    def _get_entities(self, ids, limit=100):

        entities = dict()
        filters = ''

        while len(ids) > limit:
            filters = f'limit={limit}&'
            ids_part = ids[0:limit]
            ids = ids[limit:]
            for item in range(0, len(ids_part)):
                filters += filter_templates['ids'] % ids_part[item]['id']
            entities.update(self._get_response(filters=filters))
        else:
            filters = ''
            ids_part = ids[0:len(ids)]
            for item in range(0, len(ids_part)):
                filters += filter_templates['ids'] % ids_part[item]['id']
            entities.update(self._get_response(filters=filters))

        return entities

    def store_period(self, date_start = None, date_finish = None):
        ''''''
        date_start, date_finish = engine.prepeare_period(date_start, date_finish)

        history = self._get_history(date_start, date_finish)
        self.debug.trace(f'History prepeared. Total count: {len(history)}.')

        entities = self._get_entities(history) 
        self.debug.trace(f'Entities prepeared. Total count: {len(entities)}.')

        self._save_json(entities)

    def store_pages(self, first = None, last = None, limit = 100):

        pages = self._count_pages(limit = limit)
        self.debug.trace(f'Total pages count: {pages}.')

        entities = dict()
        start, finish = engine.prepeare_index_period(first, last, pages)
        for page in range(start, finish):
            entity = self._get_response(page, limit)
            entities.update(entity)

        self._save_json(entities)
    
    def store_id(self, id):
        entities = self._get_entities([{"id":f'{id}'}], limit=100)
        self._save_json(entities)

    def _get_response(self, page=1, limit=100, filters=''):
        ''''''
        result = dict()
        filters += filter_templates['page_limit'] % (page, limit)
        url_page = engine.create_crm_url(self.source, self.version, self.entities, self.api_key, filters)
        
        response = engine.get_json(url_page)
        data = response[self.entities]
        
        for item in range(0, len(data)):                
            result[data[item]['id']] = data[item]
                
        return result

    def _count_pages(self, url=None, limit=100):
        
        filters = ''

        filters += filter_templates['limit'] % (limit)
        if url is None: 
            url = self._create_url(self.entities, filters)

        response = engine.get_json(url)
        return response['pagination']['totalPageCount']

    def _save_json(self, entities, json_name = None):
        ''''''
        if json_name is None:
            json_name = self.entities.replace('-','_')

        if len(entities) > 0:
            engine.save_json(self.path, json_name, entities, self.encoding, self.timestamp)
            self.debug.trace(f'Json saving completed.', True)
        else:
            self.debug.trace(f'No Entities to save.', True)

    def _create_url(self, entities=None, filters=''):
        ''''''
        if entities is None:
            entities = self.entities
        return engine.create_crm_url(self.source, self.version, entities, self.api_key, filters)

class Orders(Entity):

    def _entity_setup(self):
        self.path += 'orders/'
        self.entity = 'order'
        self.entities = 'orders'
        self.debug.trace(f'Orders initialization completed.')

class Customers(Entity):

    def _entity_setup(self):
        self.path += 'customers/'
        self.entity = 'customer'
        self.entities = 'customers'
        self.debug.trace(f'Customers initialization completed.')

class CustomersCorporate(Entity):

    def _entity_setup(self):
        self.path += 'customers_corporate/'
        self.entity = 'customer'
        self.json_entity = 'customersCorporate'
        self.entities = 'customers-corporate'
        
        self.debug.trace(f'Customers Corporate initialization completed.')

    def _get_response(self, page=1, limit=100, filters=''):
        ''''''
        result = dict()
        filters += filter_templates['page_limit'] % (page, limit)
        url_page = engine.create_crm_url(self.source, self.version, self.entities, self.api_key, filters)
        
        response = engine.get_json(url_page)
        data = response[self.json_entity]
        
        for item in range(0, len(data)):                
            result[data[item]['id']] = data[item]
                
        return result

class Users(Entity):

    def _entity_setup(self):
        self.path += 'users/'
        self.entity = 'user'
        self.entities = 'users'
        self.timestamp = False
        self.debug.trace(f'Users initialization completed.')

    def store_period(self):
        ''''''       
        entities = self._get_entities()         
        self.debug.trace(f'Entities prepeared. Total count: {len(entities)}.')

        if len(entities) > 0:
            engine.save_json(self.path, self.entities.replace('-','_'), entities, self.encoding, self.timestamp)
            self.debug.trace(f'Jason saving completed.', True)
        else:
            self.debug.trace(f'No Entities to save.', True)

    def _get_entities(self):

        entities = list()
        limit = 100

        filters = filter_templates['page_limit'] % (1, limit)  
        url_pages = engine.create_crm_url(self.source, self.version, f'{self.entities}', self.api_key, filters)
        pages = self._count_pages(url_pages)

        self.debug.trace(f'User pages counted: {pages}.')

        for page in range(1, pages+1):
            filters = filter_templates['page_limit'] % (page, limit)
            url_page = engine.create_crm_url(self.source, self.version, self.entities, self.api_key, filters)
            json_response = engine.get_json(url_page) 
            if self.entities in json_response:
                entities += json_response[self.entities]

        return entities

class UsersGroups(Entity):

    def _entity_setup(self):
        self.path += 'users/'
        self.entity = 'groups'
        self.entities = 'user-groups'
        self.timestamp = False
        self.debug.trace(f'User Groups initialization completed.')

    def store_period(self):
        ''''''       
        entities = self._get_entities()         
        self.debug.trace(f'Entities prepeared. Total count: {len(entities)}.')

        if len(entities) > 0:
            engine.save_json(self.path, self.entities.replace('-','_'), entities, self.encoding, self.timestamp)
            self.debug.trace(f'Jason saving completed.', True)
        else:
            self.debug.trace(f'No Entities to save.', True)

    def _get_entities(self):

        entities = list()
        limit = 100

        filters = filter_templates['page_limit'] % (1, limit)  
        url_pages = engine.create_crm_url(self.source, self.version, f'{self.entities}', self.api_key, filters)
        pages = self._count_pages(url_pages)

        self.debug.trace(f'User pages counted: {pages}.')

        for page in range(1, pages+1):
            filters = filter_templates['page_limit'] % (page, limit)
            url_page = engine.create_crm_url(self.source, self.version, self.entities, self.api_key, filters)
            json_response = engine.get_json(url_page) 
            if self.entity in json_response:
                entities += json_response[self.entity]

        return entities