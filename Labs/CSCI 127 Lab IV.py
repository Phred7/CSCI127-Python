# --------------------------------------
# CSCI 127, Lab 4
# September 25, 2018
# Walker Ward
# --------------------------------------

def process_season(season, games_played, points_earned):
    print("");
    print("Season: " + str(season) + ", Games Played: " + str(games_played) +
          ", Points earned: " + str(points_earned));
    print("Possible Win-Tie-Loss Records");
    print("-----------------------------");

# --------------------------------------

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
                        if(loss >= 0 and win >= 0 and tie >= 0):
                            array.insert(x, [win, tie, loss]);
                if(x < 4 and games < 11):
                    win = int(points/3) - x;
                    tie = points%3 + (3*x);
                    loss = games - (win+tie);
                    if(loss >= 0 and win >= 0 and tie >= 0):
                        array.insert(x, [win, tie, loss]);
            resA1.insert(i, [array]);
    return resA1;


# --------------------------------------

def main():
    soccer_seasons = [[1, 3], [1, 1], [1, 0], [2, 3], [2, 4], [10, 15], [10, 16], [10, 17], [20, 30]];
    resA4 = process_seasons(soccer_seasons);
    resA5 = [];
    resA6 = [];
    resA7 = [];
    w = 0;
    t = 0;
    l = 0;
    for i in range(len(resA4)):
        games, points = soccer_seasons[i];
        seasonNum = i + 1;
        process_season(seasonNum, games, points);
        if(games == 1):
            resA5 = resA4[i];
            resA6 = resA5[0];
            w = resA6[0];
            t = resA6[1];
            l = resA6[2];
            print(str(w)+"-"+str(t)+"-"+str(l));
        elif(points < 6):
            resA5 = resA4[i];
            resA6 = resA5[0];
            resA7 = resA6[0];
            w = resA7[0];
            t = resA7[1];
            l = resA7[2]; 
            print(str(w)+"-"+str(t)+"-"+str(l)); 
        else:
            resA5 = resA4[i];
            resA6 = resA5[0];
            for x in range(len(resA6)):
                resA7 = resA6[x];
                w = resA7[0];
                t = resA7[1];
                l = resA7[2];
                print(str(w)+"-"+str(t)+"-"+str(l));

# --------------------------------------

main()


