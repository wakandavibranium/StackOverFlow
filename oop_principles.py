class User:
    """User class"""
    
    def __init__(self):
        pass

    def signup(self,first_name,last_name,email,password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        return "Registration was successful"

    def login(self,email,password):
        self.email=email
        self.password=password

class Question(User):
    """Question class"""    

    def __init__(self,question):
        self.question = question         