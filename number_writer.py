import json

number = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as file_obj:
	json.dump(number, file_obj)