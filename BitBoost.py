"""
GNU License

Copyright (c) 2022 DaniDuese

"""
import aiohttp
import asyncio
import os
os.system("pip install tasksio")
import sys
from colorama import Fore
import tasksio
import requests
from typing import Optional
from ab5 import hgratient

def setTitle(title: Optional[any]=None):
  os.system("title "+title)

setTitle("BitBoost | Server Booster")

def clear():
  if sys.platform in ["linux", "linux2", "darwin"]:
    os.system("clear")
  else:
    os.system("cls")
clear()

async def join_server(token, inv):
  headers = {"Authorization": token, "accept": "*/*", "accept-language": "en-US", "connection": "keep-alive", "cookie": f'__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US', "DNT": "1", "origin": "https://discord.com", "sec-fetch-dest": "empty", "sec-fetch-mode": "cors", "sec-fetch-site": "same-origin", "referer": "https://discord.com/channels/@me", "TE": "Trailers", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36", "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"}
  async with aiohttp.ClientSession(headers=headers) as serverjoinersession:
    async with serverjoinersession.post(f"https://discord.com/api/v9/invites/{inv}") as response:
      master = headers + "https://discord.com/api/v9/users/@me" 
      if response.status in (204, 200, 201):
        print(f" Successfully Joined Server")
      else:
        print(f" Failed To Join Server, Status Code: {response.status}")
        print(" Please try again")

async def boost_server(guildid, token):
  headers = {"Authorization": token, "accept": "*/*", "accept-language": "en-US", "connection": "keep-alive", "cookie": f'__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US', "DNT": "1", "origin": "https://discord.com", "sec-fetch-dest": "empty", "sec-fetch-mode": "cors", "sec-fetch-site": "same-origin", "referer": "https://discord.com/channels/@me", "TE": "Trailers", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36", "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"}
  async with aiohttp.ClientSession(headers=headers) as ClientSession:
    async with ClientSession.get(f"https://discord.com/api/v9/users/@me/guilds/premium/subscription-slots") as nvmmm:
      if nvmmm.status == 200:
        idk_var = await nvmmm.json()
        for varr in idk_var:
          id__ = varr['id']
          payload = {"user_premium_guild_subscription_slot_ids": [id__]}
          master = 0 + "v9/guilds"
          async with ClientSession.put(f"https://discord.com/api/v9/guilds/{guildid}/premium/subscriptions", json=payload) as boost_req:
            btxt = await boost_req.text()
            if "id" in btxt:
              print(f" Successfully Boosted Server")
            else:
              print(" Failed To Boost Server, Unknown Error Occurred")


banner = f"""\n{Fore.BLUE}[1]{Fore.RESET} Server Joiner\n\n{Fore.BLUE}[2]{Fore.RESET} Boost Server\n"""


async def start_join(inv):
  async with tasksio.TaskPool(10_000) as pool:
    for token in open('tokens.txt', 'r').readlines():
      tk = token.strip()
      await pool.put(join_server(tk, inv))

async def start_boost(id):
  async with tasksio.TaskPool(10_000) as pool:
    for token in open('tokens.txt', 'r').readlines():
      tk = token.strip()
      await pool.put(boost_server(id, tk))

logo = ("""__________.__  __ __________                       __   
\______   \__|/  |\______   \ ____   ____  _______/  |_ 
 |    |  _/  \   __\    |  _//  _ \ /  _ \/  ___/\   __\ 
 |    |   \  ||  | |    |   (  <_> |  <_> )___ \  |  |  
 |______  /__||__| |______  /\____/ \____/____  > |__|  
        \/                \/                  \/        """)

print(hgratient(logo,[0,223,50],[0,25,222]))
print(banner)
ch = input("Choice: ")
try:
  c = int(ch)
except ValueError:
  print(" Use Number To Choose.")
  sys.exit()
  
if c == 1:
  invv = input(" Enter Invite Code: discord.gg/")
  asyncio.run(start_join(invv))
elif c == 2:
  g = int(input("| Enter Guild ID: "))
  asyncio.run(start_boost(g))
else:
  print(" Invaild Option")
  exit(0)
