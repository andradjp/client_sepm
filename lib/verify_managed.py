import subprocess
import re
from json import loads
from time import sleep

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
        except ValueError:
            return 0
        except AttributeError:
            return 0


def verify_managed(ip):
    try:
        f = loads(open('list_computers.json', 'r').read())
        for x in f:
            for y in f[x]['ipAddress']:
                if str(ip) == y:
                    return True
        return False

    except Exception as e:
        print(e)
