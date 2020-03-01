class Generic_Major():
    def __init__(self, inFirst, inLast):
        self.first = inFirst.capitalize();
        self.last = inLast.capitalize();
        self.major = "Generic";
        self.majorTroubles = False;
        self.mathTroubles = False;
    def get_first_name(self):
        return self.first;
    def get_last_name(self):
        return self.last;
    def get_major(self):
        return self.major;
    def get_major_troubles(self):
        return self.majorTroubles;
    def get_math_troubles(self):
        return self.mathTroubles;
    def set_major(self, major):
        self.major = major;
    def set_major_troubles(self, trouble):
        self.majorTroubles = trouble;
    def set_math_troubles(self, trouble):
        self.mathTroubles = trouble;
    def major_advising(self):
        if(self.majorTroubles == True): 
            print("because you are having troubles with your major:");
            if(self.major == "Computer Science"):
                print("--> visit the CS Student Success Center in Barnard Hall 259");
                print("--> visit a CS professional advisor in Barnard Hall 357");
            if(self.major == "College of Engineering" or "Computer Science" or "Computer Engineering"):
                print("--> visit the EMPower Student Center in Roberts 313");
            elif(self.major == "Physics"):
                print("--> visit the Physics Learning Center in Barnard Hall 230");
            print("--> visit your professor during office hours");
            print("--> visit your academic advisor");
    def math_advising(self):
        if(self.mathTroubles == True):
            print("because you are having troubles with math:");
            print("--> visit the Math Learning Center in Wilson 1-112");            

class COE_Major(Generic_Major):
    def __init__(self, inFirst, inLast):
        super().__init__(inFirst, inLast);
        self.major = "College of Engineering";
    

class Computer_Science_Major(COE_Major):
    def __init__(self, inFirst, inLast):
        super().__init__(inFirst, inLast);
        self.major =  "Computer Science";
        

##class COE_Major(Generic_Major):
##    def __init__(self, inFirst, inLast):
##        super().__init__(inFirst, inLast);
##        self.major = "College of Engineering";
##        super().set_major(self.major);
##        super().set_COE_True();        
##     
##class Computer_Science_Major(COE_Major):
##    def __init_(self, inFirst, inLast):
##        self.major = "Computer Science";
##        super().self.major = self.major
##        super().set_major("Computer Science"); 
        

#--------------------------------------------------------------------------------------

def advise(student):
    print("Student:", student.get_first_name(), student.get_last_name())
    print("Major: " + student.get_major() + ", Major Troubles: " +
          str(student.get_major_troubles()) + ", Math Troubles: " +
          str(student.get_math_troubles()))
    print()
    if not student.get_math_troubles() and not student.get_major_troubles():
        print("No advising is necessary.  Keep up the good work!")
    else:
        student.major_advising()
        student.math_advising()
    print("------------------------------")

# -------------------------------------------------

def process(student):
    advise(student)
    student.set_major_troubles(True)
    student.set_math_troubles(True)
    advise(student)

# -------------------------------------------------

def main():

    # A Computer Science major is a subclass of a COE major
    msu_student = Computer_Science_Major("halley", "jones")
    process(msu_student)


# -------------------------------------------------

main()
