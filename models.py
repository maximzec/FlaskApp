

class User(object):

    def __init__(self , result):
        self.first_name = result['first_name']
        self.last_name = result['last_name']
        self.email = result ['email']
        self.password = result ['password']

