count = 0
flag1 = "Александра"
flag2 = "Левон"
n = input()
while n != flag1:
    n = input()
n = input()    
while n != flag2:
    n = input()
    count += 1

print(count)
