from itertools import permutations

from e5.main import IntCode

with open("input.txt") as file:
    code = [int(x) for x in file.readline().split(',')]

phases = [0, 1, 2, 3, 4]
m = 0
for perm in permutations(phases, len(phases)):
    inp = 0
    ic = IntCode(code)
    for i in range(5):
        ic.reset()
        ic.run(perm[i])
        inp = ic.run(inp)
    m = max(m, inp)
print(m)

phases = [5, 6, 7, 8, 9]
m = 0
ics = [IntCode(code) for _ in range(len(phases))]
for perm in permutations(phases, len(phases)):
    for i, ic in enumerate(ics):
        ic.reset()
        ic.run(perm[i])
    inp = 0
    while True:
        out = None
        for ic in ics:
            out = ic.run(inp)
            if out is not None:
                inp = out
        if out is None:
            break
    m = max(m, inp)
print(m)
