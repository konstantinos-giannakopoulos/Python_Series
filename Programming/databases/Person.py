class Person():

    def __init__(self, first=None, last=None, age=None):
        self.first = first
        self.last = last
        self.age = age

    def clone_person(self,result):
        self.first = result[0]
        self.last = result[1]
        self.age = result[2]
