def process_seasons(seasons):
    return 0;

##games = 0;
##points = 0;
##loss = 0;
##tie = 0;
##win = 0;
soccer_seasons = [[1, 3], [1, 1], [1, 0], [20, 30]];
numOfSeasons = len(soccer_seasons); #4

#print(soccer_seasons[0]);
#print(len(soccer_seasons));


for i in range(len(soccer_seasons)):
#for i in range(1):
    games = 0;
    points = 0;
    loss = 0;
    tie = 0;
    win = 0;
    season = i + 1;
    games, points = soccer_seasons[i];
    print("games:", games, "points:", points);
    if(games == 1):
        if(points%3 == 0):
            if(points/3 < games):
                win = win + int(points/3);
                loss = loss + int(games-win);
            else:
                win = win + int(points/3);
        elif(points%3 == 1 or points%3 == 2):
            win = win + int((points - 1)/3);
            tie = tie + int(points%3);
            loss = loss + int(games-(win+tie));
    elif(games > 1):
        n = int(points/3);
        print(n);
        z = 0;
        for i2 in range(n):
            loss = 0;
            tie = 0;
            win = 0;
            if(i2 >= 4):
                if(True):
                    loss = n - ((2*i2) - 8);
                    win = n - (i2-4);
                    tie = 3 * (i2-4);
                    print(win, tie, loss);
                    if(loss <= 0 or win <= 0):
                        break;
    results = [win, tie, loss]
    print("Season "+str(season)+" results: wins, ties, losses:", results);

##games4 = 0;
##points4 = 0;
##games4, points4 = soccer_seasons[3];
##n = 20 #int(points4/3)
##games = 0;
##points = 0;
##print(n)

##for i in range(n):
##    loss = 0;
##    tie = 0;
##    win = 0
##    #print(i);
##    if(i >= 4):
##        if(True):
##            loss = n - ((2*i) - 8);
##            win = n - (i-4);
##            tie = 3 * (i-4);
##            if(loss < 0 or win < 0):
##                break;
##        print(win, tie, loss);
