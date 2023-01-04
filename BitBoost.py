"""
GNU License

Copyright (c) 2022 DaniDuese

"""
from ab5 import hgratient
from typing import Optional
import colorama
import sys
from pystyle import Center, Colorate, Colors, Write
import tls_client
import os


def setTitle(title: Optional[any] = None):
  os.system("title "+title)


setTitle("BitBoost V2 | Server Booster")


def clear():
  if sys.platform in ["linux", "linux2", "darwin"]:
    os.system("clear")
  else:
    os.system("cls")

clear()

sub_ids = []
logo = ("""__________.__  __ __________                       __   
\______   \__|/  |\______   \ ____   ____  _______/  |_ 
 |    |  _/  \   __\    |  _//  _ \ /  _ \/  ___/\   __\ 
 |    |   \  ||  | |    |   (  <_> |  <_> )___ \  |  |  
 |______  /__||__| |______  /\____/ \____/____  > |__|  
        \/                \/                  \/        """)
banner = ("""Please make sure that all your tokens are already in the server you want to boost.\n""")

print(hgratient(logo, [0, 223, 50], [0, 25, 222]))
print(banner)
__guild_id__ = Write.Input("Guild ID: ", Colors.blue_to_green, interval=0.05)
colorama.init(convert=True)


class Nitro:
    def __init__(self, token: str):
        self.token = token
        self.headers = {
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US",
            "authorization": token,
            "referer": "https://discord.com/channels/@me",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9007 Chrome/91.0.4472.164 Electron/13.6.6 Safari/537.36",
            "x-debug-options": "bugReporterEnabled",
            "x-discord-locale": "en-US",
            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDA3Iiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTYxODQyLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=="
        }
        self.session = tls_client.Session(client_identifier="chrome_107")
        self.sub_ids = []

    def removeTokenFromTxt(self):
        with open("tokens.txt", "r") as f:
            lines = f.readlines()
        with open("tokens.txt", "w") as f:
            for line in lines:
                if line.strip("\n") != self.token:
                    f.write(line)

    def hasNitro(self):
        sex = self.session.get(
            "https://discord.com/api/v9/users/@me/guilds/premium/subscription-slots",
            headers=self.headers,
        )
        if sex.status_code in [403, 401]:
            return self._extracted_from_hasNitro_7('Token is invalid, removing.')
        try:
            for sub in sex.json():
                self.sub_ids.append(sub["id"])
        except Exception as e:
            print(e)
            print(sex.text)
        if len(self.sub_ids) == 0:
            return self._extracted_from_hasNitro_7('Token has no nitro, removing.')
        log(f"{colorama.Fore.GREEN}Token has nitro.")
        return True

    # TODO Rename this here and in `hasNitro`
    def _extracted_from_hasNitro_7(self, arg0):
        log(f"{colorama.Fore.RED}{arg0}")
        self.removeTokenFromTxt()
        return False

    def boostServer(self, guildID):
        for i in range(len(self.sub_ids)):
            self.headers["Content-Type"] = "application/json"
            r = self.session.put(
                url=f"https://discord.com/api/v9/guilds/{guildID}/premium/subscriptions",
                headers=self.headers,
                json={
                    "user_premium_guild_subscription_slot_ids": [f"{self.sub_ids[i]}"]
                },
            )
            if r.status_code == 201:
                log(
                    f"{colorama.Fore.GREEN}Boosted {i + 1} of {len(sub_ids)} from {self.token[25:]}"
                )
            elif r.status_code == 400:
                log(
                    f"{colorama.Fore.YELLOW}Boost already used {i + 1} of {len(sub_ids)} from {self.token[25:]}"
                )
            else:
                log(f"{colorama.Fore.RED}ERROR: {r.status_code}")


def log(text):
    print(f"{text}{colorama.Fore.RESET}")


def main():
    with open("tokens.txt", "r") as f:
        tokens = f.read().splitlines()
    for token in tokens:
        nitro = Nitro(token)
        if nitro.hasNitro():
            nitro.boostServer(__guild_id__)


if __name__ == "__main__":
    main()
    input("Press enter to exit.")
