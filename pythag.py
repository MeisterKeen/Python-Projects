
# Importing the pythagorean method I wrote in abs1.py:
import abs1

class RightTriangle:

    sideA = 5
    sideB = 11
    sideC = abs1.doAllTheMathForMe(sideA, sideB)
        # Here I'm determining sideC using the method from abs1.py

    def printSides(self):
        print("If side A is length {}, \nand side B is length {},\nthen side C will have length {}!".format(self.sideA, self.sideB, self.sideC))
        # Nicely prints our triangle lengths


class a345Triangle(RightTriangle):

    # 3-4-5 triangles are a sorta "ideal" subset of right triangles

    sideA = 3
    sideB = 4
    sideC = abs1.doAllTheMathForMe(sideA, sideB)
    
    

if __name__ == "__main__":
    x = a345Triangle() # Instantiating the child class
    x.printSides() # Calling a method inherited from the parent class
