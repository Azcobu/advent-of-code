import hashlib
from collections import deque

def find_keys(salt):
    index = 0
    foundkeys = []

    hashes = deque([hashlib.md5(f'{salt}{x}'.encode('utf-8')).hexdigest() for x in range(1001)], 1001)
    while len(foundkeys) < 64:
        for pos, char in enumerate(hashes[0][:-2]):
            if char == hashes[0][pos+1] == hashes[0][pos+2]:
                for i in range(1, 1001):
                    if char*5 in hashes[i]:
                        foundkeys.append(index)
                        break
                break
        index += 1
        hashes.append(hashlib.md5(f'{salt}{index + 1000}'.encode('utf-8')).hexdigest())
    return foundkeys[63]

def main():
    print(find_keys('yjdafjpo'))

if __name__ == '__main__':
    main()
