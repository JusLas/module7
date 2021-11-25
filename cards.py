class BusinessCard:
    def __init__(self, name, company, position,business_phone,  email, priv_phone):
        self.name = name
        self.company = company
        self.position = position
        self.business_phone = business_phone
        self.email = email
        self.priv_phone = priv_phone

    def print_me(self):
        print(f'{self.name},{self.company},{self.position},{self.email}')

    def __str__ (self):
        return f'{self.name},{self.company},{self.email}'
        
    def contact (self):
        print("Kontaktuję się z", self.name,self.company, self.email)
    
    @property
    def birth_date (self):
        return self.__birth_date

    @birth_date.setter
    def birth_date(self,value):
        self.__birth_date = value
    
    @property
    def lenght(self):
        return f'{len(self.name)}'

#7.2




class BaseContact:
    def __init__(self, name,email, priv_phone):
        self.name = name
        self.email = email
        self.priv_phone = priv_phone

    def contact (self):
        print("Wybieram numer", self.priv_phone, "i dzwonie do", self.name)
    
    @property
    def lenght(self):
        return f'{len(self.name)}'

class BusinessContact(BaseContact):
    def __init__(self, name, company, position,business_phone,  email, priv_phone):
        super().__init__(name,email,priv_phone)
        self.company = company
        self.position = position
        self.business_phone = business_phone
    def contact (self):
        print("Wybieram numer", self.business_phone, "i dzwonie do", self.name)

    



     

    