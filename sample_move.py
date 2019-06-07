from requests import post, patch
from json import dumps, loads
from urllib3 import disable_warnings, exceptions

disable_warnings(exceptions.InsecureRequestWarning)

server = 'https://sav340206.brb.com.br:8446'
username = ''
password = ''

class moveClient(object):

    def __init__(self, server, username, password):
        self.server = server
        self.username = username
        self.password = password
        self.headers = {'Content-Type': 'application/json'}

    def logon(self):
        try:
            data = dumps({'username': self.username, 'password': self.password, 'domain': ''})
            response = post(server + '/sepm/api/v1/identity/authenticate',
                            headers=self.headers, data=data, verify=False)
            return loads(response.text)['token']
        except Exception as e:
            print(e)

    def logout(self):
        try:
            post(server + '/sepm/api/v1/identity/logout', headers=self.headers, verify=False)
        except Exception as e:
            print(e)

    def move_client(self):
        self.headers['Authorization'] = 'Bearer {}'.format(self.logon())
        payload = dumps([{'group':{'id':'2E46B9AB0A01017D7E2DE716D2E8D542'}, 'hardwareKey':'527078A4C78303792860D54AC7F0F5F6'}])
        response = patch(server + '/sepm/api/v1/computers', headers=self.headers, data=payload, verify=False)
        print(response.text)

c = moveClient(server, username, password)
c.move_client()
c.logout()