import subprocess
import re

def get_ttl(ip):
    p = subprocess.Popen(['ping', ip, '-c 3 -v'], stdout=subprocess.PIPE)
    result = p.communicate()[0]
    if p.returncode > 0:
        print('Erro durante o ping!')
    else:
        pattern = re.compile('ttl=\d\d\d')
        ttl = pattern.search(str(result)).group().strip('ttl=')
        return ttl

def get_mac(ip):
    p = subprocess.Popen(['arp', ip], stdout=subprocess.PIPE)
    result = p.communicate()[0]
    if p.returncode > 0:
        print('Erro na obtenção do MAC!')
    else:
        pattern = re.compile('\S\S:\S\S:\S\S:\S\S:\S\S:\S\S')
        mac = pattern.search(str(result)).group().replace(':','-').upper()
        return mac

print(get_mac('10.2.1.115'))
