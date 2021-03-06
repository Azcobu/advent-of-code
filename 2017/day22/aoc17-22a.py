#AoC 2017 - Day 22a

def load_data():
    grid = set()
    with open('input.txt', 'r') as infile:
        for rownum, row in enumerate(infile.read().splitlines()):
            for colnum, char in enumerate(row):
                if char == '#':
                    grid.add((colnum, rownum))
    return grid

def move(x, y, curr_dir):
    moves = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    return (x + moves[curr_dir][0], y + moves[curr_dir][1])

def count_infections(grid):
    curr_dir, infs = 0, 0
    moves = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    x = round(max([k[0] for k in grid])/2)
    y = round(max([k[1] for k in grid])/2)

    for burst in range(10000):
        turn_dir = 1 if (x, y) in grid else -1
        curr_dir = (curr_dir + turn_dir) % 4

        if (x, y) in grid:
            grid.remove((x, y))
        else:
            grid.add((x, y))
            infs += 1

        x, y = (x + moves[curr_dir][0], y + moves[curr_dir][1])

    return infs

def main():
    print(count_infections(load_data()))

if __name__ == '__main__':
    main()
