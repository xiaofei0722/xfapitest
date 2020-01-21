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
        actual_value = getattr(self.response,key)
        return self

    def run(self):
        self.response = requests.request(self.method,
                                         self.url,
                                         params=self.params,
                                         json=self.json,
                                         headers=self.headers,
                                         data=self.data)
        return self
    def set_data(self,data):
        self.data = data
        return self

    def set_json(self,json):
        self.json = json
        return self