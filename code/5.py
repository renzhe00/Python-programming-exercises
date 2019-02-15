class InputOutString():
    def __init__(self):
        self.s = ''
    
    def getString(self):
        self.s = input()

    def printString(self):
        print(self.s.upper())

test = InputOutString()
test.getString()
test.printString()