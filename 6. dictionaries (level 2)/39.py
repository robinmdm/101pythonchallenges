my_dict = {
	"a": 4,
	"b": 4,
	"c": 2,
	"d": 7,
	"e": 4,
	"f": 2,
	"g": 7,
	"h": 7
 }


key_li = list(my_dict.keys())
value_li = list(my_dict.values())

frequency_dict = {}

for i in value_li:
    if i not in frequency_dict:
        frequency_dict[i] = 1
    else:
        frequency_dict[i] = frequency_dict[i] + 1

print(frequency_dict)