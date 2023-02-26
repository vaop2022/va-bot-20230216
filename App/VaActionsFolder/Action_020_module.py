def Action_020(va_data,bot_data, update, context):
    print('Action_020')

    count = va_data.get('command count...command_counts')
    va_data.set('command count...command_counts', count + 1)
    
    va_data.set('text out...text_out', '/val a bot, please talk to me! - ' + str(count))
    if(count > 2):
        va_data.set('text out...text_out', '!!! /val command is more than three times in row')
    
    """
    message = bot_data.get('message from customer...b11')
    bot_obj = bot_data.get('telebot_obj.TeleBot(5662687046******)...b10')

    mess = f'<b>Hi, I know about you )))</b>, {message}'
    bot_obj.send_message(message.chat.id, mess, parse_mode='html')
    """