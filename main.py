from lib.get_data import GetData
from lib.move_computer import MoveComputer
from lib.config import username, password, scan_range
from lib.unmanaged_clients import GetUnmanagedClients
from lib.send_mail import send_email

if __name__ == '__main__':
    i = GetData(username,password)
    # i.get_computer_info('et154019524')
    # i.get_groups()
    i.get_all_computers()
    # m = MoveComputer(username,password)
    # m.move_computer()
    # i.get_computers_from_group('8E73CC080A01017D3F280D0250EB47B9')

    for x in scan_range:
        g = GetUnmanagedClients(x)
        message = ''
        for y in g.get_clients():
             message += ('Hostname: {} IP Address: {} MAC Address: {} \n'.format(y['hostName'], y['ipAddress'], y['MAC']))
        if message != '':
            send_email(x, 'Unmanaged hosts {}'.format(x), message)
    # g = GetUnmanagedClients('10.2.1.8/29')
    # send_email('Unmanaged hots 10.2.1.8/29',g.get_clients())