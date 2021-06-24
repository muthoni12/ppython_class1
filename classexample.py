'''
#EXAMPLE
Building a system for computer pride.
Comp. pride had diff ppl - student, trainers, management, etc.

But rmr all are ppl but not all can do the same things.
e.g trainer can go to staff kitchen and student can't
e.g trainer can't sign checks

#CHILD vs PARENT
-So, must have different classes.
-The PARENT class however, is the class with
properties applyingto all people in the class.
The CHILD class(es), have properties pertaining to only them
but they can inherit properties from the parent class.
-When deciding what goes in a child class,
remember to remove redundancies
that would go in the parent class anyway.

#FUNCTIONS
-When writing FUNCTIONS inside a class,
think of the verbs, the behaviours,
attached to that class/group.

#PROPERTIES
-Apart from defining functions, you can define PROPERTIES.
-The distiction is that a property is a fact attached to one
and a function is something everything(one) in that class can do.
-All properties of the parent class (in a constructor, maybe)
are inherited by the child class(es).

#DECLARING VARIABLE vs PROPERTIES
-The difference is that, with declaring, it means you want
to put it in a function. You want ot manipulate it.
-But, with a property, it belongs to a class but
you can also manipulate it.

#CONSTRUCTOR
-A class has a specific function called a constructor.
-A constructor is a special function which is called
eveytime you create an instance of a class.
-As long as a property is inside a constructor,
you can access them whenever you want.

#INSTANCE
-An INSTANCE is an individual object of a class.
-An object belonging to a class is an instance of that class.
-Each realized variation of that object is an instance
of its class.
-Creating an instance of a class is like
creating copies of that class.

#SELF
-SELF means you're refering to that class it's in.
-SELF is a special key word which is always
the first parameter of all functions inside a class.

'''

# parent class with only functions
class person:
    def gotothebeach():
        #logic
        pass

    def walk():
        #logic
        pass
# one child class with only functions
class student:
    def sitforexam():
        #logic
        pass

    def learn():
        #logic
        pass
# another child class with only functions
class trainer:
    def teach():
        #logic
        pass

    def usestaffkitchen():
        #logic
        pass



# parent class with constructor,
# properties in constructor and function
class person:
    def __init__(self, name, gender, age):
        pass

    def walk(self, origin, destination):
        pass

# creating an instance below
# must pass parameters everytime you create an instance
newperson = person("muthoni", "F", 19)
newperson.walk("-133.49, 00.10", "-0.24, 1.0")