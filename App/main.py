
# from https://towardsdatascience.com/understanding-python-imports-init-py-and-pythonpath-once-and-for-all-4c5249ab6355
import os
import sys
fpath = os.path.join(os.path.dirname(__file__), 'VaActionsFolder')
sys.path.append(fpath)

import psycopg2

import VaBox
import VaScript
import VaConfig
import VaConfigBot
from VaData import VaData



hostname = 'localhost'
database = 'postgres'
username = 'postgres'
pwd = 'Postg!2408'
port_id = 5432

conn = None
cur = None

try:
    conn = psycopg2.connect(
            host = hostname,
            dbname = database,
            user = username,
            password = pwd,
            port = port_id
        )
    cur = conn.cursor()

    insert_script = 'INSERT INTO payment (id, chat_id) VALUES (%s,%s)'
    insert_value = (4,'test 4')

    cur.execute(insert_script, insert_value)

    conn.commit()
except Exception as error:
    print('error:[ ' + str(error) + ' ]')
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()  
    print('\nThe end in -finally-')
    exit(1)  

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
