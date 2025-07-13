#n, m = map(int, input().split())
import sys
n = int(sys.argv[1])
m = int(sys.argv[2])

def next_elem(i):
    elem = 1 + (i + m - 2) % n
    return elem


i = 1
while True:
    print(i, end='')
    i = next_elem(i)
    if i == 1:
        break
