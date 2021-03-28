from retailcrm.base import Entity
class Reference(object):
    ''''''
    def __init__(self, entity, engine):       

        self.engine = engine
        self.path = entity['path'] 
        self.name = entity['name']
        self.url = entity['url']
        self.entity_id = entity['entity_id']
        self.format = entity['format']
        self.timestamp = entity['timestamp']

        self.engine.trace(f'Reference {self.name} initialization completed.')      

    def store_period(self):
        ''''''
        entity = dict()
        
        response = self.engine.get_response(self.url)
        data = response[self.entity_id]

        if isinstance(data, list):
            for item in data:
                if isinstance(item, dict):
                    if 'code' in item.keys(): 
                        entity[item['code']] = self.format(item)
                    elif 'id' in item.keys(): 
                        entity[item['id']] = self.format(item)
                else:
                    entity[item] = self.format(item)
            data = entity
        
        self.engine.save_json(self.path, self.name, data, self.timestamp)

class Users(Entity):

    def prepare_entities(self, limit = 100):
        pages = self.engine.count_pages(self.url)
        self.engine.trace(f'User pages counted: {pages}.')
        for page in range(1, pages+1):
            filters = self.engine.filter_templates['page_limit'] % (page, limit)       
            data = self.engine.get_response(self.url, filters)
            for item in data[self.entity_id]:
                self.entities[item['id']] = self.format(item)
   
    def store(self):     
        self.prepare_entities()
        self.engine.trace(f'Entities prepeared. Total count: {len(self.entities)} entities.')
        self.save_json()