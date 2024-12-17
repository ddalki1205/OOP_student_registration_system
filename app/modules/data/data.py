class Data:
    DELIMITER = ','
    def __init__(self, student_constructor: object, data_file_path: str):
        self.student_constructor: object = student_constructor
        self.data_file_path: str = data_file_path
        self.students: dict[str : object] = {} # ID : Student Object

    def load_to_program(self):
        with open(self.data_file_path, 'r') as file:
            for line in file.lines():
                attributes = [value.strip() for value in line.strip().split(Data.DELIMITER)]
                
                if not (len(attributes) == 5):
                    return -1
                
                student = self.student_constructor(*attributes)

                self.students[student.id] = student