class Boolean:

    MAP = {
        'true': True,
        'false': False
    }
    
    def __init__(self, contents, environment):
        self.__contents = contents

    def evaluate(self):
        return Boolean.MAP[self.__contents]
        
    def is_valid(self):
        return self.__contents in Boolean.MAP
        
