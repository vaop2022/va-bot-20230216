
# from https://towardsdatascience.com/understanding-python-imports-init-py-and-pythonpath-once-and-for-all-4c5249ab6355
import os
import sys
fpath = os.path.join(os.path.dirname(__file__), 'VaActionsFolder')
sys.path.append(fpath)

#https://www.youtube.com/watch?v=M2NzvnfS-hI - Connect to PostgreSQL from Python (Using SQL in Python)
import psycopg2
import psycopg2.extras

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
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    insert_script = 'INSERT INTO payment (id, chat_id) VALUES (%s,%s)'
    insert_value = (4,'test 4')

    #cur.execute(insert_script, insert_value)

    update_script = 'UPDATE payment SET chat_id = \'new\' WHERE id = 1'

    cur.execute(update_script)

    cur.execute('SELECT * FROM payment')

    for record in cur.fetchall():
        print(record['id'], record['chat_id'])

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
