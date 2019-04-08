from requests import get
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
        list_groups = {}
        response = get(server + '/sepm/api/v1/groups', headers=self.headers, verify=False)
        group_list = loads(response.text)['content']
        for x in group_list:
            list_groups[x['name']] = x['id']
        f = open('list_group.json','w+')
        f.write(dumps(list_groups))
        f.close()
        return group_list

    def get_computers_from_group(self, group_id):
        response = get(server + '/sepm/api/v1/groups/{}/computers'.format(group_id), headers=self.headers, verify=False)
        computer_list = loads(response.text)['content']
        f = open('computers_from_group.json','w+')
        f.write(dumps(computer_list))
        f.close()
        return computer_list

    def get_computers(self, pageIndex=1):
        response = get(server + '/sepm/api/v1/computers/?pageSize=100&pageIndex={}'.format(pageIndex), headers=self.headers, verify=False)
        return loads(response.text)

    def get_all_computers(self):
        hosts = {}
        response = self.get_computers()
        for i in range(1,response['totalPages']+1):
            response = self.get_computers(i)
            for x in response['content']:
                hosts[x['computerName']] = {'macAddress': x['macAddresses'][0], 'hardwareKey': x['hardwareKey'],
                                            'ipAddress': []}
                for k in x['ipAddresses']:
                    if ip_address(k).version == 4:
                        hosts[x['computerName']]['ipAddress'].append(k)
            sleep(3)
        f = open('list_computers.json','w+')
        f.write(str(dumps(hosts)))
        f.close()

    def get_servers(self):
        response = get(server + '/sepm/api/v1/admin/servers', headers=self.headers, verify=False)
        return response.text

    def get_version(self):
        response = get(server + '/sepm/api/v1/version', headers=self.headers, verify=False)
        return response.text

    def get_computer_info(self, computer_name):
        response = get(server + '/sepm/api/v1/computers/?computerName={}'.format(computer_name), headers=self.headers, verify=False)
        return response.text
