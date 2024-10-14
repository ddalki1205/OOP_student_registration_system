class AddStudent:
  def __init__(self, constructor, student_list, path):
    self.constructor = constructor
    self.student_list = student_list            #The list in student.py => admin.all_students
    self.path = path                            #THE TXT FILE

  def add_student(self, student):               #this deals with adding and writing(don't use before preloading from file)
    self.student_list.append(student)
    self.write(student)

  def create(self, attributes):
    name, age, id, email, phone = attributes
    new_student = self.constructor(name, age, id, email, phone)
    self.add_student(new_student)

  def read(self):
    with open(self.path, 'r') as f:
      for line in f:
        attributes = line.strip().split(',')
        student = self.constructor(*attributes)
        self.student_list.append(student)

  def write(self, student):
    with open(self.path, 'a') as f:
      display = ",".join(student.attributes())
      f.write(f"{display}\n")