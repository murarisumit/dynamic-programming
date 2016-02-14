from sys import stdin, stdout

def fibo(n):
    if n <=2 :
        return 1
    else:
        return (fibo(n-1) + fibo(n-2))


def fibo_topdown(n, lookup):
    if n == 0 or n == 1:
        lookup[n] = n

    if lookup[n] is None:
        lookup[n] = fibo_topdown(n-1, lookup) + fibo_topdown(n-2, lookup)
    return lookup[n]


def fibo_bottomup(n):
    fib=[0, 1]
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]

def read_input():
    name = int((stdin.readline()))


if __name__ == "__main__":
    name = int((stdin.readline()).rstrip('\n'))
    lookup = [None] * 101
    print(" Fibonacci number is ", fibo_topdown(name, lookup))
    #fibo_dyna(name)
