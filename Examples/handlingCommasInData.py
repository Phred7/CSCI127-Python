

playData = open("broadway.csv", "r")

name = input("Give play?")

for i in playData:
    x = i.split(',')
    if x[7][0] == '"':
       name = x[7] + x[8]
       x[7] = name
       x.remove(x[8])
       
playData.close()


