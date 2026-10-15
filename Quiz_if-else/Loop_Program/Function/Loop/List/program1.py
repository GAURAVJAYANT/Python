list = [1,2,3,4,5]
print(list[0])
print(list[4])

numbers = [10, 20, 30, 40]
numbers.append(70)
print(numbers)

numbers1 = [10, 20, 30, 40, 50]
numbers1.remove(30)
print(numbers1)

numbers2 = [5, 10, 15, 20, 25]

for x in numbers2:
    print(x)


numbers3 = [10, 20, 30, 40, 50]
sum=0
for x in numbers3:
    sum=sum+x

print(sum)

numbers4 = [10, 20, 30, 20, 40, 20]
print(numbers4.count(20))

numbers6 = [50, 10, 40, 20, 30]
numbers6.sort()
print(numbers6)

numbers = [10, 20, 30, 40, 50]
numbers.reverse()
print(numbers)

numbers = [10, 20, 30, 40, 50]
if 30 in numbers:
    print("found")
else:
    print("not")
