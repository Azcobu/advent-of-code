from parse import parse
import random

def load_data():
    probes = {}
    parsestr = 'pos=<{},{},{}>, r={}'
    with open('input.txt', 'r') as infile:
        for num, line in enumerate([x.strip() for x in infile.readlines()]):
            x, y, z, rad = [int(x) for x in parse(parsestr, line)]
            probes[num] = (x, y, z, rad)
    return probes

def gen_init_pop(probes, popsize):
    pop = {}
    min_x, max_x = min([x[0] for x in probes.values()]), max([x[0] for x in probes.values()])
    min_y, max_y = min([y[1] for y in probes.values()]), max([y[1] for y in probes.values()])
    min_z, max_z = min([z[2] for z in probes.values()]), max([z[2] for z in probes.values()])

    for x in range(popsize):
        pop[(random.randint(min_x, max_x), random.randint(min_y, max_y), random.randint(min_z, max_z))] = 0
    return pop

def score_point(probes, point):
    probes_in_range = 0

    for probe_num, probe_coords in probes.items():
        dist = sum([abs(point[x] - probe_coords[x]) for x in range(3)])
        if dist <= probe_coords[3]:
            probes_in_range += 1

    dist_from_origin = sum(point) # = 1/sum(point) 
    return (probes_in_range, dist_from_origin)

def find_fittest(probes, pop, nextgenpcent):
    for pop_coords, pop_score in pop.items():
        if pop_score == 0:
            pop[pop_coords] = score_point(probes, pop_coords)

    x = sorted(pop.items(), key=lambda x:(x[1][0], -x[1][1]), reverse=True)[:int(len(pop) * nextgenpcent)]
    print(f'Current high score is {x[0]}')
    return {k:v for k, v in x}
    
def find_optimal(probes, popsize):
    gencount = 0
    bestset = []

    pop = gen_init_pop(probes, popsize)
    for x in range(100):
        gencount += 1
        pop = find_fittest(probes, pop, 0.1)
        print(f'(Gen {gencount}')
        pop = breed_sets(pop, popsize, gencount)

def breed_sets(pop, popsize, gencount):
    probelist = list(pop.keys())
    while len(pop) < popsize:
        if random.random() > 0.02:
            newprobe = crossbreed(random.choice(probelist), random.choice(probelist))
        else:
            newprobe = parthenogen(random.choice(probelist), gencount)
        pop[newprobe] = 0
    return pop

def crossbreed(p1, p2):
    step = random.randint(-10, 100)
    axis = random.randint(0,3)
    return tuple([(p1[x] + p2[x]) // 2 for x in range(3)])

def parthenogen(p1, gencount):
    if gencount <20:
        step = 20000000
    elif gencount < 30:
        step = 2000000
    elif gencount < 40:
        step = 100000
    elif gencount < 50:
        step = 10000
    elif gencount < 60:
        step = 1000
    elif gencount < 70:
        step = 100
    else:
        step = 10

    new = [0, 0, 0]
    for x in range(3):
        new[x] = p1[x] + random.randint(-step, step)
    return tuple(new)

def main():
    probes = load_data()
    find_optimal(probes, 2500)

if __name__ == '__main__':
    main()
