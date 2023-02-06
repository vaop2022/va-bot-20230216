def getDirection(va_data,bot_data):

    va_data.set('Direction...direction', 'The_code_of_the_direction_is _unknown')

    if  bot_data.get('message type from customer...message type') == bot_data.get('message_type constant: commands...commands'):
        va_data.set('Direction...direction', 'Direction_10')

    if  bot_data.get('message type from customer...message type') == bot_data.get('message type constant: any_text...any text'):
        va_data.set('Direction...direction', 'Direction_20')
           
    if  bot_data.get('message type from customer...message type') == bot_data.get('message_type constant: input...input'):
        if bot_data.get('input [call.data] from customer...input from customer') == bot_data.get('input from customer constant...yes or no'):
            va_data.set('Direction...direction', 'Direction_30')
        if bot_data.get('input [call.data] from customer...input from customer') == bot_data.get('input from customer constant...yes or no or uptoyou'):
            va_data.set('Direction...direction', 'Direction_40')
        if bot_data.get('input [call.data] from customer...input from customer') == bot_data.get('input from customer constant...again'):
            va_data.set('Direction...direction', 'Direction_50')
    