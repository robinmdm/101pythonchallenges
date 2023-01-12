import itertools

li = [1,2,3]

new_li = list(itertools.permutations(li))

for p in new_li:
    print(list(p))