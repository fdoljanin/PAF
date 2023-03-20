def demonstrateWrongness(N, a, diff):
    for _ in range(N):
        a += diff
    for _ in range(N):
        a -= diff

    return a


numberOfActions = [2 * 10**i for i in range(2, 5)]
for n in numberOfActions:
    print(demonstrateWrongness(n, 5, 1/3))
# preciznost pada s brojem operacija
