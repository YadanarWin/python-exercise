class Parent(object):

    def altered(self):
        print("PARENT altered()")

class Child(Parent):

    def altered(self):
        print("CHID, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHID, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.altered()
son.altered()
