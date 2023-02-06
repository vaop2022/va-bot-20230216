
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
            "Direction_10":"Action_010",  "_010":"/start",
            "Direction_20":"Action_010",  "_020":"any text",
            "Direction_30":"Action_010",  "_030":"answer yes_no",
            "Direction_40":"Action_010",  "_040":"answer yes_no_uptoyou",
            "Direction_50":"Action_010",  "_040":"again"
      },
      "Action_010":{
          "_agent_position":{
              "en-US":"The v-agent is in /start",
              "ru-RU":"v-agent в /start"
          },
          "_action_description":{
              "_010":"empty"
          },
            "Direction_10":"Action_010",  "_010":"/start",
            "Direction_20":"Action_010",  "_020":"any text",
            "Direction_30":"Action_030",  "_030":"answer yes_no",
            "Direction_40":"Action_040",  "_040":"answer yes_no_uptoyou",
            "Direction_50":"Action_010",  "_040":"again"
      },
      "Action_020":{
        "_agent_position":{
              "en-US":"The v-agent is any text",
              "ru-RU":"v-agent в any text"
          },
          "_action_description":{
              "_010":"empty"
          },
        "Direction_10":"Action_010",  "_010":"/start",
        "Direction_20":"Action_020",  "_020":"any text",
        "Direction_30":"Action_030",  "_030":"answer yes_no",
        "Direction_40":"Action_040",  "_040":"answer yes_no_uptoyou",
        "Direction_50":"Action_010",  "_040":"again"
      },
      "Action_030":{
        "_agent_position":{
              "en-US":"The v-agent is answer yes_no",
              "ru-RU":"v-agent в answer"
          },
          "_action_description":{
              "_010":"empty"
          },
        "Direction_10":"Action_010",  "_010":"/start",
        "Direction_20":"Action_010",  "_020":"any text",
        "Direction_30":"Action_010",  "_030":"answer yes_no",
        "Direction_40":"Action_010",  "_040":"answer yes_no_uptoyou",
        "Direction_50":"Action_010",  "_040":"again"
      },
      "Action_040":{
        "_agent_position":{
              "en-US":"The v-agent is answer yes_no_uptoyou",
              "ru-RU":"v-agent в answer"
          },
          "_action_description":{
              "_010":"empty"
          },
        "Direction_10":"Action_010",  "_010":"/start",
        "Direction_20":"Action_010",  "_020":"any text",
        "Direction_30":"Action_010",  "_030":"answer yes_no",
        "Direction_40":"Action_010",  "_040":"answer yes_no_uptoyou",
        "Direction_50":"Action_010",  "_040":"again"
      },   
      "Action_9000":{
          "_agent_position":{
              "en-US":"END",
              "ru-RU":""
          },
          "_action_description":{
              "_010":"empty"
          },
          "Direction_10":"Action_END",  "_010":"",
          "Direction_20":"Action_END",  "_020":"",
          "Direction_30":"Action_30",  "_030":"answer" ,
          "Direction_1000":"Action_END",  "_030":""
      }
    }

    return va_script