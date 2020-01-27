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

class ApiHttpbinGetCookies(BaseApi):

    url = "https://httpbin.org/cookies"
    params = {}
    method = "GET"
    headers = {"accept":"application/json"}

class ApiHttpbinGetSetCookies(BaseApi):

    url = "https://httpbin.org/cookies/set"
    params = {}
    method = "GET"
    headers = {"accept":"text/plain"}
