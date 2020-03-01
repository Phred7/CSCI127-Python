#Lecture 10/22 - Reese Pearsall reesepearsallcs@gmail.com
#StudentObject Dictionary Example


#Our student object. Each key in the dictionary links to a student object
class Student:

    def __init__(self,inName,inMajor,inGpa):
        self.name = inName
        self.major = inMajor
        self.gpa = inGpa


    def getName(self):
        return self.name

    def getMajor(self):
        return self.major

    def getGpa(self):
        return self.gpa

    def setMajor(self,newMajor):
        self.major = newMajor

#Declare empty dictionary
studentD = {
    #studentID : Student Object,
    }

#Function to add student to 
def add():
    ID = input("Enter ID: ")
    name = input("Enter name: ")
    major = input("Enter major: ")
    gpa = input("Enter gpa: ")

    studentD[ID] = Student(name,major,gpa)
    print("Student added!")
    
#Function that prints out student ID (key) and the Student object linked to it
def printDictionary():
    for key in studentD:
        print(key," ",studentD[key].getName()," ",studentD[key].getMajor()," ",studentD[key].getGpa())

#Function that deletes a student from Dictionary
def delete(deleteID): #First, we must get the student ID of the student we want to delete... we get this from main()

    if deleteID in studentD: #we first check to see if that student actually exists in the dictionary
        del studentD[deleteID]
        print("Student Deleted!")
    else:
        print("Student does not exist")


#Function that searches for a student in Dictionary and prints out the object's attributes
def search(searchID):

    if searchID in studentD:
        print("Student found!")
        print(searchID," ",studentD[searchID].getName()," ",studentD[searchID].getMajor()," ",studentD[searchID].getGpa())
        #we have to use getName(),getMajor(),etc on studentD[searchID] because studentD[searchID] is a Student object
    else:
        print("Student not found!")

#function that changes a student's major        
def modify(modifyID, newMajor): #Two input parameters. modifyID = the ID of the student we want to modify. newMajor = the major that we are changing it to

    if modifyID in studentD:
        studentD[modifyID].setMajor(newMajor)
        print("Modified student!")
    else:
        print("Student does not exist")
        

def main():

    #fill dictionary with 3 initial students
    studentD["-1234"] = Student("John Smith","CS",3.2)
    studentD["-5678"] = Student("Mike James","Math",4.0)
    studentD["-2468"] = Student("Daniel Carson","Electrical Engineering",2.0)
    

    choice = 0
    
    while choice != 6:
        print("")
        print("Office of the Registrar Database")
        print("Press 1 to Add a student")
        print("Press 2 to Delete a student")
        print("Press 3 to Modify existing student's major")
        print("Press 4 to Search a student")
        print("Press 5 to Print out Dictionary")
        print("Press 6 to Exit")
        choice = int(input(""))

        if choice == 1:
            add() #calls the add function
        if choice == 2:
            deleteID = input("Enter the ID of the student that you want to delete: ")
            delete(deleteID) #calls the delete function
        if choice == 3:
            modyifyID = input("Enter the ID of the student that you want to change: ")
            newMajor = input("Enter the new Major: ")
            modify(modyifyID,newMajor) #calls the modify function
        if choice == 4:
            searchID = input("Enter the ID of the student that you are looking for: ")
            search(searchID) #calls the search function
        if choice == 5:
            printDictionary() #Calls the print dictionary function




main()
