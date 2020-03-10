import typing_extensions
import json

from nonebot.default_config import *


with open('cgap.config.json') as file:
    config = json.load(file)


SUPERUSER: int = int(config['super_user'])

WAIT_MINUTE: int = int(config['wait_minute'])

HOST = str(config['host'])
PORT = int(config['port'])
