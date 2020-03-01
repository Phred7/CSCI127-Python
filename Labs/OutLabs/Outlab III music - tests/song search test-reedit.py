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
        if(fList[15][0] == '"'): 
            nombre = fList[15] + fList[16];
            fList[15] = nombre;
            fList.remove(fList[16]);
        lSong = fList[33];
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
        file.close();

song = '\';
cSong = song;
song = song.lower();
song = song.replace('"', "");
song_search(song, cSong);
