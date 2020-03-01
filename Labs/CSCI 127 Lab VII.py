
# -----------------------------------------------------
# CSCI 127, Lab 7
# October 16, 2018
# Walker Ward
# -----------------------------------------------------

class Contact():
    
    def __init__(self, first, last, phone):
        self.first = first;
        self.last = last;
        self.phone = phone;
    
    def setFirstName(self, name):
        self.first = name;
    
    def setTitle(self, title):
        self.title = title;

    def getCellNumber(self):
        return self.phone;

    def getAreaCode(self):
        return self.phone[0:3];

    def printEntry(self):
        self.length = len(self.first) + len(self.last) + 1;
        ##print("{:<25}{}".format(self.first+" "+self.last, self.phone));
        if(self.length <= 14):
            print(self.first, self.last,"\t\t" + self.phone);
        else:
            print(self.first, self.last,"\t" + self.phone);    
        

# -----------------------------------------------------
# Do not change anything below this line
# -----------------------------------------------------

def print_directory(contacts):
    print("My Contacts")
    print("-----------")
    for person in contacts:
        person.printEntry()
    print("-----------\n")

# -----------------------------------------------------

def main():
    dad = Contact("Homer", "Simpson", "406-994-0000")
    son = Contact("????", "Simpson", "406-994-5959")
    pun = Contact("Amanda", "Huginkiss", "406-994-4780")

    contacts = [dad, son, pun]

    print_directory(contacts)

    son.setFirstName("Bart")
    dad.setTitle("Dad")
    pun.setTitle("Silly Pun")

    print_directory(contacts)

    print("The area code for cell number", dad.getCellNumber(), "is", \
           dad.getAreaCode())

# -----------------------------------------------------

main()
