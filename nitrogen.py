import random, string
import os
import webbrowser
import time
import requests
import colorama
import ctypes
from colorama import Fore
from time import gmtime, sleep, strftime

def Home():
    os.system("cls")
    colorama.init()
    ctypes.windll.kernel32.SetConsoleTitleW(f"[Nitro Tool] By Reds#9999 and etxrnal#9999 | Loading...")
    time.sleep(3)
    ctypes.windll.kernel32.SetConsoleTitleW(f"[Nitro Tool] By Reds#9999 and etxrnal#9999 | Main Menu")
    print(f'''
{Fore.LIGHTCYAN_EX} ███▄    █  ██▓▄▄▄█████▓ ██▀███   ▒█████     ▄▄▄█████▓ ▒█████   ▒█████   ██▓    
{Fore.LIGHTCYAN_EX} ██ ▀█   █ ▓██▒▓  ██▒ ▓▒▓██ ▒ ██▒▒██▒  ██▒   ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    
{Fore.LIGHTCYAN_EX}▓██  ▀█ ██▒▒██▒▒ ▓██░ ▒░▓██ ░▄█ ▒▒██░  ██▒   ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    
{Fore.LIGHTCYAN_EX}▓██▒  ▐▌██▒░██░░ ▓██▓ ░ ▒██▀▀█▄  ▒██   ██░   ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░    
{Fore.LIGHTCYAN_EX}▒██░   ▓██░░██░  ▒██▒ ░ ░██▓ ▒██▒░ ████▓▒░     ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒
{Fore.LIGHTCYAN_EX}░ ▒░   ▒ ▒ ░▓    ▒ ░░   ░ ▒▓ ░▒▓░░ ▒░▒░▒░      ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░
{Fore.LIGHTCYAN_EX}░ ░░   ░ ▒░ ▒ ░    ░      ░▒ ░ ▒░  ░ ▒ ▒░        ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░
{Fore.LIGHTCYAN_EX}   ░   ░ ░  ▒ ░  ░        ░░   ░ ░ ░ ░ ▒       ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   
{Fore.LIGHTCYAN_EX}         ░  ░              ░         ░ ░                  ░ ░      ░ ░      ░  ░

{Fore.LIGHTCYAN_EX}              ╔══════════════════════════════════════════════════════════╗
{Fore.LIGHTCYAN_EX}              ║       Nitro Tool by Reds#9999 and etxrnal#9999           ║
{Fore.LIGHTCYAN_EX}              ║══════════════════════════════════════════════════════════║
{Fore.LIGHTCYAN_EX}              ║ {Fore.YELLOW}[1] {Fore.LIGHTCYAN_EX}NITRO CODE GENERATOR                                 ║
{Fore.LIGHTCYAN_EX}              ║ {Fore.YELLOW}[2] {Fore.LIGHTCYAN_EX}NITRO CODE CHECKER                                   ║
{Fore.LIGHTCYAN_EX}              ║ {Fore.YELLOW}[E] {Fore.LIGHTCYAN_EX}EXIT                                                 ║
{Fore.LIGHTCYAN_EX}              ╚══════════════════════════════════════════════════════════╝
''')

    answer = input(f"{Fore.LIGHTBLACK_EX}[{Fore.LIGHTCYAN_EX}NITRO TOOL{Fore.LIGHTBLACK_EX}]{Fore.LIGHTCYAN_EX}> ")

    if answer == '1':
        Generator()

    elif answer == '2':
        Checker()

def Generator():
    os.system("cls")
    ctypes.windll.kernel32.SetConsoleTitleW(f"[Nitro Tool] By Reds#9999 and etxrnal#9999 | Nitro Generator")
    generated = 0

    print(f'''
{Fore.LIGHTCYAN_EX} ███▄    █  ██▓▄▄▄█████▓ ██▀███   ▒█████     ▄▄▄█████▓ ▒█████   ▒█████   ██▓    
{Fore.LIGHTCYAN_EX} ██ ▀█   █ ▓██▒▓  ██▒ ▓▒▓██ ▒ ██▒▒██▒  ██▒   ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    
{Fore.LIGHTCYAN_EX}▓██  ▀█ ██▒▒██▒▒ ▓██░ ▒░▓██ ░▄█ ▒▒██░  ██▒   ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    
{Fore.LIGHTCYAN_EX}▓██▒  ▐▌██▒░██░░ ▓██▓ ░ ▒██▀▀█▄  ▒██   ██░   ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░    
{Fore.LIGHTCYAN_EX}▒██░   ▓██░░██░  ▒██▒ ░ ░██▓ ▒██▒░ ████▓▒░     ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒
{Fore.LIGHTCYAN_EX}░ ▒░   ▒ ▒ ░▓    ▒ ░░   ░ ▒▓ ░▒▓░░ ▒░▒░▒░      ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░
{Fore.LIGHTCYAN_EX}░ ░░   ░ ▒░ ▒ ░    ░      ░▒ ░ ▒░  ░ ▒ ▒░        ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░
{Fore.LIGHTCYAN_EX}   ░   ░ ░  ▒ ░  ░        ░░   ░ ░ ░ ░ ▒       ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   
{Fore.LIGHTCYAN_EX}         ░  ░              ░         ░ ░                  ░ ░      ░ ░      ░  ░
                                                                                                                                                    
{Fore.LIGHTBLACK_EX}Made By Reds#9999 and etxrnal#9999 | Nitro Code Generator
    ''')

    num=input(f"[{Fore.LIGHTCYAN_EX}Enter The Ammount Of Codes To Generate{Fore.LIGHTBLACK_EX}]{Fore.LIGHTCYAN_EX}> ")

    f = open('Codes.txt', "a+")
        
    for Reds in range(int(num)):
        nitro = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
        print(f'{Fore.LIGHTBLACK_EX}[{Fore.LIGHTCYAN_EX}GENERATED{Fore.LIGHTBLACK_EX}] {Fore.LIGHTCYAN_EX}https://discord.gift/{nitro}')
        ctypes.windll.kernel32.SetConsoleTitleW(f"[Nitro Tool] By Reds#9999 and etxrnal#9999 | Generated: %s" % generated)
        generated += 1
        f.write('https://discord.gift/')
        f.write(nitro)
        f.write("\n")

    f.close()
    input("\n\nFinished Generating Codes. Press Enter To Return To The Main Menu.")

    if input == input:
        Home()

def Checker():
    os.system("cls")
    colorama.init()
    checked = 0

    print(f'''
{Fore.LIGHTCYAN_EX} ███▄    █  ██▓▄▄▄█████▓ ██▀███   ▒█████     ▄▄▄█████▓ ▒█████   ▒█████   ██▓    
{Fore.LIGHTCYAN_EX} ██ ▀█   █ ▓██▒▓  ██▒ ▓▒▓██ ▒ ██▒▒██▒  ██▒   ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    
{Fore.LIGHTCYAN_EX}▓██  ▀█ ██▒▒██▒▒ ▓██░ ▒░▓██ ░▄█ ▒▒██░  ██▒   ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    
{Fore.LIGHTCYAN_EX}▓██▒  ▐▌██▒░██░░ ▓██▓ ░ ▒██▀▀█▄  ▒██   ██░   ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░    
{Fore.LIGHTCYAN_EX}▒██░   ▓██░░██░  ▒██▒ ░ ░██▓ ▒██▒░ ████▓▒░     ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒
{Fore.LIGHTCYAN_EX}░ ▒░   ▒ ▒ ░▓    ▒ ░░   ░ ▒▓ ░▒▓░░ ▒░▒░▒░      ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░
{Fore.LIGHTCYAN_EX}░ ░░   ░ ▒░ ▒ ░    ░      ░▒ ░ ▒░  ░ ▒ ▒░        ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░
{Fore.LIGHTCYAN_EX}   ░   ░ ░  ▒ ░  ░        ░░   ░ ░ ░ ░ ▒       ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   
{Fore.LIGHTCYAN_EX}         ░  ░              ░         ░ ░                  ░ ░      ░ ░      ░  ░                                                                                                                                     
  
{Fore.LIGHTBLACK_EX}Made By Reds#9999 and etxrnal#9999 | Nitro Code Checker
    ''')

    num=input(f"[{Fore.LIGHTCYAN_EX}Press Enter To Start Checking Codes{Fore.LIGHTBLACK_EX}]{Fore.LIGHTCYAN_EX}> ")

    f = open('Codes.txt')

    for line in f:
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(f'{Fore.LIGHTBLACK_EX}[{Fore.LIGHTGREEN_EX}VALID{Fore.LIGHTBLACK_EX}]{Fore.LIGHTCYAN_EX} {nitro}')
            break
            ctypes.windll.kernel32.SetConsoleTitleW(f"[Nitro Tool] By Reds#9999 | Checked: %s" % checked)
            checked += 1
        else:
            print(f'{Fore.LIGHTBLACK_EX}[{Fore.LIGHTRED_EX}INVALID{Fore.LIGHTBLACK_EX}]{Fore.LIGHTCYAN_EX} {nitro}')
            ctypes.windll.kernel32.SetConsoleTitleW(f"[Nitro Tool] By Reds | Checked: %s" % checked)
            checked += 1

    f.close()
    input("\n\nFinished Checking Codes. Press Enter To Return To The Main Menu.")
    Home()

webbrowser.open_new_tab("https://github.com/RedsLovesGames/Nitrogen-and-checker")
Home()
