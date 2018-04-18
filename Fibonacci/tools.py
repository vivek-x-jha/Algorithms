def power(a, n, mod=10 ** 9 + 7):
    """Performs exponentiation in O(log n) time and accounts for overflow"""
    
    if n == 1:
        return a
    elif n % 2 == 0:
        return (power(a, n / 2) ** 2) % mod
    else:
        return ((power(a, (n - 1) / 2) ** 2) * a) % mod


def main():
    print(power(2, 3))
    print(power(0, 100))
    print(power(1, 64))
    print(power(2, 10))


if __name__ == '__main__':
    main()

