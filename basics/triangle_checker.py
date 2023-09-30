print("Running the Triangle Type Checker program …")
print("You may assume that the 3 input numbers are valid integer numbers greater than 0.")
sideA = int(input("Enter one integer value: "))
sideB = int(input("Enter another integer value: "))
sideC = int(input("Enter one last integer value: "))

def question1c(sideA, sideB, sideC):

    isTriangle = ""
    triangle123 = ""
    triangleType = 1

    if sideA+sideB > sideC and sideB+sideC > sideA and sideA+sideC > sideB:
        
        isTriangle = "It's a valid triangle."
        
        if sideA == sideB:
            triangleType += 1

        if sideA == sideC:
            triangleType += 1
            
        if sideB == sideC:
            triangleType += 1
        
        if triangleType == 1:
            triangle123 = "It's a scalene triangle."
        
        if triangleType == 2:
            triangle123 = "It's a isosceles triangle."

        if triangleType == 4:
            triangle123 = "It's a equilateral triangle."


    else:
        isTriangle = "It's not a valid triangle."

    
    return isTriangle + triangle123

answer3 = question1c(sideA, sideB, sideC)
print(" The answer is: {} ".format(answer3))
