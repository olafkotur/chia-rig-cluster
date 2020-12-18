import os
import requests
import subprocess
import dotenv
import platform
import shutil
import time
from datetime import datetime


# env variables
dotenv.load_dotenv()
ENVIRONMENT = os.environ.get('ENVIRONMENT')
RIG_NAME = os.environ.get('RIG_NAME')
DEV_DISCORD_HOOK = os.environ.get('DEV_DISCORD_HOOK')
PROD_DISCORD_HOOK = os.environ.get('PROD_DISCORD_HOOK')
ASSIGN_ID = os.environ.get('ASSIGN_ID')
DIRECTORY = os.environ.get('DIRECTORY')
COMMAND = os.environ.get('COMMAND')
DIST = os.environ.get('DIST')

def moment():
  return datetime.now().strftime("**%H:%M:%S**")

def sendMessage(msg = ''):
  hook = PROD_DISCORD_HOOK if ENVIRONMENT == 'production' else DEV_DISCORD_HOOK
  requests.post(hook, { 'content': msg })

def getDiskInformation(drive):
  usage = shutil.disk_usage(drive)
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
    subprocess.Popen(['powershell.exe', '-Command', '(cd "' + DIRECTORY + '") ; (' + COMMAND + ')']).wait()
  else:
    os.system(COMMAND)

  sendMessage(':100: `' + RIG_NAME + '` - finished plotting at ' + moment())

  # construct and send resource message
  diskUsage = getDiskInformation(DIST)
  rss = ':pizza: `' + RIG_NAME + '` - Resource update:\n```'
  rss = rss + 'Disk Size: ' + str(diskUsage['total']) + ' GiB\n'
  rss = rss + 'Used Space: ' + str(diskUsage['used']) + ' GiB\n'
  rss = rss + 'Free Space: ' + str(diskUsage['free']) + ' GiB\n'
  rss = rss + 'Estimated Plots: ' + str(round(diskUsage['used'] / 106)) + ' (' + str(diskUsage['used'] / 106) +')' + '```'
  sendMessage(rss)

# execution
shouldPlot = True
while (shouldPlot):
  startPlot() # this takes roughly 12 hours to complete
  time.sleep(60 if ENVIRONMENT == 'production' else 1)

  # check if there is enough storage for the next plot
  diskUsage = getDiskInformation(DIST)
  if diskUsage['free'] <= 110:
    sendMessage(':exclamation: `' + RIG_NAME + '` - insufficient space to start the next plot, requesting manual hard drive replacement from <@' + ASSIGN_ID + '>')
    shouldPlot = False
  elif diskUsage['free'] <= 220:
    sendMessage(':exclamation: `' + RIG_NAME + '` - there is only enough space for one more plot, requesting assistance from <@' + ASSIGN_ID + '>')
