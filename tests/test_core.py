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
    data = "abc=123"

def test_httpbin_get():

    ApiHttpbinGet().run()\
        .validate("status_code",200)\
        .validate("headers.server","gunicorn/19.9.0")\
        .validate("json().url","https://httpbin.org/get")\
        .validate("json().headers.Accept","application/json")\
        .validate("json().args",{})

def test_httpbin_get_with_params():

    ApiHttpbinGet()\
        .set_params(xxx=555,abc=666)\
        .run()\
        .validate("status_code",200) \
        .validate("headers.server", "gunicorn/19.9.0")\
        .validate("json().url","https://httpbin.org/get?xxx=555&abc=666") \
        .validate("json().headers.Accept", "application/json")

def test_httpbin_post_json():

    ApiHttpbinPost()\
        .set_json({"abc":666})\
        .run()\
        .validate("status_code",200) \
        .validate("headers.server", "gunicorn/19.9.0") \
        .validate("json.headers.Accept", "application/json") \
        .validate("json.url", "https://httpbin.org/post")

def test_httpbin_post_data():
    ApiHttpbinPost() \
        .set_data("abc=666") \
        .run() \
        .validate("status_code", 200) \
        .validate("headers.server", "gunicorn/19.9.0") \
        .validate("json.headers.Accept", "application/json") \
        .validate("json.url", "https://httpbin.org/post")