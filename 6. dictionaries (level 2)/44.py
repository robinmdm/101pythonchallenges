product_info = {
	"description": "shoe",
	"price": 4.56,
	"colors": ["green", "blue", "red"]
}

get_keys = list(product_info.keys())

get_values = list(product_info.values())

# new_list = list(zip(get_keys, get_values))

new_list = [[key, value] for key, value in zip(get_keys, get_values)]

print(new_list)    
