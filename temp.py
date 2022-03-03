class Parent():
    def __init__(self, name='Unknown'):
        self.name = name

    def printname(self):
        print(self.name)

class C1(Parent):
    '''
    def __init__(self, name='Unknown'):
        self.name = name
    '''

    def __str__(self):
        return f'Имя этого объекта - {self.name}'

    def setname(self, name='Inkognito'):
        self.name = name

    # переопределяем метод
    def printname(self):
        print(f'Имя: {self.name}')


    def returnname(self):
        return self.name


human = C1('Petya')
print(human.name)
human.setname('Vova')
print(human.name)

human.printname()
print(human.returnname())

