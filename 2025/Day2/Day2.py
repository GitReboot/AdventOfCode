total = 0

with open('Day2.txt') as f:
    for x in f.read().split(","):
        start, end = map(int, x.split("-"))
        start_len = len(str(start))
        end_len = len(str(end))

        for length in range(start_len, end_len + 1):
            if length % 2 != 0:
                continue

            half_len = length // 2
            fh = 10**(half_len - 1)
            sh = (10**half_len) - 1
            for y in range(fh, sh + 1):
                guess = y * (10**half_len) + y

                if start <= guess <= end:
                    total += guess

print(total)