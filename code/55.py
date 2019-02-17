class MyError(Exception):
    def __init__(self, msg):
        super().__init__()
        self.msg = msg

    def display(self):
        print(self.msg)

myError = MyError('something wrong!')
myError.display()