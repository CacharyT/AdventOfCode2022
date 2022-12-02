#Cachary Tolentino
#12/1/22
#This program will output the highest calories of the elf carrying the most calories

#Main array containing all inputs
calorieListArray = []

#Reading in inputs and assigning each to a slot in an array
with open(r'C:\Users\rance\OneDrive\Documents\My Files\Git\AOC2022\Day1\inputDay1.txt') as f:
    for line in f:
        calorieListArray.append(line)

#Loops through all the listed calories  
currentCalories = 0         
highestCalories = 0 
for cal in calorieListArray:
    if cal == '\n':
        currentCalories = 0
        continue
    else :
        if cal == '\n':
            continue
        currentCalories = currentCalories + int(cal)
        if currentCalories > highestCalories:
            highestCalories = currentCalories


#Prints the highest calories
print(highestCalories)

