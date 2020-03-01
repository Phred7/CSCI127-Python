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
    for line in file:
        fList = [];
        fList = line.split(",");
        lSong = fList[34];
        lSong = lSong.lower();
        lSong = lSong.replace('"', '');
        artistX = fList[2];
        artistX = artistX.lower();
        if(song == lSong):
            artist = fList[2];
            time = int(float(fList[9]));
            artistHeat = float(fList[0]);
        sTime = fList[9];
        heat = fList[0];
        if(i != 0):
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
            ##totalSongs = unique_artists(artistX, i);
        i += 1;
    timeM = time/60;
    print("");
    print("Title: ", cSong);
    print("Duration (to the nearest second): ", str(time) + " seconds.");
    print("Duration: ", str(timeM) + " minutes.");
    print("There are " + str(longerSongs), "songs that are longer, \n" + str(shorterSongs), "songs that are shorter, \nand " + str(sameDuration), "songs that are the same length as the " + cSong + "."); 
    if(hottness == 1):
        print("The artist:", artist, "is the hottest artist!!!"); 
    elif(hottness == 2):
        print("The artist:", artist, "is the 2nd hottest artist!!"); 
    elif(hottness == 3):
        print("The artist:", artist, "is the 3rd hottest artist!");
    elif(hottness <= 0 or hottness >= 1000):
        print("The artist:", artist, "is not even remotly hot.");
        print("(The", str(hottness) + " hottest artist)."); 
    else:
        print("The artist:", artist, "is the", str(hottness) + " hottest artist.");
    ##print("There are a total of", totalSongs, "unique artists in this database"); 
    file.close();

def unique_artists(artistX, w):
    totalSongs = 9999;
    i = 0;
    file = open("music.csv", "r");
    for line in file:
        xList = [];
        xList = line.split(",");
        a = xList[2];
        a = a.lower();
        if(artistX == a):
            totalSongs += (-1);
            print(i, w, str(True)+":", a, artistX)
            w += 1;
        i += 1
    file.close();
    return totalSongs;

song = 'Barking Dogs (From "Piouhgd")';
cSong = song;
song = song.lower();
song = song.replace('"', "");
song_search(song, cSong);
