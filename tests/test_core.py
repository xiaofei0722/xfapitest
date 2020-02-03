import json

from tests.api.httpbin import *
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

def test_httpbin_extract():
    api_run = ApiHttpbinGet().run()
    status_code = api_run.extract("status_code")
    assert status_code == 200

    server = api_run.extract("headers.server")
    assert server == "gunicorn/19.9.0"

    accp = api_run.extract("json().headers.Accept")
    assert accp =="application/json"


def test_httpbin_setcookies():
    api_run = ApiHttpbinGetCookies()\
        .set_cookie("freefrom1","123")\
        .set_cookie("freefrom2","456")\
        .run()

    freefrom1 = api_run.extract("json.cookies.freefrom1")
    freefrom2 = api_run.extract("json.cookies.freefrom2")
    assert freefrom1 == "123"
    assert freefrom2 == "456"

def test_httpbin_parameters_extract():
    freefrom = ApiHttpbinGetCookies()\
        .set_cookie("freefrom","123")\
        .run()\
        .extract("json.cookies.freefrom")
    assert freefrom == "123"

    ApiHttpbinPost() \
        .set_json({"freefrom":freefrom}) \
        .run() \
        .validate("status_code", 200) \
        .validate("headers.server", "gunicorn/19.9.0") \
        .validate("json.headers.Accept", "application/json") \
        .validate("json.url", "https://httpbin.org/post")\
        .validate("json.json.freefrom",freefrom)


def test_httpbin_login_status(init_session):

    ApiHttpbinGetSetCookies().set_params(freefrom="678")\
        .run(init_session)

    resp = ApiHttpbinPost() \
        .set_json({"abc": 123}) \
        .run(init_session) \
        .get_response()

    request_headers = resp.request.headers
    assert "freefrom=678" in request_headers["Cookie"]