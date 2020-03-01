#Lecture 10/24 - Peter Gifford - peter.lee.gifford@gmail.com
#Dictionaries:

exampleDictionary = {
    #key : value,
    "Bart" : "Simpson",
    "Marge" : "Bouvier",
    "Montgomery" : "Burns"
}

# retrieve all keys -

 print(exampleDictionary.keys())
 print("")

# # retrieve all the keys in a list

 tempList = list(exampleDictionary.keys())
 print(tempList)
 print("")

# # retrieve keys one at a time (for processing)-
#
 for key in list(exampleDictionary.values()):
     print(key)
 print("")

# #check if a key exists -

 if "Simpson" in exampleDictionary.values():
     print('Eat my short')
 else :
     print('Dont HAve a Cow, Man!')
 print("")

#do Exercise 16

# retrieve all values

 print(list(exampleDictionary.values()))
 print("")

# # retrieve a specific value or get an error-

 print(exampleDictionary['Bart'])
 print("")

# # retrieve a specific value without the error -

 print(exampleDictionary.get("Flanders"))
 print(exampleDictionary.get("Belcher", "Bob"))
 print("")

# # retrieve all the key-value pairs

 print(exampleDictionary.items())
 print("")

#Aliasing versus Copying

#alias

tempDictionary = exampleDictionary
print(tempDictionary is exampleDictionary)
print(tempDictionary == exampleDictionary)
print("")
tempDictionary["Maggie"] = "Simpson"
print(tempDictionary)
print(exampleDictionary)


#copy

tempDictionary = exampleDictionary.copy()
print(tempDictionary is exampleDictionary)
print(tempDictionary == exampleDictionary)
print("")
tempDictionary["Lisa"] = "Simpson"
print(tempDictionary)
print(exampleDictionary)

#exercise 19

print(sorted(tempDictionary))
