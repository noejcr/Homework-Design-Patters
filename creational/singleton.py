#Singleton.py
class Borg:
    """Borg class making class attributes global"""
    #Attribute dictionary
    _shared_state = {}

    def __init__(self):
        #make it an attribute dictionary
        self.__dict__=self._shared_state

class Singleton(Borg): #Inherits from the Borg class
    """This class now share all attibutes amoung its various instances"""
    #This essenstially makes the singleton objects an object-oriented global variable

    def __init__(self, **kwargs):
        Borg.__init__(self)
        #Update the attribute dictionary by inserting new key-value pair
        self._shared_state.update(kwargs)

    def __str__(self):
        #returns the attribute dictionary for printing
        return str(self._shared_state)
    
#Let's create a singleton object and add our first acronym
x = Singleton(HTTP="Hyper Text Transfer Protocol")
#Print the object
print(x)
#Let's create another singleton object if it refers to the same attribute dictionary by adding anothe acronym
y = Singleton(FTP="File Transfer Protocol")
#print the object
print(y)
