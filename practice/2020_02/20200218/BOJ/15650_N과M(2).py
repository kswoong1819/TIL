N, M = map(int, input().split())

check = [False] * (N + 1)
a = [0] * M


def go(index, start, n, m):
    if index == m:
        for i in range(m):
            print(a[i], end=' ')
        print()
        return
    for i in range(start, n + 1):
        if check[i]:
            continue
        check[i] = True
        a[index] = i
        go(index + 1, i + 1, n, m)
        check[i] = False


go(0, 1, N, M)
