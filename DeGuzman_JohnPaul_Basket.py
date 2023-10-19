print("Fruit Basketttt!")
print("Enter (1-4)")
print("")
numOfFruits = int(input("Enter of no. fruits you want to eat: "))

basket = []
for i in range(numOfFruits):
    print("")
    print("Press A(apple), O(Orange) , M(Mango), G(Guava)")
    b = input("Fruits you catch " + str((i+1)) + " of " + str(numOfFruits) + " : ")

    if str.upper(b) == 'A':
        basket.append("Apple")
    elif str.upper(b) == 'O':
        basket.append("Orange")
    elif str.upper(b) == 'M':
        basket.append("Mango")
    elif str.upper(b) == 'G':
        basket.append("Guava")


print("Your basket now has: " + str(basket))

while(len(basket) !=0):
    eat = input ("Press E to eat fruit: ")
    if(eat.upper() == 'E'):
        basket.pop(len(basket)-1)
    else:
        print("Invalid Input")

print("No more Fruits in basket")