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

<<<<<<< HEAD
    def save(self,question_id,question):
        self.question_id = question_id
        self.question = question
        self.question_dictionary = dict(id=self.question_id, title=self.question)
=======
    def __init__(self,question_id,question):
        self.question_id = question_id
        self.question = question            

    def save(self,question):
        self.question_dictionary = dict(q_id=self.question_id, question=self.question)
>>>>>>> 5c569a9bca8d36fedff2b57e77a5a06d4465eee5
        return self.question_dictionary
