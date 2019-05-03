import lib.verify_managed
from ipaddress import IPv4Network
from socket import gethostbyaddr
import socket

class GetUnmanagedClients(object):

    def __init__(self, ip_range):
        self.ip_range = ip_range
        self.v = lib.verify_managed
        self.unmanaged_list = []

    def get_clients(self):

        for x in IPv4Network(self.ip_range).hosts():
            ttl = self.v.get_ttl(str(x))
            if (ttl > 115) and (ttl < 130):
                if not self.v.verify_managed(x):
                    try:
                        self.unmanaged_list.append({'hostName':gethostbyaddr(str(x))[0],'ipAddress':str(x)})
                    except socket.herror:
                        self.unmanaged_list.append({'hostName': 'Reverso nao configurado', 'ipAddress': str(x)})
        return self.unmanaged_list
