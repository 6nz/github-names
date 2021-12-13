#VPS, Replit version

import os
import random
import string
from colorama import Fore
import time
import requests
os.system("pip install pygithub")
from github import Github

g = Github("") #github token

repo = g.get_repo("") #github repo

os.system('clear')


namelist = requests.get('https://raw.githubusercontent.com/6nz/3-char-github-names/main/names.txt') #current list

def check(): #main checker
    for i in range(int(1)):
        try:
            code = ''.join(random.choices(string.ascii_letters + string.digits, k = (int(3))))
            r = requests.get(f'https://github.com/{code}')
            if r.status_code == 404:
                if r in namelist:
                    print(f"{Fore.RED}Code: {code} already exist!{Fore.RESET}") #filter
                    pass
                else:    
                    print(f'{Fore.GREEN}Not Taken: {code}{Fore.RESET}')
                    with open('names.txt', 'a', encoding = 'UTF-8') as f:
                        f.write(f'https://github.com/{code}\n')
                    contents = repo.get_contents("names.txt")
                    with open('names.txt', 'r') as file:
                        datas = file.read()
                        print(datas)
                    repo.update_file("names.txt", "Updated", f"{datas}", contents.sha)
                    print(f"{Fore.YELLOW}Updated!")
            else:
                print(f'{Fore.RED}Taken: {code}{Fore.RESET}')
        except:
            pass

while True: #loop
    check()
