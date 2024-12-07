with open('left.txt', 'r') as lf:
    left = sorted(map(int, lf))
with open('right.txt', 'r') as rf:
    right = sorted(map(int, rf))

def part_one() -> int:
    total_dist = 0

    for lval, rval in zip(left, right):
        total_dist += abs(lval - rval)

    return total_dist

def part_two() -> int:
    return sum(x * right.count(x) for x in left)

if __name__ == "__main__":
    print(part_one())
    print(part_two())