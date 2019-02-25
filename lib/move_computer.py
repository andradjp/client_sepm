from requests import patch
from lib.auth import Authentication
from lib.config import server

class MoveComputer(object):

    def __init__(self, username, password):
        self.token = Authentication(username, password).logon()
        self.headers = {'Authorization': 'Bearer {}'.format(self.token)}

    def move_computer(self):
        payload = [{"group":{"id":"8E73CC080A01017D3F280D0250EB47B9"}, "hardwareKey":""}]
        response = patch(server + '/sepm/api/v1/computers', headers=self.headers, verify=False)