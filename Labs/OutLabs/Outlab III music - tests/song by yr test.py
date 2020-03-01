def songs_by_year(year): ##years are the 35th column
    file = open("music.csv", "r");
    numSongs = 0;
    iYear = str(year);
    i = 0;
    for line in file:
        fList = [];
        fList = line.split(",");
        fList.reverse();
        sYear = fList[0];
        sYear = sYear.strip("\n")
        if(iYear == sYear):
            numSongs = numSongs + 1;
    print(numSongs);
    file.close();

print("Printing...");
songs_by_year(2010);
