class Website:
    def __init__(self, type, url):
        self.type = type
        self.url = url


    def show_data(self):
        print(f"Website is created, type is {self.type} , {self.url}") 


job = Website("job", "www.job.am")
job.show_data()