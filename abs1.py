
import abc
from abc import abstractmethod  # If I don't do this, I have to write the
                                # decorator as "@abc.abstractmethod"

 # So this class will be the parent class:
class Abstract(object):

    @abstractmethod
    def abstractery(self):
        pass
        # So this is the method we're going to define in the child class

    def anotherMethod(self):
        print("This method was defined in the parent class")
        # Here's a method with some actual content

class Concrete(Abstract):
    
    def abstractery(self):
        print("This method was defined in the child class")
        # Isn't this basically the same as polymorphism?


c = Concrete() # instantiate an object
c.abstractery() # call the abstract method defined in the child
c.anotherMethod() # call the method defined in the parent.

 # Wow! I was totally over-thinking this.
 # I think I kinda-sorta get how this would be useful, but I'll need to
 # practice with it to really get it.
