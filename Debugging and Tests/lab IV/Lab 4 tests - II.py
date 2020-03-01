def process_seasons(seasons):
    z = 0;
    resA1 = [];
    results2 = [];
    for i in range(len(seasons)):
        games = 0;
        points = 0;
        loss = 0;
        tie = 0;
        win = 0;
        season = i + 1;
        games, points = seasons[i];
        array = [];
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
            results = [win, tie, loss]
            resA1.insert(i, [results]);
        elif(games > 1):
            n = int(points/3);
            for x in range(n):
                if(x >= 4):
                    if(loss >= 0 and win >= 0):
                        loss = n - ((2*x) - 8);
                        win = n - (x-4);
                        tie = 3 * (x-4);
                        #print(win, tie, loss);
                        array.insert(x, [win, tie, loss]);
                if(x < 4 and games < 11):
                    win = int(points/3) - x;
                    tie = points%3 + (3*x);
                    loss = games - (win+tie);
                    if(loss >= 0 and win >= 0 and tie >= 0):
                        array.insert(x, [win, tie, loss]);
                        
            resA1.insert(i, [array]);
        print("Season "+str(season)+" results: wins, ties, losses:", resA1[season-1]);
        #print(str(array));
    return resA1;



soccer_seasons = [[1, 3], [1, 1], [1, 0], [2, 3], [2, 4], [10, 15], [10, 16], [10, 17], [20, 30]];
soccerSeasonResults = process_seasons(soccer_seasons);

##print("SR:", seasonResults);
##print("resA1:", resA1);
##print("resA2:", resA2);

#print(soccerSeasonResults[4]);

##for i in range(len(array[])):
##    print(str(array[0]));
##array2t = [];
##for i in range(len(soccer_seasons)):
##    x = i;
##    x_2 = i * 2;
##    x_3 = int(i*4/3)
##
##    array2t.insert(i, [x, x_2, x_3]); 
##    print(array2t[i]);

##def process_seasons_2(seasons):
##    z = 0;
##    resA1 = [];
##    results2 = [];
##    for i in range(len(soccer_seasons)):
##        games = 0;
##        points = 0;
##        loss = 0;
##        tie = 0;
##        win = 0;
##        season = i + 1;
##        games, points = soccer_seasons[i];
##        array = [];
##        for i in range(games):
##            if(games != 0):
##                win = int(points/3);
##            games = games - 1;

#soccerSeasonResults = process_seasons_2(soccer_seasons);
