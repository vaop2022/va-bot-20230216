
# from https://towardsdatascience.com/understanding-python-imports-init-py-and-pythonpath-once-and-for-all-4c5249ab6355
import os
import sys
fpath = os.path.join(os.path.dirname(__file__), 'VaActionsFolder')
sys.path.append(fpath)

#https://www.youtube.com/watch?v=M2NzvnfS-hI - Connect to PostgreSQL from Python (Using SQL in Python)


import VaBox
import VaScript
import VaConfig
import VaConfigBot
from VaData import VaData

from sqlalchemy import URL
from sqlalchemy import create_engine

hostname = 'localhost'
database = 'postgres'
username = 'postgres'
pwd = 'Postg!2408'
port_id = 5432

url_object = URL.create(
    "postgresql",
    username=username,
    password=pwd,  # plain (unescaped) text
    host=hostname,
    database=database,
)

engine = create_engine(url_object)


print('\nThe end')
exit(1)


va_data = VaData()
VaConfig.setup(va_data)
bot_data = VaData()
VaConfigBot.setup(bot_data)

if False:
    test = va_data.getAll()
    print(test)
    print('------------------------')
    test = bot_data.getAll()
    print(test)
print('------------------------')

VaBox.start(va_data,bot_data)


print('\nThe end')
