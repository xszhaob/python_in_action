magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician)
print('this is all')

# 含头不含尾
for val in range(0,10):
	print(val)

# 使用range创建数字列表
nums = list(range(0,10))
print(nums)

#  使用range创建数字列表时，指定步长
even_numbers = list(range(0,10,2))
print(even_numbers)

squares = []
for val in range(1,11):
	squares.append(val ** 2)
print(squares)


digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(min(digits))
print(max(digits))
print(sum(digits))

suqares = [val ** 2 for val in range(1,11)]
print(suqares)