import json

from tests.api.httpbin import ApiHttpbinGet, ApiHttpbinPost
from xf_apitest.api import BaseApi



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
        .validate("json.url", "https://httpbin.org/post")\
        .validate("json().json.abc",666)

def test_httpbin_post_data():
    ApiHttpbinPost() \
        .set_data("abc=666") \
        .run() \
        .validate("status_code", 200) \
        .validate("headers.server", "gunicorn/19.9.0") \
        .validate("json.headers.Accept", "application/json") \
        .validate("json.url", "https://httpbin.org/post")

def test_httpbin_parameters_share():
    user_id = "adk129"
    ApiHttpbinGet() \
        .set_params(user_id=user_id) \
        .run() \
        .validate("status_code", 200) \
        .validate("headers.server", "gunicorn/19.9.0") \
        .validate("json().url", "https://httpbin.org/get?user_id={}".format(user_id)) \
        .validate("json().headers.Accept", "application/json")
    ApiHttpbinPost() \
        .set_json({"user_id":user_id}) \
        .run() \
        .validate("status_code", 200) \
        .validate("headers.server", "gunicorn/19.9.0") \
        .validate("json.headers.Accept", "application/json") \
        .validate("json.url", "https://httpbin.org/post") \
        .validate("json().json.user_id", "adk129")
