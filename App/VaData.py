import sys
class VaData():
    def __init__(self):
        self.va_data = {}

    def defineVariable(self, key, value):
        temp = []
        temp = key.split('...')
        if temp[1] in self.va_data:
            sys.exit('Error:Attempt to define existing variable [' + key + ']')
        if temp[1] not in self.va_data:
            self.va_data[temp[1]] = {}
            self.va_data[temp[1]][0] = value
            self.va_data[temp[1]][1] = temp[0]
            self.va_data[temp[1]][2] = temp[0]

    def unDefineVariable(self, key, value): # TODO update code
        temp = []
        temp = key.split('...')
        if temp[0] in self.va_data:
            sys.exit('Error:Attempt to define existing variable [' + key + ']')
        if temp[0] not in self.va_data:
            self.va_data[temp[0]] = {}
            self.va_data[temp[0]][0] = value
            self.va_data[temp[0]][1] = temp[1]
            self.va_data[temp[0]][2] = temp[1]

    def set(self, key, value):
        temp = []
        temp = key.split('...')
        if temp[1] in self.va_data:
            self.va_data[temp[1]] = {}
            self.va_data[temp[1]][0] = value
            self.va_data[temp[1]][1] = temp[0]
        if temp[1] not in self.va_data:
            sys.exit('Error: Attempt to set undefined variable')

    def get(self, key):
        temp = []
        temp = key.split('...')
        if temp[1] not in self.va_data:
            sys.exit('Error: Attempt to get undefined variable [' + key + ']')

        return self.va_data[temp[1]][0]

    def getAll(self):

        return self.va_data

    def saveContext(self, user_id, data_obj):
        pass
        temp_dict = self.get('Context variable dict...cvd') 
        temp_dict[user_id] = data_obj
        self.set('Context variable dict...cvd', temp_dict) 

    def loadContext(self, user_id):
        temp_dict = self.get('Context variable dict...cvd')

        return temp_dict[user_id]
    """
    va.defineVariable('Context variable list...cvl', [])
    va.defineVariable('Context variable dict...cvd', {})
    
    def saveContext(self, user_id):
        temp_dict = self.get('Context variable dict...cvd')
        context_var_list = self.get('Context variable list...cvl')
        for context_var in context_var_list:
            if user_id in temp_dict:
                temp_dict[user_id][context_var] = self.get(context_var)
            if user_id not in temp_dict:
                temp_dict[user_id] = {}
                temp_dict[user_id][context_var] = self.get(context_var)

        self.set('Context variable dict...cvd', temp_dict)   

    def loadContext(self, user_id):
        temp_dict = self.get('Context variable dict...cvd')
        context_var_list = self.get('Context variable list...cvl')
        for context_var in context_var_list:
            if user_id in temp_dict:
                self.set(context_var, temp_dict[user_id][context_var])
              
    def isContextExist(self, user_id):
        temp_dict = self.get('Context variable dict...cvd')
        temp_out = False
        if user_id in temp_dict:
            temp_out = True

        return temp_out 

    """