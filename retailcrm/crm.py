class Reference(object):
    ''''''
    def __init__(self, entity, engine):       

        self.engine = engine
        self.path = entity['path'] 
        self.name = entity['name']
        self.url = entity['url']
        self.entity_id = entity['entity_id']
        # self.format = entity['format']
        self.timestamp = entity['timestamp']

        self.engine.trace(f'Reference {self.name} initialization completed.')      

    def store_period(self):
        ''''''
        response = self.engine.get_response(self.url)     
        data = response[self.entity_id]  
        self.engine.save_json(self.path, self.name, data, self.timestamp)