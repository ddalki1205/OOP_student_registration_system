class StudentInfo:
    def __init__(self, name=None, age=None, id=None, email=None, phone=None):
        self.name = name
        self.age = age
        self.id = id
        self.email = email
        self.phone = phone
        self.all_student = []
  
    def attributes(self):
        return [self.name, self.age, self.id, self.email, self.phone]
  
    def __str__(self):
        return (
            f"\nName:   {self.name}"
            f"\nAge:    {self.age}"
            f"\nID:     {self.id}"
            f"\nEmail:  {self.email}"
            f"\nPhone:  {self.phone}\n"
            )
  
    def get_name(self):
        return self.name
  
    def get_age(self):
        return self.age
  
    def get_id(self):
        return self.id
  
    def get_email(self):
        return self.email
  
    def get_phone(self):
        return self.phone
  
    def set_name(self, new_name):
        self.name = new_name

    def set_age(self, new_age):
        self.age = new_age
  
    def set_id(self, new_id):
        self.id = new_id
    
    def set_email(self, new_email):
        self.email = new_email

    def set_phone(self, new_phone):
        self.phone = new_phone