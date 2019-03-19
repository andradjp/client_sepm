import lib.get_hosts
from ipaddress import IPv4Network


class GetUnmanagedClients(object):

    def __init__(self, ip_range):
        self.ip_range = ip_range
        g = lib.get_hosts()

    def get_clients(self):
        for x in IPv4Network(self.ip_range):
            g.get

g = GetUnmanagedClients('10.2.1.0/24')
g.get_clients()