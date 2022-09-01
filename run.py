import os
try:
    import requests
except ImportError:
    print('\n')
    os.system('pip install requests')

try:
    import bs4
except ImportError:
    print('\n')
    os.system('pip install bs4')

try:
    import rich
except ImportError:
    print('\n')
    os.system('pip install rich')
#################################################################################
from src import ll

if __name__ == '__main__':
    os.system("git pull")
    ll.menu()
