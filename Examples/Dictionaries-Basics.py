#Lecture 10/22 - Reese Pearsall reesepearsallcs@gmail.com
#Dictionary Basics

myDictionary = {
    #key : value,
    "John" : "Accounting",
    "Sally" : "Engineering",
    "Sam" : "R&D",
    "Hunter Lloyd" : "CEO",
}

#printing out keys (names) in Dictionary
for keys in myDictionary:
    print(keys)

print("")
    
#printing out values (departments) in Dictionary
for keys in myDictionary:
    print(myDictionary[keys])
    
print("")
    
#Printing out keys and Values
for keys,values in myDictionary.items():
    print(keys , "- ", values)

#add new pair to dictionary
myDictionary["Luke"] = "Accounting"

print("")
for keys,values in myDictionary.items():
    print(keys , "- ", values)

#deleting item in dictionary
del myDictionary["Hunter Lloyd"]
#or you can do myDictionary.pop("Hunter Lloyd")

print("")
for keys,values in myDictionary.items():
    print(keys , "- ", values)


#Modify item in dictionary
myDictionary["Sally"] = "CEO"

print("")
for keys,values in myDictionary.items():
    print(keys , "- ", values)


#Print out length of Dictionary
print("Lenght of Dictionary: ",len(myDictionary))
print("")

#We can also use different kinds of data types for our keys or
#Keys do not need to be same data type as values
anotherDictionary = {
    4: 231,
    "String" : 3.14,
    419.231 : [1,2,4,16,64],
}


print(anotherDictionary[4])
print(anotherDictionary["String"])
print(anotherDictionary[419.231])


