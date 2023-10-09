import smtplib
import sys
from colorama import Fore
import os
from pystyle import Write, Colors
from rich.console import Console
import platform
import json
import ctypes
console = Console()
import time
import pyautogui
import requests
import threading
# import android
import random
import datetime

if os.path.exists('users.json'):
    pass
else:
    os.system("cls" or "clear")
    username = input(f"   └─({Fore.CYAN}Enter your username{Fore.WHITE}) → ")
    data = {
        'username': username
    }
    with open('users.json', 'x') as f:
        json.dump(data, f)

def color():
    global gr
    b = Fore.BLACK
    g = Fore.GREEN
    m = Fore.MAGENTA
    gr = Fore.LIGHTWHITE_EX

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def banner():
    global gr
    clear()
    Write.Print(Fore.MAGENTA + f"""



                

   ███╗░░██╗██╗░░░██╗░█████╗░██╗░░░░░███████╗░█████╗░░██████╗    ██████╗░░█████╗░███╗░░░███╗██████╗░███████╗██████╗░
   ████╗░██║██║░░░██║██╔══██╗██║░░░░░██╔════╝██╔══██╗██╔════╝    ██╔══██╗██╔══██╗████╗░████║██╔══██╗██╔════╝██╔══██╗
   ██╔██╗██║██║░░░██║██║░░╚═╝██║░░░░░█████╗░░███████║╚█████╗░    ██████╦╝██║░░██║██╔████╔██║██████╦╝█████╗░░██████╔╝
   ██║╚████║██║░░░██║██║░░██╗██║░░░░░██╔══╝░░██╔══██║░╚═══██╗    ██╔══██╗██║░░██║██║╚██╔╝██║██╔══██╗██╔══╝░░██╔══██╗
   ██║░╚███║╚██████╔╝╚█████╔╝███████╗███████╗██║░░██║██████╔╝    ██████╦╝╚█████╔╝██║░╚═╝░██║██████╦╝███████╗██║░░██║
   ╚═╝░░╚══╝░╚═════╝░░╚════╝░╚══════╝╚══════╝╚═╝░░╚═╝╚═════╝░    ╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝
   Made By Ahmed Malik
   https://github.com/Ahmeddaayy

    """, Colors.green_to_yellow, interval=0.000)
    print(f"""
   ({Fore.LIGHTWHITE_EX}0{Fore.WHITE}) Options →
   ({Fore.LIGHTWHITE_EX}1{Fore.WHITE}) Email Bomber
   ({Fore.LIGHTWHITE_EX}2{Fore.WHITE}) Phone Number Bomber (Coming Soon)
   ({Fore.LIGHTWHITE_EX}3{Fore.WHITE}) Discord Spammer
   ({Fore.LIGHTWHITE_EX}4{Fore.WHITE}) Whatsapp Spammer
    """) # {Fore.CYAN} 2 2
    choice = input(Fore.WHITE + f"   └─({Fore.CYAN}@{platform.node()}{Fore.WHITE}) → ")
    Fore.WHITE
    print('\n')
    if choice == "1":
        i = 0
        try:
            counter = int(input(f"  ({Fore.LIGHTWHITE_EX}>{Fore.WHITE}) Number of mails → "))
            email = input(f"  ({Fore.LIGHTWHITE_EX}>{Fore.WHITE}) Your gmail → ")
            password = input(f"  ({Fore.LIGHTWHITE_EX}>{Fore.WHITE}) Your gmail app password → ")
            message = input(f"  ({Fore.LIGHTWHITE_EX}>{Fore.WHITE}) Message → ")
            bomb_email = input(f"  ({Fore.LIGHTWHITE_EX}>{Fore.WHITE}) Target email (only gmail is supported) → ")
            for x in range(counter):
                mail = smtplib.SMTP('smtp.gmail.com',587)
                mail.ehlo()
                mail.starttls()
                mail.login(email,password)
                mail.sendmail(email,bomb_email,message)
                # console.log(f"lol")
                console.log(f"Sent count: {i} | {email}")
                i +=1
        # try:
        except Exception as er:
            # pr
            console.log(f"Unknown error occured: {er}")
        
    if choice == "4":
        # message = input(f"    {Fore.WHITE}[{Fore.MAGENTA}>{Fore.WHITE}] Message: ")
        message = input(f"  ({Fore.LIGHTWHITE_EX}>{Fore.WHITE}) Message → ")
        print("open the contact which you want to spam in whatsapp to spam! you have 20 seconds")
        time.sleep(20)
        for i in range(5000):
            pyautogui.write(message)
            pyautogui.press('enter')
        banner()

    if choice == "3":
        session = requests.Session()
        # type = int(input(f"    {Fore.WHITE}[{Fore.MAGENTA}>{Fore.WHITE}] Type 1: a little slow, Type2: Faster (1, 2): "))
        webhook = input(f"    {Fore.WHITE}[{Fore.MAGENTA}>{Fore.WHITE}] Webhook URL: ")
        content = input(f"    {Fore.WHITE}[{Fore.MAGENTA}>{Fore.WHITE}] content: ")
        username = input(f"    {Fore.WHITE}[{Fore.MAGENTA}>{Fore.WHITE}] username: ")
        spam = int(input(f"    {Fore.WHITE}[{Fore.MAGENTA}>{Fore.WHITE}] spam amount: "))

        def spammer():
            requests.post(webhook, data={'username': f'{username}', 'content': f'{content}'}) # WaveBomber
        
        for i in range(spam):
            threading.Thread(target=(spammer)).start()

        banner()
    
    if choice == "0":
        banner()

    if choice == "2":
    #     d=android.Android()
    #     #1(area code) number(7digits)
    #     bombed="918249106513" #crude example of a phone number
    #     #how many bombs
    #     bombnums=range(10)
    #     msg="bolo beta lmao"
    #     for i in bombnums:
    #         d.smsSend(bombed,msg)
        print("wait for v2 <:")

if __name__ == "__main__":
    with open('users.json') as f:
        data = json.load(f)
        name = data["username"]
    ctypes.windll.kernel32.SetConsoleTitleW(f"Nucleas Bomber | Logged in as {name}")
    # os.system(f"title  | Logged in as {name}")
    banner()
