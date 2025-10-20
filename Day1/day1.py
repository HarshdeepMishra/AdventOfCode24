import sys

with open(sys.argv[1], 'r') as file:
    lines = [list(map(int, line.strip().split())) for line in file.readlines()]
list1 = []
list2 = []

list1, list2 = list(map(list, zip(*lines)))


part1 = sum(abs(x1 - x2) for x1, x2 in zip(sorted(list1), sorted(list2)))
print(f"Part 1: {part1}")
part2 = "list2"
print(f"Part 2: {part2}")