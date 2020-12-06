import re

passports = []
with open("4.input") as file:
    passport = {}
    for line in file.readlines():
        for entry in line.strip().split(" "):
            if line == "\n":
                passports.append(passport)
                passport = {}
            else:
                key, value = entry.split(":")
                passport[key] = value

count = 0
for p in passports:
    if len(p) == 8 or (len(p) == 7 and "cid" not in p):
        count += 1
print(count)

count2 = 0
for p in passports:
    byr = p.get("byr")
    if not byr:
        continue
    if not 1920 <= int(byr) <= 2002:
        continue

    iyr = p.get("iyr")
    if not iyr:
        continue
    if not 2010 <= int(iyr) <= 2020:
        continue

    eyr = p.get("eyr")
    if not eyr:
        continue
    if not 2020 <= int(eyr) <= 2030:
        continue

    hgt = p.get("hgt")
    if not hgt:
        continue
    unit = hgt[-2:]
    if unit not in ["in", "cm"]:
        continue
    if unit == "cm" and (int(hgt[:-2]) < 150 or int(hgt[:-2]) > 210):
        continue
    if unit == "in" and (int(hgt[:-2]) < 59 or int(hgt[:-2]) > 76):
        continue
    print(hgt)

    hcl = p.get("hcl")
    if not hcl:
        continue
    if not re.match(r"^#[a-z0-9]{6}$", hcl):
        continue

    ecl = p.get("ecl")
    if not ecl:
        continue
    if not ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        continue

    pid = p.get("pid")
    if not pid:
        continue
    if not re.match(r"^[0-9]{9}$", pid):
        continue

    count2 += 1

print(count2)
