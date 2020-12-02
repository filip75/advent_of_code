from typing import Dict, List, Optional


class Point:
    def __init__(
        self,
        name: str,
        orbitee: Optional["Point"] = None,
        orbiters: Optional[List["Point"]] = None,
    ):
        self.orbiters = orbiters[:] if orbiters else []
        self.orbitee = orbitee
        self.name = name


def add_orbit(points: Dict[str, Point], orbitee: str, orbiter: str) -> None:
    orbitee_object = points.get(orbitee, None)
    if orbitee_object is None:
        orbitee_object = Point(orbitee)
        points[orbitee] = orbitee_object

    orbiter_object = points.get(orbiter, None)
    if orbiter_object is None:
        orbiter_object = Point(orbiter)
        points[orbiter] = orbiter_object

    orbiter_object.orbitee = orbitee_object
    orbitee_object.orbiters.append(orbiter_object)


def count_orbits(points: Dict[str, Point]) -> int:
    to_visit = [(x, 1) for x in points["COM"].orbiters]
    number_of_orbits = len(to_visit)
    while to_visit:
        current = to_visit.pop()
        to_visit.extend([(x, current[1] + 1) for x in current[0].orbiters])
        number_of_orbits += len(current[0].orbiters) * (current[1] + 1)
    return number_of_orbits


def count_transfers(start_point: Point, end_point: Point) -> int:
    path1 = []
    point = start_point
    while point.orbitee:
        path1.append(point.orbitee)
        point = point.orbitee

    path2 = []
    point = end_point
    while point.orbitee:
        path2.append(point.orbitee)
        point = point.orbitee

    for i, p1 in enumerate(path1):
        for j, p2 in enumerate(path2):
            if p1 is p2:
                return i + j
    return -1


with open("input.txt") as file:
    p = {}
    for line in file:
        add_orbit(p, *line.strip().split(")"))
    print(count_orbits(p))
    print(count_transfers(p["SAN"], p["YOU"]))
