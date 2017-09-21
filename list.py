bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())
print(bicycles[-1].title())
print("My first bicycle was a " + bicycles[0].title() + ".")

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
print(motorcycles)
motorcycles.insert(1,'halei')
print(motorcycles)
del motorcycles[0]
print(motorcycles)

poped_motorcycle = motorcycles.pop()
print(motorcycles)
print(poped_motorcycle)

second_motorcycle = motorcycles.pop(1)
print(motorcycles)
print(second_motorcycle)

nums = [1,2,3,4,5,6]
num = 1
nums.remove(num)
print(nums)
print(num)


nums = [2,4,3,6,8,9,5]
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)

nums = [2,1,3]
rev_nums = sorted(nums)
print(nums)
print(rev_nums)
nums.reverse()
print(nums)
print(rev_nums)
print(len(nums))