def read_table():
    valy = []
    with open("walls.txt", "r", encoding = "utf-8") as table:
        for line in table:
            mean = line.split("\t")
            valy.append(mean[3])
    return valy

def read_line(valy):
    value = {}
    for means in valy:
        if means in value:
            value[means] += 1
        else:
            value[means] = 1
    return value

from operator import itemgetter

def values(value):
    valuing = []
    valuing = sorted(value.items(), key =itemgetter(0))
    return valuing


walls = read_table()
lines = read_line(walls)
value = values(lines)
print(value)
