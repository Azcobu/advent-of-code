# AoC 2022 Day 10b

def load_data():
    with open('input.txt', 'r') as infile:
        return [(x[:4], int(x[5:])) if 'addx' in x else ('noop',) for x in infile.readlines()]

def track_sigstr(instrs):
    reg = [1]

    for instr in instrs:
        reg.append(reg[-1])
        if instr[0] == 'addx':
            reg.append(reg[-1] + instr[1])

    return sum([reg[p-1] * p for p in range(20, 221, 40)])

def main():
    print(track_sigstr(load_data()))

if __name__ == '__main__':
    main()
