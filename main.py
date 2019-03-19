from lib.get_data import GetData
from lib.move_computer import MoveComputer
from lib.config import username, password

if __name__ == '__main__':
    # i = GetData(username,password)
    # i.get_groups()
    # i.get_all_computers()
    m = MoveComputer(username,password)
    m.move_computer()
    # i.get_computers_from_group('0F120C410A01017D0C3B1382B5E942FC')