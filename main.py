import os
import requests
import subprocess
import dotenv
from datetime import datetime

dotenv.load_dotenv()

RIG_NAME = os.environ.get('RIG_NAME')
DISCORD_HOOK = os.environ.get('DISCORD_HOOK')

def moment():
  return datetime.now().strftime("**%H:%M:%S**")

def sendMessage(msg = ''):
  requests.post(DISCORD_HOOK, { 'content': msg })

def startPlot():
  sendMessage(':island: `' + RIG_NAME + '` - initiating new plot at ' + moment())
  subprocess.run(['powershell.exe', '-Command', '(cd ./) ; (py mock_plot.py)'])
  sendMessage(':island: `' + RIG_NAME + '` - initiating new plot at ' + moment())
  print('Done')

startPlot()