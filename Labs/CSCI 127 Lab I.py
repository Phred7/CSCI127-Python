roomLength = int(input("What is the length of the room (in feet)?"));
roomWidth = int(input("What is the width of the room (in feet)?"));
tableLength = int(input("What is the length of the table (in feet)?"));
tableWidth = int(input("What is the width of the table (in feet)?"));
spaceBetweenTables = int(input("How much space is required between tables (in feet)?"));
peoplePerTable = int(input("How many people does each table seat?"));

ftPerTableLength = spaceBetweenTables + tableLength;
ftPerTableWidth = spaceBetweenTables + tableWidth;

tablesByLength = int((roomLength - spaceBetweenTables) / ftPerTableLength);
tablesByWidth = int((roomWidth - spaceBetweenTables) / ftPerTableWidth);

totalTables = tablesByLength * tablesByWidth;
totalPeople = totalTables * peoplePerTable;

print("This arrangment seats", totalPeople, "people");

