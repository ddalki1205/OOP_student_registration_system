class DataProcessor:
    DELIMITER = ','
    def __init__(self, student_constructor: object, data_file_path: str):
        self.student_constructor: object = student_constructor
        self.data_file_path: str = data_file_path
        self.students: dict[str : object] = {} # ID : Student Object

    def load_to_program(self):
        print("Loading student data to program...")
        with open(self.data_file_path, 'r') as file:
            for line in file.readlines():
                attributes = line.strip().split(DataProcessor.DELIMITER)
                
                if not (len(attributes) == 5):
                    return -1
                
                print(f"Creating student with attributes: {attributes}")
                student = self.student_constructor(*attributes)
                self.students[student.id] = student

            return 0

    def fetch_student_by_id(self, id: str):
        result = self.students.get(id)
        return result if result else None
    
    def add_student_to_program(self, name: str, age: str, id: str, email: str, phone: str):
        errors = {}

        check_for_duplicate_id = self.fetch_student_by_id(id)
        

        errors["name"] = "Name is required" if not name else None
        errors["age"] = "Age is required" if not age else None
        errors["id"] = "ID is required" if not id else f"The ID '{id}' is already taken" if not check_for_duplicate_id else None
        errors["email"] = "Email is required" if not email else None
        errors["phone"] = "Phone Number is required" if not phone else None

        found_error = False
        for value in list(errors.values()):
            if not value:
                found_error = True
                break
        
        if found_error:
            return errors
        
        student = self.student_constructor(name, age, id, email, phone)

        self.students[student.id] = student

        return student