def getDirection(va_data,bot_data):

    va_data.set('Direction...direction', 'The_code_of_the_direction_is _unknown')


    def Action_000_case(va_data,bot_data):
        pass
        print('Action_000_case')

    def Action_010_case(va_data,bot_data):
        pass
        print('Action_010_case', va_data)

    def Action_020_case(va_data,bot_data):
        pass
        print('Action_020_case')

    def Action_030_case(va_data,bot_data):
        pass
        print('Action_030_case')

    def Action_040_case(va_data,bot_data):
        pass
        print('Action_040_case')

    def Action_9000_case(va_data,bot_data):
        pass
        print('Action_9000_case')


    switch_options = {
        'Action_000':Action_000_case,
        'Action_010':Action_010_case,
        'Action_020':Action_020_case,
        'Action_030':Action_030_case,
        'Action_040':Action_040_case,
        'Action_9000':Action_9000_case
    }

    current_action = va_data.get('The current Action...current action')

    switch_options[current_action](va_data,bot_data)


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
    


    