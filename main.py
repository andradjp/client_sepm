from lib.get_data import GetData
from lib.config import username, password

if __name__ == '__main__':
    i = GetData(username,password)
    i.get_all_computers()