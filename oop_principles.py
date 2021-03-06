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

    def __init__(self,question_id,question):
        self.question_id = question_id
        self.question = question            

    def save(self,question):
        self.question_dictionary = dict(q_id=self.question_id, question=self.question)
        return self.question_dictionary

class Answer(Question):
    """Answer class"""

    def __init__(self,answer_id,answer):       
        self.answer_id = answer_id
        self.answer = answer

    def save(self,answer):
        self.answer_dictionary = dict(a_id=self.answer_id, answer=self.answer)
        return self.answer_dictionary        