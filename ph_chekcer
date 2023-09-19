print( "Running the pH checker program …")
print( "Assuming valid numeric input" )
print(" ")

def question1a(ph):

    if ph == 7:
        return "This ph is neutral."

    elif ph > 10:
        return "This ph is VERY alkali."
        
    elif ph > 7:
        return "This ph is alkali."
        
    elif ph < 4:
        return "This ph is VERY acidic."
    
    elif ph < 7:
        return "This ph is acidic."        


playflag = True

while playflag:

    ph = input("Insert the pH that you want to know about or type 'Quit' to exit the program: ")

    try:
        

        ph = float(ph)

        if ph >= 0 and ph <= 14:
            print(question1a(ph))
        else:
            print("Invalid input. Insert another value.")
            
    except:

        if ph == "Quit" or ph == "quit" or ph == "q":
            playflag = False
        else:
            print("Invalid input. Insert another value.")


print("pH checker program ended")

    

        

    
   
    
