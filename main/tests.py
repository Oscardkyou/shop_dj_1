<<<<<<< HEAD
from django.test import TestCase

# Create your tests here.
=======
class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def change_password(self, password):
        self.password = password
        print("Your password has been changed to", self.password)

    def __str__(self):
        return "User(name={}, email={}, password={})".format(self.name, self.email, self.password)
    
class Name(User):
    def __init__(self, name, email, password, image):
        super().__init__(name, email, password)
        self.image = image
>>>>>>> d3bd320 (ShopTestDj)
