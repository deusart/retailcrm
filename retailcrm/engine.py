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
            url = f'{url}?apiKey={self.api_key}'
        response = requests.get(url)    
        json = response.json()
        
        return json