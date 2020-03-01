scores = [0, 31, 27, 31, 49, 21, 17, 25] # [msu-score-1, opponent-score-1, msu-score-2, opponent-score-2, etc.]
# The missing code goes here but write it below. Assume that every game results in either a win or a loss.
s = 0;
wins = 0;
losses = 0;

for i in range(len(scores)):
    if(s%2 == 0):
        if(scores[s] > scores[s+1]):
            wins = wins + 1;
        elif(scores[s] < scores[s+1]):
            losses = losses + 1;
    s=s+1;

print("MSU has", wins, "win(s) and", losses, "loss(es)")
            
