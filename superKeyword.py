#We need to call parants class methods from child class methods,so we use super keyword
class ParentClass:
    def parent_method(self):
        print("This is parent method ")

class ChildClass(ParentClass):
    def child_method(self):
        print("This is child method")
        super().parent_method

child_obj=ChildClass()
child_obj.child_method()
child_obj.parent_method()