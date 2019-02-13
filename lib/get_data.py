from requests import get, post
from lib.auth import Authentication
from lib.config import server
from json import loads, dumps
from ipaddress import ip_address
from time import sleep

class GetData(object):

    def __init__(self, username, password):
        self.token = Authentication(username, password).logon()
        self.headers = {'Authorization': 'Bearer {}'.format(self.token)}

    def get_groups(self):
        response = get(server + '/sepm/api/v1/groups', headers=self.headers, verify=False)
        group_list = loads(response.text)['content']
        return group_list

    def get_computers_from_group(self, group_id):
        # response = get(server + '/sepm/api/v1/computers', headers=self.headers, verify=False)
        response = get(server + '/sepm/api/v1/groups/{}/computers'.format(group_id), headers=self.headers, verify=False)
        computer_list = loads(response.text)['content']
        print(len(computer_list))

    def get_computers(self, pageIndex=1):
        response = get(server + '/sepm/api/v1/computers/?pageIndex={}'.format(pageIndex), headers=self.headers, verify=False)
        return loads(response.text)

    def get_all_computers(self):
        hosts = {}
        response = self.get_computers()
        for i in range(1,response['totalPages']):
            response = self.get_computers(i)
            print(response['number'])
            for x in response['content']:
                if len(x['ipAddresses']) == 1:
                    hosts[x['computerName']] = x['ipAddresses'][0]
                elif len(x['ipAddresses']) == 2:
                    for y in x['ipAddresses']:
                        if ip_address(y).version == 4:
                            hosts[x['computerName']] = y
            sleep(3)
        print(len(hosts))


    def get_version(self):
        response = get(server + '/sepm/api/v1/version', headers=self.headers, verify=False)
        print(response.text)
