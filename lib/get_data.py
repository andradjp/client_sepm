from requests import get
from lib.auth import Authentication
from json import loads
import pprint

class GetData(object):

    def __init__(self):
        self.token = Authentication('admin', 'Sep@2018').logon()
        self.headers = {'Authorization': 'Bearer {}'.format(self.token)}

    def get_groups(self):
        response = get('https://sav340206.brb.com.br:8446/sepm/api/v1/groups', headers=self.headers, verify=False)
        group_list = loads(response.text)['content']
        for x in group_list:
            print(x)

    def get_computers(self):
        # response = get('https://sav340206.brb.com.br:8446/sepm/api/v1/computers', headers=self.headers, verify=False)
        response = get('https://sav340206.brb.com.br:8446/sepm/api/v1/groups/881FEE010A01017D52F44B90455799FE/computers', headers=self.headers, verify=False)
        computer_list = loads(response.text)['content']
        for x in computer_list:
            print(x)
        # pprint.pprint(computer_list)



g = GetData().get_computers()
