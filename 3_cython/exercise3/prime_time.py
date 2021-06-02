import timeit

print(timeit.timeit("""
import primes_c
primes_c.primes(1000000)""", number=10))

print(timeit.timeit("""
import primes_py
primes_py.primes(1000000)""", number=10))
