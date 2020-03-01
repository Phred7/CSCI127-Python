

def song_search(song, cSong): ##searchs for a specific song and returns details
    file = open("music.csv", "r");
    totalSongs = 9999;
    artist = "";
    artistX = "";
    artistXH = 0.0;
    i = 0;
    total = 0;
    for line in file:
        fList = [];
        fList = line.split(",");
        artistX = fList[2];
        artistX = artistX.lower();
        if(i != 0):
            pass;
            #artistXH = float(fList[0]);
        i += 1;
    total = unique_artists6()

    print(total);
    print(i);
    file.close();

def unique_artists(artistX):
    total = 0;
    file = open("music.csv", "r");
    for line in file:
        xList = [];
        xList = line.split(",");
        a = xList[2];
        a = a.lower();
        if(artistX == a):
            total += 1;
    file.close();
    return total;

def unique_artists2(artistX):
    total = 0;
    file = open("music.csv", "r");
    for line in file:
        xList = [];
        xList = line.split(",");
        a = xList[2];
        a = a.lower();
        if(artistX == a):
            total += 1;
    #total = math.sqrt(total)
    file.close();
    return total;

def unique_artists3(artistX, a):
    #oops
    return x;

def unique_artists4(artistXH, a, total):
##    file = open("music.csv", "r");
##    for xline in file:
##        xList = [];
##        xList = xline.split(",");
##        a = xList[0];
    if(artistXH < a):
        total += 1;
        artistXH = a;
        print(True, "<a", a);
    elif(a == 0):
        total += 1;
        print(True, "== 0:", a);
    return total, artistXH;

def unique_artists5(artistsXH, a):
##    a = [];
##    b = [];
##    c = [];
##    d = [];
##    e = [];
##    f = [];
##    g = [];
##    h = [];
##                if(artistXH == 0):
##                a = a.append(artistXH);
##            elif(artistXH <= 0.33 and artistXH != 0):
##                b = b.append(artistXH);
##            elif(artistXH <= 0.4 and artistXH > 0.33):
##                c = c.append(artistXH);
##            elif(artistXH <= 0.41 and artistXH > 0.4):
##                d = d.append(artistXH);
##            elif(artistXH <= 0.42 and artistXH > 0.41):
##                e = e.append(artistXH);
##            elif(artistXH <= 0.5 and artistXH > 0.41):
##                e = e.append(artistXH);
##            elif(artistXH <= 0.5 and artistXH > 0.41):
##                e = e.append(artistXH);
##            elif(artistXH <= 0.5 and artistXH > 0.41):
##                e = e.append(artistXH);
##            elif(artistXH <= 0.66 and artistXH > 0.5):
##                f = f.append(artistXH);
##            elif(artistXH <= 1.0 and artistXH > 0.66):
##                g = g.append(artistXH);
    return 0;

def unique_artists6():
    i = 0;
    rFile = open("music.csv", "r");
    wFile = open("musicOutput.csv", "w");
    for xline in rFile:
        fList = [];
        fList = xline.split(",");
        if(i != 0):
            artistX = fList[2];
            artistX = artistX.lower();
            wFile.write(artistX);
            wFile.write("\n");
        i += 1;
##        xFile = open("musicOutput.csv", "r");
##    for wLine in xFile:
##        wList = [];
##        wList = wLine.split(",");
    ##write to a text file and then reread from there
    wFile.close();
    return 0;

def unique_artists6():
    i = 0;
    rFile = open("music.csv", "r");
    wFile = open("musicOutput.csv", "w");
    for xline in rFile:
        fList = [];
        fList = xline.split(",");
        if(i != 0):
            artistX = fList[2];
            artistX = artistX.lower();
            wFile.write(artistX);
            wFile.write("\n");
        i += 1;
    wFile.close();
    return 0;

song = 'Barking Dogs (From "Piouhgd")';
cSong = song;
song = song.lower();
song = song.replace('"', "");
song_search(song, cSong);

