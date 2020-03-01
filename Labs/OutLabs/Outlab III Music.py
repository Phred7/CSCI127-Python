# ----------------------------------------
# CSCI 127, Joy and Beauty of Data
# Program 3: Msuic CSV Library
# Walker Ward
# Last Modified: October 19, 2018 
# ----------------------------------------
# Gives information about songs from the
# file music.csv according to user input.
# things it can identify: longest song,
# number of songs by year, songs by each
# artist or searches for the details
# about a specific song.
# ----------------------------------------
# ~*~
# Creates a list with the data from any
# given row then converts it to individual
# list indexes.
# ----------------------------------------
# ~*~*~
# This if statement (and its contents)
# detect all occurances of quotations (")
# at the beginning and end of fList
# index's, remove the commas between any
# two sets. Then concatonates all fList
# indexes between any set of quotations
# into one index. Then removing the extra
# indexes.
# ----------------------------------------

def longest_song(): ##duration (in seconds) is the 10th column
    file = open("music.csv", "r");
    time = 0.0;
    i = 0;
    songs = [];
    for line in file: ##For details regarding this for loop see above labled: ~*~
        fList = [];
        fList = line.split(",");
        sTime = fList[9];
        if(i != 0): ##ignores the first row (names of cells)
            sTime = float(sTime);
            if(time < sTime):
                songs.clear()
                time = sTime;
                songs.append(fList[33]);
            if(time == sTime):
                songs.append(fList[33]);
        i += 1
    if(int(time) == int(time-0.5)):
        time = int(time) + 1;
    else:
        time = int(time);
    print("");
    print("Title: ", songs[0]);
    print('Length to the nearest second:', time);
    file.close();

def songs_by_year(year): ##years are the 35th column
    file = open("music.csv", "r");
    numSongs = 0;
    iYear = str(year);
    i = 0;
    for line in file: ##For details regarding this for loop see above labled: ~*~
        fList = [];
        fList = line.split(",");
        fList.reverse();
        sYear = fList[0];
        sYear = sYear.strip("\n")
        if(iYear == sYear):
            numSongs = numSongs + 1;
    print("The number of songs from " + str(year) + " is " + str(numSongs));
    file.close();

def all_songs_by_artist(artist): ##artists are the 3rd column ##needs commas removed for two columns see: Has commas.py
    file = open("music.csv", "r");
    songs = [];
    for line in file: ##For details regarding this for loop see above labled: ~*~
        fList = [];
        fList = line.split(",");
        name = ((fList[2])).lower()
        if(artist == name): ##For details regarding this if statement see above labled: ~*~*~
            for i in range(35): ##indexs without value == ""
                z = 1;
                if(i > 0 and fList[i] != ""): ##allows skipping of columns that are empty (column == "")
                    if(fList[i][0] == '"'): #finds all quotations in each line (through list)
                        x = i;
                        while(z != 0):
                            if(fList[x][-1] == '"'): ##finds quotation pair (end)
                                z = 0;
                                nombre = fList[i];
                                for j in range(x-i): ##concatonates all indexes within quotations and removes extras
                                    nombre += fList[i+1];
                                    fList.remove(fList[i+1]);
                                fList[i] = nombre
                                fList[i] = fList[i].replace('"', ''); #removes quotations from index
                            else:
                                x += 1;
            song = fList[33]
            songs.append(song); ##song title are the 34th column
    songs.sort();
    print("\n" + "Songs In Alphabetical Order \n" + "---------------------------");
    if(len(songs) != 0):
        for i in range(len(songs)):
            print(str(i+1), songs[i]);
    else:
        print("There are no songs by this artist.");
    print("---------------------------");
    file.close();
    
def song_search(song, cSong): ##searchs for a specific song and returns details
    file = open("music.csv", "r");
    time = 0;
    timeM = 0;
    hottness = 0;
    heat = 0.0;
    cHeat = 0.0;
    artist = "";
    artistX = "";
    artistHeat = 0.0;
    longerSongs = 0;
    shorterSongs = 0;
    sameDuration = -1;
    i = 0;
    for line in file: ##For details regarding this for loop see above labled: ~*~
        fList = [];
        fList = line.split(",");
        if(fList[15][0] == '"'): ##removes comma in location cell
            nombre = fList[15] + fList[16];
            fList[15] = nombre;
            fList.remove(fList[16]);
        lSong = fList[33];
        lSong = lSong.lower();
        lSong = lSong.replace('"', '');
        artistX = fList[2];
        artistX = artistX.lower();
        if(song == lSong): ##For details regarding this if statement see above labled: ~*~*~
            for i in range(35): ##indexs without value == ""
                z = 1;
                if(i > 0 and fList[i] != ""): ##allows skipping of columns that are empty (column == "")
                    if(fList[i][0] == '"'): #finds all quotations in each line (through list)
                        x = i;
                        while(z != 0):
                            if(fList[x][-1] == '"'): ##finds quotation pair (end)
                                z = 0;
                                nombre = fList[i];
                                for j in range(x-i): ##concatonates all indexes within quotations and removes extras
                                    nombre += fList[i+1];
                                    fList.remove(fList[i+1]);
                                fList[i] = nombre
                                fList[i] = fList[i].replace('"', ''); #removes quotations from index
                            else:
                                x += 1;
            artist = fList[2];
            time = int(float(fList[9]));
            artistHeat = float(fList[0]);
        sTime = fList[9]; ##grabs duration
        heat = fList[0]; ##grabs heat
        if(i != 0): ##calculations for time and heat
            sTime = int(float(sTime));
            heat = float(heat);
            if(time < sTime):
                longerSongs += 1;
            elif(time > sTime):
                shorterSongs += 1;
            elif(time == sTime):
                sameDuration += 1;
            if(artistHeat < heat):
                hottness += 1;
        i += 1;
    timeM = time/60;
    print(""); ##print all data
    print("Song Data: ");
    print("----------------------------------------");
    print("Title: ", song);
    if(time == 0):
        print("Does not exist in this data");
    else:
        print("Duration: ", str(time) + " seconds.");
        print("Duration: ", '{:.4}'.format(timeM) + " minutes.");
        print("There are " + str(longerSongs), "songs that are longer, \n" + str(shorterSongs), "songs that are shorter, \nand " + str(sameDuration), "songs that are the same length as the " + song + "."); 
        if(hottness == 1):
            print("The artist:", artist, "is the hottest artist!!!"); 
        elif(hottness == 2):
            print("The artist:", artist, "is the 2nd hottest artist!!"); 
        elif(hottness == 3):
            print("The artist:", artist, "is the 3rd hottest artist!");
        elif(hottness <= 0 or hottness >= 1000):
            print("The artist:", artist, "is not even remotly hot.");
            print("(The", str(hottness) + " hottest artist) at this point in time."); 
        else:
            print("The artist:", artist, "is the", str(hottness) + " hottest artist at this point in time.");
    print("----------------------------------------");
    file.close();    


# --------------------------------------

def menu():
    print()
    print("1. Identify longest song.")
    print("2. Identify number of songs in a given year.")
    print("3. Identify all songs by a given artist.")
    print("4. Search for a song and its details")
    print("5. Quit.")

# --------------------------------------

def main():
    choice = 0;
    while (choice != 5):
        menu();
        choice = int(input("Enter your choice: "));
        if (choice == 1):
            longest_song();
        elif (choice == 2):
            year = int(input("Enter desired year: "));
            songs_by_year(year);
        elif (choice == 3):
            artist = input("Enter name of artist: ").lower();
            all_songs_by_artist(artist);
        elif (choice == 4):
            song = input("Enter the name of the song to search for: ");
            print(song);
            cSong = song;
            song = song.lower();
            song = song.replace('"', "");
            song_search(song, cSong);
        elif (choice != 5):
            print("That is not a valid option.  Please try again.");

# --------------------------------------

main()

