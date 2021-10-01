import requests
import json

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class APICall:

    def __init__(self, api, token):
        self.apibase = api
        self.apikey = token
        self.headers = {
            "X-Auth": self.apikey,
            "content-type": "application/json",
        }

    def __send_request(self, method='get', endpoint='', data=None):
        request_call = getattr(requests, method)
        url = str("{}{}".format(self.apibase, endpoint if endpoint else "/"))

        response = request_call(
            url,
            headers = self.headers,
            data = json.dumps(data),
            verify = False
        )
        return json.loads(response.text)

    def get_raw(self, endpoint=""):
        url = str("{}{}".format(self.apibase, endpoint if endpoint else "/"))
        try:
            response = requests.get(url, headers=self.headers, verify=False)
            return response
        except:
            return None

    def post_raw(self, endpoint, data=None):
        if data is None:
            data = {}
        url = str("{}{}".format(self.apibase, endpoint if endpoint else "/"))
        try:
            response = requests.post(url, headers=self.headers, json=data, allow_redirects=False, verify=False)
            return response
        except:
            return None

    def delete_raw(self, endpoint, data=None):
        if data is None:
            data = {}
        url = str("{}{}".format(self.apibase, endpoint if endpoint else "/"))
        try:
            response = requests.delete(url, headers=self.headers, json=data, allow_redirects=False, verify=False)
            return response
        except:
            return None

    def get(self, endpoint=""):
        return self.__send_request("get", endpoint)

    def post(self, endpoint, data=None):
        if data is None:
            data = {}
        request = self.__send_request("post", endpoint, data)
        return request

    def delete(self, endpoint, data=None):
        if data is None:
            data = {}
        return self.__send_request("delete", endpoint, data)
