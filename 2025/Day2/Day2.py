total = 0

with open('Day2.txt') as f:
    for x in f.read().split(","):
        start = x.split("-")[0]
        end = x.split("-")[1]
        while int(start) != int(end) + 1:
            if len(start) % 2 == 0:
                fh = start[0:int((len(start)/2))]
                sh = start[int((len(start)/2)):len(start)]
                if fh == sh:
                    total += int(fh+sh)
            start = str(int(start) + 1)

print(total)