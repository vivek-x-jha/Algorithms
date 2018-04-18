from tools import power


def fib(n):
    """finds nth fibonacci number in logarithmic time"""

    goldenRatio = (1 + 5 ** 0.5) / 2
    sequence = 0, 1, 1
    try:
        return sequence[n]
    except IndexError:
        binetApprox = power(goldenRatio, n) / (5 ** 0.5)
        if n % 2 == 0:
            return int(binetApprox)
        return int(binetApprox + 1)


def main():
    for k in range(30):
        print(f'Fibonacci {k}: {fib(k)}')


if __name__ == '__main__':
    main()
