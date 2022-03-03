"""
Регистрирует и обрабатывает сведения о людях.
Для тестирования классов из этого файла запустите его напрямую.
"""
from classtools import AttrDisplay

class Person(AttrDisplay):
    """
    создает и обрабатывает записи о людях
    """
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = round((self.pay * ((100+percent)/100)), 2)

    '''
    def __repr__(self):
        # return '[Person: % s, % s]' % (self.name, self.pay)
        return f'[Person: {self.name}, {self.job}, {self.pay}]'
    '''


class Manager(Person):
    """
    Настроенная версия Person co специальными требованиями
    """

    """переопределяем конструктор, путем выполнения исходного, но
    с изначальным указанием одного из атрибутов родительского класса - job"""
    def __init__(self, name, pay):
        Person.__init__(self, name, 'менеджер', pay)

    def giveRaise(self, percent, bonus=5):
        """расширение метода, путем копирования его из родительского
        класа и модифицирования - плохой свпособ"""
        # self.pay = round((self.pay * ((100+percent+bonus)/100)), 2)

        """расширение метода, путем вызова метода через класс 
        с дополненными аргументами - хороший способо"""
        Person.giveRaise(self, percent + bonus)


class Department:
    def __init__(self, *args):
        self.members = list(args)

    def addMember(self, person):
        self.members.append(person)

    def giveRaises(self, percent):
        for person in self.members:
            person.giveRaise(percent)

    def showAll(self):
        for person in self.members:
            print(person)


if __name__ == '__main__':
    vasya = Person('Вася Иванов', 'программист', 80)
    petya = Manager('Петя Васечкин', 150)

    IT_department = Department(vasya, petya)

    IT_department.showAll()

    kolya = Person('Николай Басков', 'программист', 120)

    IT_department.addMember(kolya)

    IT_department.giveRaises(5)
    IT_department.showAll()

    print(kolya.__dict__)
