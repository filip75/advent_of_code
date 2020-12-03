fuel_sum = 0
with open("input.txt") as file:
    modules = [int(line) for line in file]
    while modules:
        module_mass = modules.pop(0)
        fuel_needed = int(module_mass / 3) - 2
        if fuel_needed > 0:
            fuel_sum += fuel_needed
            modules.append(fuel_needed)
print(fuel_sum)
