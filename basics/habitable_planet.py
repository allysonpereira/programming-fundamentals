print("Running Planet Habitable checker program …")
print( "Assuming valid numeric input" )
print(" ")
minTemp = float(input("What is the minimum temperature of the planet: "))
maxTemp = float(input("What is the maximum temperature of the planet: "))

def question1b(minTemp, maxTemp):

    water = True
    crops = True
    habitable = True
    result1 = ""
    result2 = ""
    result3 = ""
    result4 = ""

    if minTemp > 0 and maxTemp < 100: 
        result1 = "Water can be present. "
    else:
        water = False
        result1 = "Water can't be present."

    if minTemp > 21 and minTemp < 32:
        result2 = "Crops can grow. "
    else:
        crops = False
        result2 = "Crops can't grow."

    if water and crops:  
        result3 = "The planet is habitable."  
    else:
        result4 = "The planet is not habitable."

    return result1 + result2 + result3 + result4

answer2 = question1b(minTemp, maxTemp)
print(" The answer is: {} ".format(answer2))
print(" ")
print(" ")
print("Why?")
print("Explaining the result ... ")
print("Water can only be present if the minimum temperature is higher than 0 and the maximum temperature is less than 100.")
print("Crops can only grow if the minimum temperature is higher than 21 and less than 32.")
print("Therefore, the planet can only be habitable if water is present and crops can grow.")
