def fibbonaci_dumb(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibbonaci_dumb(n-2) + fibbonaci_dumb(n-1)


def fib_with_DP(n: int, memo: [int]) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    if memo[n] != 0:
        return memo[n]
    memo[n] = fibbonaci_dumb(n-2) + fibbonaci_dumb(n-1)
    return memo[n]