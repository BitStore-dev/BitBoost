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


setTitle("BitBoost | Server Booster")


def clear():
  if sys.platform in ["linux", "linux2", "darwin"]:
    os.system("clear")
  else:
    os.system("cls")

clear()

sub_ids = []


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



def log(text):
    print(f"{text}{colorama.Fore.RESET}")


def main():
    with open("tokens.txt", "r") as f:
        tokens = f.read().splitlines()
    for token in tokens:
        nitro = Nitro(token)
        if nitro.hasNitro():
            pass


if __name__ == "__main__":
    main()
    pass
