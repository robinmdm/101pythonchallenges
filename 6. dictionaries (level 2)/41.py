my_dict = {
	"a": [1, 2, 3],
	"b": [4, 0, -4],
	"c": [3, 5, 9],
	"d": [45, 12, 100]
}

li = list(my_dict.values())

suma = 0

new_li = []

for item in li:
    suma = sum(item)
    new_li.append(suma)

print(max(new_li))    

