class Employee(object):

    def __init__(self, first, last):
        self.first = first
        self.last = last
        # self.fullname would not work as it wouldn't be updated if either self.first/last were changed later

    @property  # will update at any time if self.first/last are changed
    def fullname(self):
        return f"{self.first} {self.last}"

    @property
    def email(self):
        return f"{self.first}.{self.last}@email.com"

    @fullname.setter  # setter that allows us to change the fullname attribute's value and subsequently change the
    # values of self.first/last
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter  # not the fullname attribute can be deleted using the 'del' keyword
    def fullname(self):
        print("Deleted fullname")
        self.first = None
        self.last = None


parker = Employee("Parker", "Phillips")
parker.last = "Smith"  # will change the last name, fullname, and email

print(parker.first)
print(parker.last)
print(parker.fullname)
print(parker.email)

print()

parker.fullname = "Brandon Phillips"  # will change each attribute as per the names separated by a space
print(parker.first)
print(parker.last)
print(parker.fullname)
print(parker.email)

print()

del parker.fullname
print(parker.first)
print(parker.last)
print(parker.fullname)
print(parker.email)