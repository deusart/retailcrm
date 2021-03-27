class Entity(object):

    def __init__(self, entity, engine):

        self.engine = engine
        self.path = entity['path'] 
        self.name = entity['name']
        self.url = entity['url']
        self.entity_id = entity['entity_id']
        self.entity = entity['entity']
        self.timestamp = entity['timestamp']
        self.format = entity['format']
        self.ids = list()
        self.entities = dict()
        self._entity_setup()

        self.engine.trace(f'Entity {self.name} initialization completed.')

    # init extension
    def _entity_setup(self):
        pass

    def prepare_history(self, date_start, date_finish):
        history = list()
        filters = self.engine.filter_templates['period'] % (date_start.date(), date_finish.date()) 
        url_history = f'{self.url}/history'
        pages = self.engine.count_pages(url_history, filters)
        self.engine.trace(f'History counted: {pages} pages.')
    
        for page in range(1, pages+1):
            filters = self.engine.filter_templates['page_period'] % (page, date_start.date(), date_finish.date())
            json_response = self.engine.get_response(url_history, filters) 
            json_data = json_response['history']
            page_result = list()
            for item in range(0, len(json_data)):                
                result = json_data[item][self.entity]['id']
                page_result.append(result)
          
            page_result = self.engine.remove_dublicates(page_result)
            history += page_result
        
        self.ids = self.engine.remove_dublicates(history)

    def prepare_entities(self, limit=100):      
        self.ids.sort()  
        ids = self.ids
        while len(ids) > limit:
            filters = f'limit={limit}&'
            ids_part = ids[0:limit]
            ids = ids[limit:]     
            self.add_entities(ids_part, filters)
        else:
            filters = f'limit={limit}&'
            ids_part = ids[0:len(ids)]           
            self.add_entities(ids_part, filters)

    def add_entities(self, ids, filters=''):
        for item in ids:
            filters += self.engine.filter_templates['ids'] % item    
        data = self.engine.get_response(self.url, filters)         
        for item in data[self.entity_id]:
            self.entities[item['id']] = self.format(item)   
        
    def save_json(self):
        ''''''
        if len(self.entities) > 0:
            self.engine.save_json(self.path, self.name, self.entities, self.timestamp)
        else:
            self.engine.trace(f'No Entities to save.')

    def store_period(self, date_start = None, date_finish = None):
        ''''''
        date_start, date_finish = self.engine.prepeare_period(date_start, date_finish)  

        self.prepare_history(date_start, date_finish)
        self.engine.trace(f'History prepeared. Total count: {len(self.ids)} entities.')        
        self.prepare_entities()
        self.engine.trace(f'Entities prepeared. Total count: {len(self.entities)} entities.')
        self.save_json()

        # entity_ids = self.entities.keys()
        # new_list = [item for item in self.ids if item not in entity_ids]
        # print(self.ids)
        # print(new_list)


    # def store_id(self, id):
    #     filters += self.engine.filter_templates['ids'] % item 
    #     data = self.engine.get_response(self.url, filters)

    #     self.entities[f'{id}'] = entity
    #     self._get_entities([{"id":f'{id}'}], limit=100)
    #     self._save_json(entities)

        # return engine.remove_duclicates(history)

    # def _get_history(self, date_start, date_finish):

    #     history = list()
    #     filters = self.engine.filter_templates['period'] % (date_start.date(), date_finish.date())        
    #     url_history = engine.create_crm_url(self.source, self.version, f'{self.entities}/history', self.api_key, filters)
    #     pages = self._count_pages(url_history)
    #     self.debug.trace(f'History pages counted: {pages}.')
        
    #     for page in range(1, pages+1):
    #         filters = filter_templates['page_period'] % (page, date_start.date(), date_finish.date())
    #         url_history_page = engine.create_crm_url(self.source, self.version, f'{self.entities}/history', self.api_key, filters)
    #         json_response = engine.get_json(url_history_page) 
    #         json_data = json_response['history']

    #         page_result = list()
    #         for item in range(0, len(json_data)):                
    #             result = dict()                
    #             result['id'] = json_data[item][self.entity]['id']      
    #             page_result.append(result)
          
    #         page_result = engine.remove_duclicates(page_result)
    #         history += page_result

    #     return engine.remove_duclicates(history)

    # def _get_entities(self, ids, limit=100):

    #     entities = dict()
    #     filters = ''

    #     while len(ids) > limit:
    #         filters = f'limit={limit}&'
    #         ids_part = ids[0:limit]
    #         ids = ids[limit:]
    #         for item in range(0, len(ids_part)):
    #             filters += filter_templates['ids'] % ids_part[item]['id']
    #         entities.update(self._get_response(filters=filters))
    #     else:
    #         filters = ''
    #         ids_part = ids[0:len(ids)]
    #         for item in range(0, len(ids_part)):
    #             filters += filter_templates['ids'] % ids_part[item]['id']
    #         entities.update(self._get_response(filters=filters))

    #     return entities

    # def store_period(self, date_start = None, date_finish = None):
    #     ''''''
    #     date_start, date_finish = engine.prepeare_period(date_start, date_finish)

    #     history = self._get_history(date_start, date_finish)
    #     self.debug.trace(f'History prepeared. Total count: {len(history)}.')

    #     entities = self._get_entities(history) 
    #     self.debug.trace(f'Entities prepeared. Total count: {len(entities)}.')

    #     self._save_json(entities)

    # def store_pages(self, first = None, last = None, limit = 100):

    #     pages = self._count_pages(limit = limit)
    #     self.debug.trace(f'Total pages count: {pages}.')

    #     entities = dict()
    #     start, finish = engine.prepeare_index_period(first, last, pages)
    #     for page in range(start, finish):
    #         entity = self._get_response(page, limit)
    #         entities.update(entity)

    #     self._save_json(entities)
    


    # def _get_response(self, page=1, limit=100, filters=''):
    #     ''''''
    #     result = dict()
    #     filters += filter_templates['page_limit'] % (page, limit)
    #     url_page = engine.create_crm_url(self.source, self.version, self.entities, self.api_key, filters)
        
    #     response = engine.get_json(url_page)
    #     data = response[self.entities]
        
    #     for item in range(0, len(data)):                
    #         result[data[item]['id']] = data[item]
                
    #     return result

    # def _count_pages(self, url=None, limit=100):
        
    #     filters = ''

    #     filters += filter_templates['limit'] % (limit)
    #     if url is None: 
    #         url = self._create_url(self.entities, filters)

    #     response = engine.get_json(url)
    #     return response['pagination']['totalPageCount']

  