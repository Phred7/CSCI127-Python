numC = int(input("Enter the number of courses you are taking: "));

def translate(gradeSTR):
    if(gradeSTR == "A") or (gradeSTR == "a"):
        print("A");
        gradeF = 4.0;
    else:
        gradeF = 0.0;
    return gradeF;

def courseI():
    c1_H = int(input("Enter credits for course 1: "));
    c1_GSTR = input("Enter grade for course 1: ");
    return c1_H, c1_GSTR;

def userInput(nCourses):
    if(nCourses == 1):
        a1, a2 = courseI();
        #print(h1, g1)
        return a1, a2, 0, "z", 0, "z", 0, "z", 0, "z", 0, "z", 0, "z";

def tCourse():
    c1_H = int(input("Enter credits for course 1: "));
    c1_GSTR = input("Enter grade for course 1: ");
    return c1_H, c1_GSTR;

def gpa(c1_h, c1_g, c2_h, c2_g, c3_h, c3_g, c4_h, c4_g, c5_h, c5_g, c6_h, c6_g, c7_h, c7_g):
    gpaOut = ((c1_h*c1_g)+(c2_h*c2_g)+(c3_h*c3_g)+(c4_h*c4_g)+(c5_h*c5_g)+(c6_h*c6_g)+(c7_h*c7_g))/(c1_h+c2_h+c3_h+c4_h+c5_h+c6_h+c7_h);
    return gpaOut;

def main(nC):
    c1H, c1GSTR, c2H, c2GSTR, c3H, c3GSTR, c4H, c4GSTR, c5H, c5GSTR, c6H, c6GSTR, c7H, c7GSTR = userInput(nC);
    c1G = translate(c1GSTR);
    c2G = translate(c2GSTR);
    c3G = translate(c3GSTR);
    c4G = translate(c4GSTR);
    c5G = translate(c5GSTR);
    c6G = translate(c6GSTR);
    c7G = translate(c7GSTR);
    tGPA = gpa(c1H, c1G, c2H, c2G, c3H, c3G, c4H, c4G, c5H, c5G, c6H, c6G, c7H, c7G);
    print(c1H, c1G, c2H, c2G, c3H, c3G, c4H, c4G, c5H, c5G, c6H, c6G, c7H, c7G);
    print(tGPA);

main(numC);

