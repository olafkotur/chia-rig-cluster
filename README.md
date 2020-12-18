# Chia Rig Cluster
This is a simple management and monitoring tool to make looking after chia farming and plotting a little easier.

## Setup
* Install `Python3` and libraries.
* Install `Chia Beta 0.17.0` - only use the version specified here!
* Populate the `.env` file from the sample at the bottom of this README.

## Running
* Execute `py main.py`, the "py" may be different depending on your env.
* Listen on Discord for updates - mute everything apart from direct mentions (only called when immediate attention is required).

## Environmental variables
* `ENVIRONMENT=''` - local, development, production
* `RIG_NAME=''` - any
* `DIST=''` - plot destination drive
* `ASSIGN_ID=''` - discord direct mention
* `PROD_DISCORD_HOOK=''` - discord hook for production
* `DEV_DISCORD_HOOK=''` - discord hook for development
* `DIRECTORY=''` - working directory of chia beta dir
* `COMMAND=''` - start plotting command
