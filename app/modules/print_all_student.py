class PrintAllStudents:
    def __init__(self, path, constructor):
        self.path = path  
        self.constructor = constructor 

    def func(self):
        try:
            with open(self.path, 'r') as f:
                for line in f:
                    attributes = line.strip().split(',')
                    student = self.constructor(*attributes)  
                    print(student)  # Print using the __str__ method of StudentInfo
        except FileNotFoundError:
            print("No student data file found.")