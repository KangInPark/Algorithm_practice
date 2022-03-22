def func(x):
    if x == 1:
        return memo[x]
    if x % 2 == 0:
        if x / 2 in memo:
            memo[x] = (memo[x / 2] * memo[x / 2]) % c
        else:
            memo[x] = (func(x / 2) * func(x / 2)) % c
        return memo[x]
    else:
        if x - 1 in memo:
            memo[x] = (memo[x - 1] * a) % c
        else:
            memo[x] = (func(x - 1) * a) % c
        return memo[x]


a, b, c = map(int, input().split(" "))
memo = {}
memo[1] = a % c
print(func(b))
