import string, random, threading, time, os, sys, subprocess
from colorama import Fore, Back, Style

time.sleep(0.5)
count = input("Thread count: ")
accname = input("Account name: ")

def createaccsloop():
    try:
        nums = string.digits
        new = ''.join(random.choice(nums) for i in range(5))
        print(Fore.GREEN + f"Adding new user: {accname}{new}")
        subprocess.os.system(f'net user {accname}{new} {accname}{new} /add')
        print(Fore.GREEN + f"Successfully added new user! User: {accname}{new}")
    except:
        print(Fore.RED + 'Failed!')
        pass

def thread():
    acccount = 0
    threadcount = 0
    for i in range(int(count)):
        threading.Thread(target=createaccsloop).start()
        threadcount += 1
        acccount += 1
        os.system(f'title Total created accounts: {acccount} ┃ Thread count: {count}')


def starter():
    time.sleep(0.5)
    print(Fore.RED + 'Starting program!')
    time.sleep(0.5)
    thread()

start = input("Press anything to start the program!")
os.system('cls')

time.sleep(0.5)
starter()

time.sleep(5)
