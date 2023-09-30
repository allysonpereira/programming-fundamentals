# Shopping list model

mylist = [["apple", 1], ["blue pen", 2], ["red pen", 3.45], ["pants", 34.88], ["t-shirt", 24.98]]
print("Items in the list:")
for item in mylist:
    print(item[0], item[1], "$")

cartlist = []
amount = 0  # Initialize the variable to keep track of the total amount

buy = ""
while buy.lower() != "q":
    item0 = input("What do you want to buy? ")
    found = False  # Variable to check if the item was found in the list
    for i in mylist:
        if item0 == i[0]:
            amount += i[1]
            cartlist.append(item0)
            found = True
            break  # Exit the loop when item is found

    if not found:
        print("Item not found in the list.")

    buy = input("Do you want to continue? Enter 'Q' to end or any other key to continue: ")

print("You bought:")
for item in cartlist:
    print(item)

print("Total amount is: $" + str(amount))
