import subprocess
import re
from json import loads

def get_ttl(ip):
    p = subprocess.Popen(['ping', ip, '-c 1 -v'], stdout=subprocess.PIPE)
    result = p.communicate()[0]
    if p.returncode > 0:
        return 0
    else:
        try:
            pattern = re.compile('ttl=\d\d\d')
            ttl = int(pattern.search(str(result)).group().strip('ttl='))
            return ttl
        except ValueError as e:
            return 0
        except AttributeError as e:
            return 0

def get_mac(ip):
    p = subprocess.Popen(['arp', ip], stdout=subprocess.PIPE)
    result = p.communicate()[0]
    if p.returncode > 0:
        print('Erro na obtenção do MAC!')
    else:
        pattern = re.compile('\S\S:\S\S:\S\S:\S\S:\S\S:\S\S')
        mac = pattern.search(str(result)).group().replace(':','-').upper()
        return mac

def verify_managed(mac):

    f = loads(open('list_computers.json','r').read())
    for x in f:
        if mac == f[x]['macAddress']:
            return True
    return False
