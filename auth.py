from requests import post
from json import dumps, loads
from urllib3 import disable_warnings, exceptions

disable_warnings(exceptions.InsecureRequestWarning)


class Authentication(object):

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.headers = {'Content-Type': 'application/json'}

    def logon(self):
        try:
            data = dumps({'username': self.username, 'password': self.password, 'domain': ''})
            response = post('https://sav340206.brb.com.br:8446/sepm/api/v1/identity/authenticate',
                            headers=self.headers, data=data, verify=False)
            return loads(response.text)['token']
        except Exception as e:
            print(e)

    def logout(self):
        try:
            post('https://sav340206.brb.com.br:8446/sepm/api/v1/identity/logout', headers=self.headers, verify=False)
        except Exception as e:
            print(e)