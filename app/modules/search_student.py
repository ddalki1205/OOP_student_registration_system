#work in progress
#does not yet check against the DB file, only the admin list.
#convert from looping through list to looping through student_data.txt

class Search:
    '''
    def search_student(self, student_list, target_id):
        for student in student_list:
            if target_id == student.get_id():
                return student
        return None
    '''
    def search_student(self, path, target_id):
      with open(path, 'r') as f:
        for line in f:
          attributes = line.strip().split(',')
          if target_id in attributes:
             return attributes
        return None