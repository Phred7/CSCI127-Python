# ---------------------------------------
# CSCI 127, Joy and Beauty of Data
# Program 1: GPA Calculator 
# Walker Ward
# Last Modified: September 12, 2018 
# ---------------------------------------
# Calculates Users GPA based on inputs:
# Number of Classes, Grade in each class,
# number of credit hrs per course
# ---------------------------------------

def translate(gradeSTR):
    if(gradeSTR == "A") or (gradeSTR == "a"):
        gradeF = 4.0;
    elif(gradeSTR == "A-") or (gradeSTR == "a-"):
        gradeF = 3.7;
    elif(gradeSTR == "B+") or (gradeSTR == "b+"):
        gradeF = 3.3;
    elif(gradeSTR == "B") or (gradeSTR == "b"):
        gradeF = 3.0;
    elif(gradeSTR == "B-") or (gradeSTR == "b-"):
        gradeF = 2.7;
    elif(gradeSTR == "C+") or (gradeSTR == "c+"):
        gradeF = 2.3;
    elif(gradeSTR == "C") or (gradeSTR == "c"):
        gradeF = 2.0;
    elif(gradeSTR == "C-") or (gradeSTR == "c-"):
        gradeF = 1.7;
    elif(gradeSTR == "D+") or (gradeSTR == "d+"):
        gradeF = 1.3;
    elif(gradeSTR == "D") or (gradeSTR == "d"):
        gradeF = 1.0;
    elif(gradeSTR == "F") or (gradeSTR == "f"):
        gradeF = 0.0;
    else:
        gradeF = 0.0;
    return gradeF;

def courseI():
    c1H = int(input("Enter credits for course 1: "));
    c1GSTR = input("Enter grade for course 1: ");
    print(" ");
    return c1H, c1GSTR;

def courseII():
    c2H = int(input("Enter credits for course 2: "));
    c2GSTR = input("Enter grade for course 2: ");
    print(" ");
    return c2H, c2GSTR;

def courseIII():
    c3H = int(input("Enter credits for course 3: "));
    c3GSTR = input("Enter grade for course 3: ");
    print(" ");
    return c3H, c3GSTR;

def courseIV():
    c4H = int(input("Enter credits for course 4: "));
    c4GSTR = input("Enter grade for course 4: ");
    print(" ");
    return c4H, c4GSTR;
    
def courseV():
    c5H = int(input("Enter credits for course 5: "));
    c5GSTR = input("Enter grade for course 5: ");
    print(" ");
    return c5H, c5GSTR;
    
def courseVI():
    c6H = int(input("Enter credits for course 6: "));
    c6GSTR = input("Enter grade for course 6: ");
    print(" ");
    return c6H, c6GSTR;
    
def courseVII():
    c7H = int(input("Enter credits for course 7: "));
    c7GSTR = input("Enter grade for course 7: ");
    print(" ");
    return c7H, c7GSTR;

def userInput(nCourses):
    if(nCourses == 1):
        a1, a2 = courseI();
        return a1, a2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0;
    elif(nCourses == 2):
        a1, a2 = a1, a2 = courseI();
        b1, b2 = courseII();
        return a1, a2, b1, b2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0;
    elif(nCourses == 3):
        a1, a2 = courseI();
        b1, b2 = courseII();
        c1, c2 = courseIII();
        return a1, a2, b1, b2, c1, c2, 0, 0, 0, 0, 0, 0, 0, 0;
    elif(nCourses == 4):
        a1, a2 = courseI();
        b1, b2 = courseII();
        c1, c2 = courseIII();
        d1, d2 = courseIV();
        return a1, a2, b1, b2, c1, c2, d1, d2, 0, 0, 0, 0, 0, 0;
    elif(nCourses == 5):
        a1, a2 = courseI();
        b1, b2 = courseII();
        c1, c2 = courseIII();
        d1, d2 = courseIV();
        e1, e2 = courseV();
        return a1, a2, b1, b2, c1, c2, d1, d2, e1, e2, 0, 0, 0, 0;
    elif(nCourses == 6):
        a1, a2 = courseI();
        b1, b2 = courseII();
        c1, c2 = courseIII();
        d1, d2 = courseIV();
        e1, e2 = courseV();
        f1, f2 = courseVI();
        return a1, a2, b1, b2, c1, c2, d1, d2, e1, e2, f1, f2, 0, 0;
    elif(nCourses == 7):
        a1, a2 = courseI();
        b1, b2 = courseII();
        c1, c2 = courseIII();
        d1, d2 = courseIV();
        e1, e2 = courseV();
        f1, f2 = courseVI();
        g1, g2 = courseVII();
        return a1, a2, b1, b2, c1, c2, d1, d2, e1, e2, f1, f2, g1, g2;
    else:
        print("FAILED");

def gpa(c1_h, c1_g, c2_h, c2_g, c3_h, c3_g, c4_h, c4_g, c5_h, c5_g, c6_h, c6_g, c7_h, c7_g):
    gpaOut = ((c1_h*c1_g)+(c2_h*c2_g)+(c3_h*c3_g)+(c4_h*c4_g)+(c5_h*c5_g)+(c6_h*c6_g)+(c7_h*c7_g))/(c1_h+c2_h+c3_h+c4_h+c5_h+c6_h+c7_h);
    return gpaOut;

def main():
    numC = int(input("Enter the number of courses you are taking: "));
    print(" ");
    c1H, c1GSTR, c2H, c2GSTR, c3H, c3GSTR, c4H, c4GSTR, c5H, c5GSTR, c6H, c6GSTR, c7H, c7GSTR = userInput(numC);
    c1G = translate(c1GSTR);
    c2G = translate(c2GSTR);
    c3G = translate(c3GSTR);
    c4G = translate(c4GSTR);
    c5G = translate(c5GSTR);
    c6G = translate(c6GSTR);
    c7G = translate(c7GSTR);
    tGPA = gpa(c1H, c1G, c2H, c2G, c3H, c3G, c4H, c4G, c5H, c5G, c6H, c6G, c7H, c7G);
    #print(c1H, c1G, c2H, c2G, c3H, c3G, c4H, c4G, c5H, c5G, c6H, c6G, c7H, c7G);
    print("Your GPA is ", "{0:.2f}".format(tGPA));

main();

    

