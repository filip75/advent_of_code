with open("2.input") as file:
    passwords = []
    for line in file.readlines():
        line = line.strip()
        numbers = line.split(" ")[0]
        letter = line.split(" ")[1][0]
        password = line.split(":")[1][1:]
        passwords.append(
            {
                "letter": letter,
                "password": password,
                "min": int(numbers.split("-")[0]),
                "max": int(numbers.split("-")[1]),
            }
        )

valid = 0
for entry in passwords:
    if entry["min"] <= list(entry["password"]).count(entry["letter"]) <= entry["max"]:
        valid += 1
print(valid)


valid2 = 0
for entry in passwords:
    first = entry["letter"] == entry["password"][entry["min"] - 1]
    second = entry["letter"] == entry["password"][entry["max"] - 1]
    if first != second:
        valid2 += 1
print(valid2)
