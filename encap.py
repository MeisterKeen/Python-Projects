


class Encapsulated:

    def __init__(self):
        self._dontTouchThisVar = 5 # "protected" attribute
        self.__reallyDont = 10 # "private" attribute

    def okFine(self):
        print(self.__reallyDont)

x = Encapsulated()

print(x._dontTouchThisVar)

'''
print(x.__reallyDont)  
''' # Haha, this throws an error

'''
gotcha = x.__reallyDont
print(gotcha)
''' # This, too, throws an error. So I can't access it at all.

x.okFine()
    # This works!
