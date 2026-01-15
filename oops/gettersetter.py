class User:
    def __init__(self,email,password):
        self._email = email 
        self.password = password
  
    def get_email(self):  #getter method
        return self._email
    
    def set_email(self,new_email): #setter method
        self._email = new_email
        
    
user1 = User("aMRit123","12345678")

print(user1.get_email())  #got default(1st) email

user1.set_email("amrit123456789")

print(user1.get_email()) #got email after changing (after setter called)