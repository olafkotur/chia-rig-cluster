import os
import requests
import subprocess
import dotenv
import platform
import shutil
from datetime import datetime


# env variables
dotenv.load_dotenv()
ENVIRONMENT = os.environ.get('ENVIRONMENT')
RIG_NAME = os.environ.get('RIG_NAME')
DISCORD_HOOK = os.environ.get('DISCORD_HOOK')
DIRECTORY = os.environ.get('DIRECTORY')
TEMP = os.environ.get('TEMP')
DIST = os.environ.get('DIST')

def moment():
  return datetime.now().strftime("**%H:%M:%S**")

def sendMessage(msg = ''):
  if ENVIRONMENT == 'production':
    requests.post(DISCORD_HOOK, { 'content': msg })
  else:
    print('Skipping send message: ' + msg)

def getDiskInformation():
  usage = shutil.disk_usage('/')
  return {
    'total': usage.total // (1024 ** 3),
    'used': usage.used // (1024 ** 3),
    'free': usage.free // (1024 ** 3),
  }

def startPlot():
  sendMessage(':island: `' + RIG_NAME + '` - initiating new plot at ' + moment())

  # initiate plot
  operatingSystem = platform.system()
  if operatingSystem == 'Windows':
    subprocess.run(['powershell.exe', '-Command', '(cd ./) ; (py mock_plot.py)'])
  else:
    os.system('python3 /Users/olafkotur/Documents/chia-rig-cluster/mock_plot.py')

  sendMessage(':100: `' + RIG_NAME + '` - finished plotting at ' + moment())

  # construct and send resource message
  diskUsage = getDiskInformation()
  rss = ':pizza: `' + RIG_NAME + '` - Resource update\n```'
  rss = rss + 'Disk Size: ' + str(diskUsage['total']) + '\n'
  rss = rss + 'Used Space: ' + str(diskUsage['used']) + '\n'
  rss = rss + 'Free Space: ' + str(diskUsage['free']) + '\n'
  rss = rss + 'Estimated Plots: ' + str(diskUsage['used'] / 106) + '```'
  sendMessage(rss)

# execution
startPlot()
