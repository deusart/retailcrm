import requests
import json
import datetime
import time
import urllib3
import os
from templates import filter_templates

urllib3.disable_warnings() 

class Debug(object):
    def __init__(self, output = print):
        self.debug_start_time = self.debug_time = time.time()        
        self.output = output

    def trace(self, message = None, total_time = False):
        if message is not None:
            self.output(f'[Debug] {message}')
        if not total_time:
            self.output("---- Step time %.2f seconds ----" % (time.time() - self.debug_time))
            self.debug_time = time.time()
        if total_time:
            self.output("--- Total time %.2f seconds ---" % (time.time() - self.debug_start_time))

class CatalogEngine(object):
    def __init__(self):
        self.get_json = get_json
    
    def set_headers(self, source, header, authorization):
        url = create_catalog_url(source, 'authorization')
        token = get_token(url, header, authorization) 
        return {'Authorization': f'Bearer {token}'}
    
    def set_catalogs(self, url, headers):
        catalogs = {}
        for item in get_json(url, headers):
            catalogs[item['name']] = item ['id']
        return catalogs 

    def set_base_url(self, source, url_type='catalogs'):
        return create_catalog_url(source, url_type)

    def generate_url(self, 
        url_base, catalog_id='', 
        entity='', id='', sub_entity='', 
        filters=''):     
        
        if id != '':
            id = f'/{id}'
        if sub_entity != '':
            sub_entity = f'/{sub_entity}'
        if filters != '':
            filters = f'?{filters}'

        return f'{url_base}/{catalog_id}/{entity}{id}{sub_entity}{filters}'
    
    def generate_path(self, 
        path_base, catalog_id='', 
        entity='', id=''):     
        
        if id != '':
            id = f'\{id}'        
        if entity != '':
            entity = f'\{entity}'
        
        return f'{path_base}\{catalog_id}{entity}{id}\\'

    def generate_filers(self, offset='', start_id='', limit=10000):
        if offset != '':
            return filter_templates['limit_offset'] % (limit, offset)
        if start_id != '':
            return filter_templates['limit_start_id'] % (limit, start_id)
        
        return filter_templates['limit'] % (limit)   
    
    def save_json(self, path, entities, name, encoding, timestamp=False):
        
        directory_exists(path)

        if len(entities) > 0:
            save_json(path, name, entities, encoding, timestamp)
            return save_json(path, name, entities, encoding, timestamp)                      
        else:
            return 'No Entities to save.'

    def prepare_json(self, json_list, catalog_id):
        data = {}
        for item in json_list:
            item['catalogId'] = catalog_id
            data[item['id']] = item
        return data


        # result = []
        # for catalog in self.catalogs:
        #     url =  self._get_entity_url(self.catalogs[catalog],'suppliers')
        #     response = engine.get_json(url, self.bearer_headers)
            
        #     for item in response:
        #         result.append((self.catalogs[catalog], item['id']))
       
        # return result
        pass



def get_json(url, headers=None):
    restponse = requests.get(url, headers=headers)
    json = restponse.json()    
    return json
    
def get_token(url, headers, input): 
    response = requests.post(url, headers=headers, data=json.dumps(input), verify=False)
    return response.json()['token']

def create_crm_url(source, version, enties, api_key, filters=''):
    return f'https://{source}/api/{version}/{enties}?{filters}apiKey={api_key}'

def create_catalog_url(source, enties):
    return f'https://{source}/api/{enties}'

def directory_exists(path, create=True):    
    if not os.path.exists(path):
        try:
            os.mkdir(path)
        except OSError:
            print ("Creation of the directory %s failed" % path)
        else:
            print ("Successfully created the directory %s " % path)

def save_json(path, entity, json_data, encoding, timestamp = False):
    if timestamp:
        entity = f'{entity}_{int(datetime.datetime.now().timestamp())}'
    try:
        with open(f'{path}{entity}.json', 'w', encoding=encoding) as outfile:
            outfile.write(json.dumps(json_data, ensure_ascii=False))
        return f'File {entity}.json is saved by path {path}.'  
    except Exception as e:
        print(f'[Error] {e}')           

def to_date(date, add_days = 0):  
    return datetime.datetime.strptime(date, '%Y-%m-%d') + datetime.timedelta(days=add_days)

def prepeare_period(date_start, date_finish):    
    if date_finish is None: 
        date_finish = to_date(date_start, 1)
    else: 
        date_finish = to_date(date_finish)
    date_start = to_date(date_start)

    return date_start, date_finish

def prepeare_index_period(first, last, total):
    
    if first is not None and last is not None:
        return first, last + 1
    if first is not None:
        if first > total + 1:
            return 1, first + 1
        else:
            return 1, total + 1
    elif last is not None:
        if last > total:
            return 1, total + 1
        else:
            return total - last, total + 1
    else:
        return 1, total + 1

def remove_duclicates(list_data):    
    return [dict(tuple_item) for tuple_item in {tuple(dict_item.items()) for dict_item in list_data}]