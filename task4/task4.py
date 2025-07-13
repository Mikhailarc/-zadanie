import sys

num = sys.argv[1]

def get_min_count(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        nums = [int(line.strip()) for line in f]
    
    mean = int(sum(nums) / len(nums))
    count = 0

    for a in nums:
        while a != mean:
            if a > mean:
                a -= 1
                count += 1
            elif a < mean:
                a += 1
                count +=1

    return count

print(get_min_count(num))
