try:
	with open('programming.txt','r+') as file_object:
		file_object.write("I love progarmm")
	with open('programming.txt') as file_object:
		line = file_object.read()
		print(line.split())
except FileNotFoundError:
	pass
else:
	print("write file success.")