groups = []
with open("6.input") as file:
    group = []
    for line in file.readlines():
        if line == "\n":
            groups.append(group)
            group = []
        else:
            group.append(line.strip())
    groups.append(group)


counts = []
for group in groups:
    yeses = set()
    for person in group:
        for a in person:
            yeses.add(a)
    counts.append(len(yeses))
print(sum(counts))

counts2 = []
for group in groups:
    x = set(group[0]).intersection(*[set(y) for y in group[1:]])
    counts2.append(len(x))
print(sum(counts2))
