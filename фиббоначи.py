def sumfibonacci(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return sumfibonacci(n - 2) + sumfibonacci(n - 1)

print(sumfibonacci(8))