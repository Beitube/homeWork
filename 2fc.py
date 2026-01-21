colours = []
n = int(input())
for _ in range(n):
    colours.append(input())
n = int(input())
for i in range(n):
    print(colours[i % len(colours)])
