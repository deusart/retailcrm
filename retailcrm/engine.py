import urllib3
import requests
import json
import datetime
import os

urllib3.disable_warnings()

class CrmEngine(object):
    def __init__(self, settings, debug):
        self.api_key = settings.API_KEY
        self.encoding = settings.ENCODING
        self.path = settings.FOLDER
        self.trace = debug.trace
        self._set_utils()

    def save_json(self, path, entity, data, timestamp = False):

        if not os.path.exists(path):
            try:
                os.mkdir(path)
            except OSError:
                self.trace("Creation of the directory %s failed" % path)
            else:
                self.trace("Successfully created the directory %s " % path)

        if timestamp:
            entity = f'{entity}_{int(datetime.datetime.now().timestamp())}'

        try:
            with open(f'{path}{entity}.json', 'w', encoding=self.encoding) as outfile:
                outfile.write(json.dumps(data, ensure_ascii=False))
            self.trace(f'File {path}{entity}.json is saved. ({len(data)} Items)')
        except Exception as error:
            self.trace(error)

    def get_response(self, url, filters=None):
        if filters is None:
            filters = ''
        url = f'{url}?{filters}apiKey={self.api_key}'
        response = requests.get(url)    
        json = response.json()
        
        return json

    def _set_utils(self):
        self.filter_templates = dict (
            page = 'page=%s&',
            page_limit = 'page=%s&limit=%s&',
            period = 'filter[startDate]=%s%%2000:00:00&filter[endDate]=%s%%2000:00:00&',
            page_period = 'page=%s&filter[startDate]=%s%%2000:00:00&filter[endDate]=%s%%2000:00:00&',
            page_limint_period = 'page=%s&limit=%s&filter[startDate]=%s%2000:00:00&filter[endDate]=%s%2000:00:00&',
            id_site = 'site=%s&by=id&',
            id = 'by=id&',
            ids = 'filter[ids][]=%s&'
        )

    def to_date(self, date, add_days = 0):  
        return datetime.datetime.strptime(date, '%Y-%m-%d') + datetime.timedelta(days=add_days)

    def prepeare_period(self, date_start, date_finish):    
        if date_finish is None: 
            date_finish = self.to_date(date_start, 1)
        else: 
            date_finish = self.to_date(date_finish)
        date_start = self.to_date(date_start)

        return date_start, date_finish

    def prepeare_index_period(self, first, last, total):
                
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

    def remove_dublicates(self, data):
        return_date = []
        if isinstance(data, dict):
            return_date = [dict(tuple_item) for tuple_item in {tuple(dict_item.items()) for dict_item in data}]
        if isinstance(data, list):
            [return_date.append(x) for x in data if x not in return_date]
        return return_date

    def count_pages(self, url, filters=None):
        response = self.get_response(url, filters)
        return response['pagination']['totalPageCount']