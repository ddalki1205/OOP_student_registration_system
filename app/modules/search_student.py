#work in progress
#does not yet check against the DB file, only the admin list.
#convert from looping through list to looping through student_data.txt

class Search:
    def func(self, db, target_id):
        for student in db:
            if target_id == student.get_id():
                return student
        return None