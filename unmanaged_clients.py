import lib.get_hosts
from ipaddress import IPv4Network
from socket import gethostbyaddr

class GetUnmanagedClients(object):



    def __init__(self, ip_range):
        self.ip_range = ip_range
        self.g = lib.get_hosts
        self.unmanaged_list = []
    def get_clients(self):

        for x in IPv4Network(self.ip_range).hosts():
            ttl = self.g.get_ttl(str(x))
            if (ttl > 120) and (ttl < 130):
                self.unmanaged_list.append({'hostName':gethostbyaddr(str(x))[0],'ipAddress':str(x),
                                            'MAC':self.g.get_mac(str(x))})
                print(self.unmanaged_list)
        return self.unmanaged_list

g = GetUnmanagedClients('10.2.1.0/24')
print(g.get_clients())