current = 50
count1 = 0
count2 = 0

with open('Day1.txt') as f:
    for x in f.read().split():
        dist = int(x[1:])

        count2 += dist // 100
        rem = dist % 100

        if rem > 0:
            if x[0] == 'R':
                if current + rem >= 100:
                    count2 += 1
                current = (current + rem) % 100
            else:
                if current != 0 and rem >= current:
                    count2 += 1
                current = (current - rem) % 100

        if current == 0:
            count1 += 1

    print(count1, count2)