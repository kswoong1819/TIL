p, k = map(int, input().split(' '))
count = 0

for check in range(k, p+1):
    count += 1
print(count)