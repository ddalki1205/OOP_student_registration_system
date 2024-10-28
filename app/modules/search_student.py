class Search:
    def __init__(self, path, constructor):
        self.path = path
        self.constructor = constructor  

    def func(self, target_id):
        try:
            with open(self.path, 'r') as f:
                for line in f:
                    attributes = line.strip().split(',')
                    if attributes[2] == target_id:  
                        return self.constructor(*attributes)  
        except FileNotFoundError:
            print("No student data file found.")
        return None