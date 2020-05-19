chopstickNumber, spoonNumber, returnNumber = map(int, input().split())

totalNumber = 0

while returnNumber > 0:
    if chopstickNumber // 2 >= spoonNumber:
        chopstickNumber -= 1
    else:
        spoonNumber -= 1
    returnNumber -= 1

if chopstickNumber // 2 <= spoonNumber:
    totalNumber = chopstickNumber // 2
else:
    totalNumber = spoonNumber

print(totalNumber)






