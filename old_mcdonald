#Old McDonald song generator

print("Old MacDonald had a farm, E I E I O")
print("On his farm he had a duck, E I E I O")
print("With a quack, quack here and a quack, quack there")
print("Here a quack, there a quack, everywhere a quack, quack")
print("Old MacDonald had a farm, E I E I O")


def oldmacdonald (lyrics, animal, playflag):

    if animal != "-1":
        sound = input(str("Please enter an animal sound:: "))
        lyrics.append([animal, sound])
    else:
        playflag = False
        print("The song is over ...")
    return lyrics, playflag
          
playflag = True

lyrics = []

while playflag:

    animal = input(str("Please enter an animal name (or -1 to quit): "))

    lyrics,playflag = oldmacdonald(lyrics, animal, playflag)    

for item in lyrics:

    print("Old MacDonald had a farm, E I E I O")
    print("On his farm he had a {}, E I E I O".format(item[0]))
    print("With a {}, {} here and a {}, {} there".format(item[1], item[1], item[1], item[1]))
    print("Here a {}, there a {}, everywhere a {}, {}".format(item[1], item[1], item[1], item[1]))
    print("Old MacDonald had a farm, E I E I O")
    














# Prime

# def showprimes(test):
#     primeList = []
#     for item in range(2, test+1):
#         if item not in primeList:
#             print (item)
#             for item2 in range(item*item, test+1, item):
#                 primeList.append(item2)

# print(showprimes(10))








    



















