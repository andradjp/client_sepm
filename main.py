from lib.get_data import GetData
from lib.move_computer import MoveComputer
from lib.config import username, password

if __name__ == '__main__':
    # i = GetData(username,password)
    # i.get_computer_info('et154019524')
    # i.get_groups()
    # i.get_all_computers()
    m = MoveComputer(username,password)
    m.move_computer()
    # i.get_computers_from_group('8E73CC080A01017D3F280D0250EB47B9')
