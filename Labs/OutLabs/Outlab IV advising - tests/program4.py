# -------------------------------------------------
# CSCI 127, Joy and Beauty of Data
# Program 4: Advising System
# Your Name(, Your Partner's Name)
# Last Modified: 
# -------------------------------------------------
# A brief overview of the program.
# -------------------------------------------------


# Your solution goes here ...

# -------------------------------------------------
# Do not change anything below this line
# -------------------------------------------------

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

    # Every student has a major, even if it is "undeclared"
    msu_student = Generic_Major("jalen", "nelson")
    process(msu_student)

    msu_student.set_math_troubles(False)
    advise(msu_student)

    msu_student.set_math_troubles(True)
    msu_student.set_major_troubles(False)
    advise(msu_student)

    # A CLS (College of Letters and Science) major is a subclass of a Generic major
    msu_student = CLS_Major("emma", "phillips")
    process(msu_student)

    # A COE (College of Engineering) major is a subclass of a Generic major
    msu_student = COE_Major("camden", "miller")
    process(msu_student)

    # A Computer Engineering major is a subclass of a COE major
    msu_student = Computer_Engineering_Major("gabriel", "smith")
    process(msu_student)

    # A Physics major is a subclass of a CLS major
    msu_student = Physics_Major("lena", "hamilton")
    process(msu_student)

    # A Computer Science major is a subclass of a COE major
    msu_student = Computer_Science_Major("halley", "jones")
    process(msu_student)

    msu_student.set_math_troubles(False)
    advise(msu_student)

    msu_student.set_math_troubles(True)
    msu_student.set_major_troubles(False)
    advise(msu_student)

# -------------------------------------------------

main()


