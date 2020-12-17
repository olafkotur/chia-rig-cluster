import requests, os

HOOK = 'https://discord.com/api/webhooks/788024639259017247/OegiUapBmigE6N9htGwt9shilolGcHCC59mUPhsn0r0LeeVx929jl7Ws4nuKuMgXP9ZL'

def sendMessage(msg = ''):
  requests.post(HOOK, { 'content': msg })


os.system('echo Hello World')