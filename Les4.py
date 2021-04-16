import random
n1 = int(input("введіть кількість рядків"))
n2 = int(input("введіть кількість стовпців"))
n1,n2 = 2,2
a = [[int(j) for j in range(n2)]for i in range(n1)]
for i in range(n1):
    for j in range(n2):
        a[i][j] = random.randint(-50,50)
        print(a[i][j],end = "\t")
    print()
#
# for i in range (n1):
#     print (max(a[i][:]))
b  = 1
for i in range(n1):
    for j in range(n2):
        # if a[i][j] >=0:
        b *= a[i][j]
print (b)
number = []
for i in range (6):
    number.append(random.randint(0,3))
print(number)
result = 1
for i in range (6):
    if i < 2:
        result /= number[i]
    if 2 <= i <= 3:
        result *= number[i]
    else:
        result += number[i]
print (result)



