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

    def scan_network():
        for x in scan_range:
            g = GetUnmanagedClients(x)
            message = ''
            for y in g.get_clients():
                print(y)
                message += ('Hostname: {} IP Address: {} \n'.format(y['hostName'], y['ipAddress']))
            if message != '':
                send_email(x, 'Unmanaged hosts {}'.format(x), message, 'Hosts Windows nao gerenciados pela solucao Symantec!')

    def pendent_reboot():
        hosts = i.get_all_computers_pendent_reboot()
        message = ''
        for x in hosts:
            message += ('Hostname: {} IP Address: {}\n'.format(x, hosts[x]['ipAddresses']))
        send_email('All', 'Pendent Reboot', message, 'Hosts Windows com reboot pendente!')

# scan_network()
pendent_reboot()
