def all_songs_by_artist(artist): ##artists are the 3rd column ##needs commas removed for two columns see: Has commas.py
    file = open("music.csv", "r");
    songs = [];
    for line in file:
        fList = [];
        fList = line.split(",");
        name = ((fList[2])).lower()
        if(artist == name):
            for i in range(35): ##indexs without value == ""
                z = 1;
                #print(i);
                if(i > 0 and fList[i] != ""): ##allows skipping of columns that are empty (column == "")
                    if(fList[i][0] == '"'): #finds all quotations in each line (through list)
                        x = i;
                        #print("z:", z);
                        while(z != 0):
                            if(fList[x][-1] == '"'):
                                z = 0;
                                nombre = fList[i];
                                for j in range(x-i):
                                    nombre += fList[i+1];
                                    #print("i:", fList[i], "i+1:", fList[i+1], "nombre:", nombre, x, i);
                                    fList.remove(fList[i+1]);
                                fList[i] = nombre
                                #print("flist[i]:", fList[i]);
                                fList[i] = fList[i].replace('"', '');
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

artist = "black debbath"
artist = artist.lower();
all_songs_by_artist(artist);

##for i in range(len(fList)): ##indexs without value == ""
##            if(i > 0):
##                if(fList[i] == ""): ##allows skipping of columns that are empty (column == "")
##                    pass;
##                elif(fList[i][0] == '"'): #finds all quotations in each line (through list)
##                    x = i;
##                    z = 1;
##                    while(z != 0)
##                        if(fList[x][-1] == '"'):
##                            z = 0;
##                            nombre = "";
##                            for j in range(x-i):
##                                nombre += fList[i+1];
##                                print(fList[i], fList[i+1], nombre);
##                                fList.remove(fList[i+1]);
##                                print(flist[i+1]);
##                        else:
##                            x += 1;
        
    
