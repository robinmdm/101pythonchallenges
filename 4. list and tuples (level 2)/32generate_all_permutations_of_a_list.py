import itertools

li = ['a', 'b', 'c', 'd']

new_li = list(itertools.permutations(li))
i = 1
for p in new_li:
    print(list(p), i)
    i = i + 1

print(len(p))