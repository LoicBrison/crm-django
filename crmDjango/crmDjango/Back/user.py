
class User:

    def __init__(self,firstname,lastname,email,address,phone):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.address = address
        self.phone = phone

    def getFirstName(self):
        return self.firstname

    def getLastName(self):
        return self.lastname

    def getEmail(self):
        return self.email

    def getPhone(self):
        return self.phone

    def getAddress(self):
        return self.address