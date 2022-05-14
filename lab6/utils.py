def check(n):
    if n == 1 or n < 0 or n % 2 == 1:
        return False
    while n % 2 == 0:
        n = n // 2
    if n % 2 == 1 and n != 1:
        return False
    return True
