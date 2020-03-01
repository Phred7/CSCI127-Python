# --------------------------------------
# CSCI 127, Lab 6
# October 8, 2018
# Walker Ward
# --------------------------------------

def calculate_attendance(play_name, file):
    aFile = open(file, "r"); ##file format: Attendence, Capacity, Day, Full, Gross, Gross Potential, Month, Name, Preformances, Theatre, Type, Year
    attendence = 0;
    for line in aFile:
        aList = [];
        aList = line.split(",");
        name = str(aList[7]);
        name = name.lower();
        if(name == play_name):  
            attendence = attendence + int(aList[0]);            
    peeps = attendence;
    aFile.close();
    return peeps;

def calculate_revenue(play_name, file):
    rFile = open(file, "r");
    revenue = 0;
    for line in rFile:
        rList = [];
        rList = line.split(",");
        name = str(rList[7]);
        name = name.lower();
        if(name == play_name):
            revenue = revenue + int(rList[4]);            
    monies = revenue;
    rFile.close();
    return monies; 

# --------------------------------------

def main():
    play_name = input("Please enter the name of a play: ")
    play_name = play_name.lower()
    attendance = calculate_attendance(play_name, "broadway.csv")
    print("Total attendance is", "{:,d}".format(attendance))
    revenue = calculate_revenue(play_name, "broadway.csv")
    print("Total revenue is", "${:,d}".format(revenue))

# --------------------------------------

main()
