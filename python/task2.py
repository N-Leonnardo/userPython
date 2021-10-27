

lowNum = 2
highNum = 9
mult = 3

for i in range(lowNum,highNum+1):
    if i%(mult) == 0:
        print(i)

i = 2018
while i>= 0:
    print (i)
    i -= 4

sum = 0

for i in range(0,500001):
    if i%2 != 0:
        sum = sum + i

print(sum)

dividB = ()
for i in range(1,101):
    if i%5 == 0:
        dividB = ("Coding")
        if i%10 == 0:
            dividB += ("Dojo")
        print(dividB)
    else:
        print(i)
for i in range(0,151):
    print (i)


for i in range(5,1000,5):
    if i%5 == 0:
        print (str(i))