from requests import patch
from lib.auth import Authentication
from lib.config import server
from json import dumps, loads

class MoveComputer(object):

    def __init__(self, username, password):
        self.token = Authentication(username, password).logon()
        self.headers = {'Authorization': 'Bearer {}'.format(self.token)}

    def move_computer(self):
        payload = dumps([{'group':{"id":"2E46B9AB0A01017D7E2DE716D2E8D542"}, "hardwareKey":"527078A4C78303792860D54AC7F0F5F6"}])
        response = patch(server + '/sepm/api/v1/computers', headers=self.headers, data=payload, verify=False)
        print(response.text)
