import json

from xf_apitest.api import BaseApi


class ApiHttpbinGet(BaseApi):

    url = "https://httpbin.org/get"
    params = None
    method = "GET"
    headers = {"accept":"application/json"}
    json = {}
    data = ""



class ApiHttpbinPost(BaseApi):

    url = "https://httpbin.org/post"
    params = {}
    method = "POST"
    headers = {"accept":"application/json"}
    json = {"abc":123}


