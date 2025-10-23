#tried putting this into a python notebook, but both pycharm and vscode threw a hissy fit :/ will copy code into a notebook on thursday when at uni PC :-)

expenses = [] #initialize empty array
totalexpense = 0 #initialize our total expenses tracker
while True: #infinite loop
    newexpense = input("Please enter value of expense, or type 'END' to finish: ") #gather user input. i will be using the "END" keyword to break the loop. this could be changed to something else if need be
    if newexpense.upper() == "END": #the .upper() makes the input case insensitive i.e. "eND" or "end" or "eNd" will all work
        break #break loop when end keyword
    else:
        print("You entered: " + newexpense) #spit the input back to the user
        expenses.append(newexpense) #append it to the list (which just adds it to the end - this saves having to count the index and then manually inserting!)
        totalexpense += float(newexpense) # the =+ operator saves typing x = x + y
        print("Total expenses: " + str(totalexpense)) #prints the total expenses
        if float(newexpense) > 100: # detect if expense larger than 100
            print("Specified expense has exceeded the £100 limit! Manager approval required!") #warn the user about manager approval. were this a more complicated system this is where something like a manager call system would go ;-)


print("Total: "+ str(totalexpense)) # spit out the total
print("List of expenses: ") # this is on it's own line for neatness
print(expenses) #spits out the array... not super pretty but it works. could make it prettier using a for loop

