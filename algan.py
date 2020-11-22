#!/usr/bin/python3

import requests
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)   
import time
import os
import socket

def algan():    

    dosya = open('subdomains-100.txt','r')
    oku = dosya.read()
    alt_alan_adi_dosya = oku.splitlines()
    for alt_alan_adi in alt_alan_adi_dosya:
        url = f'http://{alt_alan_adi}.{alan_adi}'
        try:
            requests.get(url)
        except requests.ConnectionError:
            pass
        else:
            print(Fore.RED+" Alt Alan Adı: "+Fore.WHITE+"",url)

def banner():  
                    
    print(Fore.CYAN+"""

     ▄▄▄       ██▓      ▄████  ▄▄▄       ███▄    █ 
    ▒████▄    ▓██▒     ██▒ ▀█▒▒████▄     ██ ▀█   █ 
    ▒██  ▀█▄  ▒██░    ▒██░▄▄▄░▒██  ▀█▄  ▓██  ▀█ ██▒
    ░██▄▄▄▄██ ▒██░    ░▓█  ██▓░██▄▄▄▄██ ▓██▒  ▐▌██▒
     ▓█   ▓██▒░██████▒░▒▓███▀▒ ▓█   ▓██▒▒██░   ▓██░
     ▒▒   ▓▒█░░ ▒░▓  ░ ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ▒ ▒ 
      ▒   ▒▒ ░░ ░ ▒  ░  ░   ░   ▒   ▒▒ ░░ ░░   ░ ▒░
      ░   ▒     ░ ░   ░ ░   ░   ░   ▒      ░   ░ ░ 
          ░  ░    ░  ░      ░       ░  ░         ░ 
                                               
"""+Fore.BLUE+"""\t  Subdomain Tarama Aracı """ + Fore.RED + """@saricayemre\n""")

def tarama():
    
    time.sleep(1)
    print(Fore.RED+" Tarama Başlıyor ",end="")
    time.sleep(1)
    for i in range(3):
        print(Fore.RED+"•",end="")
        time.sleep(1)
    print("\n")

   

banner()
alan_adi = input(Fore.RED+" Site Adını Giriniz!>"+Fore.WHITE+" ")
os.system("clear")
banner()
tarama()
print(Fore.GREEN+"+"+"-"*30+"+")
print(Fore.BLUE+" Alan Adı: "+Fore.CYAN+alan_adi)
print(Fore.GREEN+"+"+"-"*30+"+")
algan()


