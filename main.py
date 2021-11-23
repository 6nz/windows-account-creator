import string, random, threading, os, sys, subprocess
from colorama import Fore, Back, Style

count = input("Thread count: ")

def createaccsloop():
    try:
        nums = string.digits
        new = ''.join(random.choice(nums) for i in range(5))
        os.system(f'title {new}')
        print(Fore.GREEN + f"Adding new user: {new}")
        subprocess.os.system(f'net user Libes{new} Libes{new} /add')
        print(Fore.GREEN + f"Successfully added new user! User: {new}")
    except:
        print(Fore.RED + 'Failed!')
        pass

def thread():
    for i in range(int(count)):
        threading.Thread(target=createaccsloop).start()


def starter():
    print(Fore.RED + 'Starting program!')
    thread()

start = input("Press anything to start the program!")
os.system('cls')

starter()
