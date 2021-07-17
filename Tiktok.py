import random
import requests
import sys as n
import time as mm
from colorama import *
import threading
req = requests.session()
def slow(M):
    for c in M + '\n':
        n.stdout.write(c)
        n.stdout.flush()
        mm.sleep(1. / 200)
slow('''"""\033[1;33m
 ░░╚══╗░╔═╔════╝  Tool: TikTok Username Checker
 ╚═╦═╗╠═╩═╩╗╔═╦═╗ Control: Telegram Bot
 ░░║▒╠╣▒▒▒▒╠╣▒║▒║ Author: aaBooD ~!
 ╔═╩═╝╠═╦═╦╝╚═╩═╝ Version: 1.0v
 ░░╔══╝░╚═╚════╗  Developer: @DDDPDDDD
==============================================
''')
print(" ")
le = int(input('[+] User Length : '))
print("==============================================")
print(" ")
chrs = 'abcdefg_hijklmnopqrstuvwxyz1234567890'
print(" ")
sleep = int(input('[+] Sleep : '))
print(" ")
print("==============================================")
print(" ")
Token = input('[+] Bot Token : ')
print(" ")
print("==============================================")
print(" ")
Id = input('[+] Id Telegram : ')
print(" ")
print('==============================================')
print(" ")
print(" ")
a = 0
b = 0

while True:
    pass
    lst = str("".join(random.choice(chrs)for x in range(le)))
    url = f'https://www.tiktok.com/@{lst}?'
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,/;q=0.8,"
                  "application/signed-exchange;v=b3;q=0.9",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/85.0.4183.83 Safari/537.36",
        "Connection": "close",
        "Host": "www.tiktok.com",
        "Accept-Encoding": "gzip, deflate",
        "Cache-Control": "max-age=0"
    }
    reqsnd = req.get(url, headers=headers)
    if reqsnd.status_code == 404:
        b += 1
        print(
            f"{Style.BRIGHT}{Fore.LIGHTBLACK_EX}[{Fore.LIGHTCYAN_EX}{b}{Fore.LIGHTBLACK_EX}]{Fore.LIGHTGREEN_EX} Hunt | {Style.BRIGHT}{Fore.LIGHTWHITE_EX} {lst} {Fore.LIGHTGREEN_EX}|")
        bot = f"https://api.telegram.org/bot{Token}/sendMessage?chat_id={Id}&text=* TikTok Username\nUser: {lst}\n₪ Abood | @DDDPDDDD *"
        req.get(bot)
        with open("T-User.txt", "a")as T3ZTT:
            T3ZTT.write(lst + "\n")
            time.sleep(sleep)
    else:
        a += 1
        print(f"{Style.BRIGHT}{Fore.LIGHTBLACK_EX}[{Fore.LIGHTCYAN_EX}{a}{Fore.LIGHTBLACK_EX}]{Fore.LIGHTRED_EX} Not Available | {Style.BRIGHT}{Fore.LIGHTWHITE_EX} {lst} {Fore.LIGHTRED_EX}|")
        time.sleep(sleep)
