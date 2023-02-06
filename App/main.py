
# from https://towardsdatascience.com/understanding-python-imports-init-py-and-pythonpath-once-and-for-all-4c5249ab6355
import os
import sys
fpath = os.path.join(os.path.dirname(__file__), 'VaActionsFolder')
sys.path.append(fpath)

import VaBox
import VaScript
import VaConfig
import VaConfigBot
from VaData import VaData


#print(sys.path)

#exit(1)


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
