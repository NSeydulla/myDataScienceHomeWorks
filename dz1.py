stats = {}
with open('URLs.txt', 'r') as f:
    for line in f:
        line = line.strip().split('/')
        stats.setdefault(line[1], 1)
        stats[line[1]] += 1
for i in stats:
    print('"' + i + '"', stats[i])
