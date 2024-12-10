class StudentInfo:
  def __init__(self, name=None, age=None, student_id=None, email=None, phone=None):
      self.name = name
      self.age = age
      self.student_id = student_id
      self.email = email
      self.phone = phone

  def attributes(self):
      return [self.name, self.age, self.student_id, self.email, self.phone]

  def __str__(self):
      return f"Name: {self.name}\nAge: {self.age}\nID: {self.student_id}\nEmail: {self.email}\nPhone: {self.phone}"

  def get_name(self):
      return self.name

  def get_age(self):
      return self.age

  def get_id(self):
      return self.student_id

  def get_email(self):
      return self.email

  def get_phone(self):
      return self.phone