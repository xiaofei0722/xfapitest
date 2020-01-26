import json
import logging

import requests

class BaseApi(object):

    method = ""
    url = ""
    params = {}
    headers = {}
    data = {}
    json = {}

    def set_params(self, **params):
        self.params = params
        return self

    def validate(self,key,expected_value):
        value = self.response
        for _key in key.split("."):
            # print("key------",_key,"value------",value)
            if isinstance(value,requests.Response):
                if _key in ["json()","json"]:
                    value = self.response.json()
                else:
                    value = getattr(self.response, _key)
            elif isinstance(value,(requests.structures.CaseInsensitiveDict,dict)):
                value = value[_key]
        print(json.dumps(self.response.json(),indent=2))
        print(value)
        print(expected_value)
        assert value == expected_value
        return self

    def run(self):
        self.response = requests.request(self.method,
                                         self.url,
                                         params=self.params,
                                         json=self.json,
                                         headers=self.headers,
                                         data=self.data)
        return self

    def extract(self,field):
        value = getattr(self.response,field)
        return value
    def set_data(self,data):
        self.data = data
        return self

    def set_json(self,json):
        self.json = json
        return self