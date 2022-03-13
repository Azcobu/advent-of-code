# AoC 2017 - Day 5a

def load_data():
    with open('input.txt', 'r') as infile:
        return [int(x.strip()) for x in infile.readlines()]

def calc_exit(instrs):
    pos, steps = 0, 0
    while pos < len(instrs):
        oldpos = pos
        pos += instrs[pos]
        instrs[oldpos] += 1
        steps += 1
    return steps

def main():
    print(calc_exit(load_data()))

if __name__ == '__main__':
    main()
