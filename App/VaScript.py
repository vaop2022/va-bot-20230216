
def getVaScript():
    va_script = {
      "Action_000":{
          "_agent_position":{
              "en-US":"In Init block of VA-box",
              "ru-RU":"В блоке Init VA-box"
          },
          "_action_description":{
              "_010":"--> init action"
          },
            "Direction_10":"Action_010",  "_010":"/start"
      },      
      "Action_010_v":{
          "_agent_position":{
              "en-US":"Welcome screen with instructions",
              "ru-RU":"Начальный экран с приветствием и инструкцией"
          },
          "_action_description":{
              "_010":"Начальный экран с приветствием и инструкцией",
              "_020":"dfdfdfdfdfdfdfd",
              "_02220":"dfdfdfdfdfdf   dfdfdfdfd"

          },
            "Direction_10":"Action_020_v",  "_010":"Кнопка подписки",
            "Direction_20":"Action_030_v",  "_010":"Кнопка Выставить счет"
      },      
      "Action_020_v":{
          "_agent_position":{
              "en-US":"Subcription",
              "ru-RU":"Подписка"
          },
          "_action_description":{
              "_010":"Subcription / Информация о текущей подписке"
          },
            "Direction_10":"Action_010_v",  "_010":"Кнопка 'Назад'",
      },
      "Action_030_v":{
          "_agent_position":{
              "en-US":"",
              "ru-RU":""
          },
          "_action_description":{
              "_010":""
          },
            "Direction_10":"Action_XXX",  "_010":"",
            "Direction_20":"Action_XXX_v",  "_010":""
      }      
    };