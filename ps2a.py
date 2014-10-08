 # Problem Set 2 (Part III) 
 # Name:  Greg Padin
 # Collaborators: None
 # Time: 3:00 
 # 
sizeA = 6 #must be smallest quantity
sizeB = 9
sizeC = 20

quantityA = 0
quantityB = 0
quantityC = 0

NoOfNuggets = 1

isValidCombination = False

NoOfConsecutive = 0 #increment until = SizeA (once you hit size a consecutive valid numbers, any combination above that can be made)

lastInvalidCombo = 0

while NoOfConsecutive < sizeA:
    while quantityC * sizeC <= NoOfNuggets  and isValidCombination == False: #(How many orders of sizeC you can have before exceeding the desired NoOfNuggets)
        while quantityB * sizeB + (sizeC * quantityC)<= NoOfNuggets  and isValidCombination == False: #(How many orders of sizeA you can have before exceeding the desired NoOfNuggets)
            while (sizeA * quantityA) + (sizeB * quantityB) + (sizeC * quantityC) <= (NoOfNuggets) and isValidCombination == False: #(How many orders of sizeA you can have before exceeding the desired NoOfNuggets)
                if (sizeA * quantityA) + (sizeB * quantityB) + (sizeC * quantityC) == NoOfNuggets:
                    isValidCombination = True
                quantityA += 1
            quantityA = 0
            quantityB += 1
        quantityB = 0
        quantityC += 1
    if isValidCombination == True:
        NoOfConsecutive += 1
    else:
        NoOfConsecutive = 0
        lastInvalidCombo = NoOfNuggets

    NoOfNuggets += 1
    quantityA = 0
    quantityB = 0
    quantityC = 0
    isValidCombination = False
print 'Largest number of McNuggets that cannot be bought in exact quantity: ' + str(lastInvalidCombo)
