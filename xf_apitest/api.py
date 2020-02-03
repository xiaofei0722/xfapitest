import json
import logging
import requests

class BaseApi(object):

    method = ""
    url = ""
    params = {}
    headers = {}
    cookies = {}
    data = {}
    json = {}

    def __init__(self):
        self.response = None

    def set_params(self, **params):
        self.params = params
        return self

    def validate(self,key,expected_value):
        print("响应数据===============",json.dumps(self.response.json(),indent=2))
        print("字段路径===============",key)
        print("预期结果===============",expected_value)
        actual_value = self.extract(key)
        print("实际结果===============",actual_value)
        assert actual_value == expected_value
        return self

    def run(self,session=None):
        session=session or requests.sessions.Session()
        self.response = session.request(
            self.method,
             self.url,
             params=self.params,
             json=self.json,
             cookies=self.cookies,
             headers=self.headers,
             data=self.data)
        return self

    def extract(self,field):
        value = self.response
        for _key in field.split("."):
            if isinstance(value, requests.Response):
                if _key in ["json()", "json"]:
                    value = self.response.json()
                else:
                    value = getattr(self.response, _key)
            elif isinstance(value, (requests.structures.CaseInsensitiveDict, dict)):
                value = value[_key]
        return value

    def set_data(self,data):
        self.data = data
        return self

    def set_json(self,json):
        self.json = json
        return self

    def set_cookie(self,key,value):
        self.cookies.update({key:value})
        return self

    def get_response(self):
        return self.response