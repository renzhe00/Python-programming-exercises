class Person():
    name = 'Person'

    def __init__(self, name = None):
        self.name = name

renzhe = Person('renzhe')
print('{0} name is {1}'.format(Person.name, renzhe.name))

renzhe11 = Person()
renzhe.name = 'renzhe11'
print('{0} name is {1}'.format(Person.name, renzhe.name))