from datetime import datetime

start = int(input("Enter the range from which you want to start: "))
end = int(input("Enter the range to which you want to end: "))

def measure_time(func, *args):
    start_time = datetime.now()
    result = func(*args)
    elapsed = datetime.now() - start_time
    return result, elapsed



def simple_prime_search(x, y):
    result = []
    for i in range(x, y + 1):
        if i > 1:
            is_prime = True
            for j in range(2, i):
                if i % j == 0:
                    is_prime = False
            if is_prime:
                result.append(i)
    return result


def sieve_eratosthenes(a, b):
    if b < 2:
        return []

    is_prime = [True] * (b + 1)
    is_prime[0] = is_prime[1] = False

    for p in range(2, int(b ** 0.5) + 1):
        if is_prime[p]:
            for i in range(p * p, b + 1, p):
                is_prime[i] = False

    primes_in_range = [num for num in range(max(2, a), b + 1) if is_prime[num]]

    return primes_in_range

simple_primes, simple_time = measure_time(simple_prime_search, start, end)
sieve_primes, sieve_time = measure_time(sieve_eratosthenes, start, end)

print(f"Simple search time: {simple_time.total_seconds():.6f} seconds")
print(f"Sieve time:         {sieve_time.total_seconds():.6f} seconds")

difference = abs(simple_time - sieve_time).total_seconds()
faster = "Sieve" if sieve_time < simple_time else "Simple search"
print(f"Difference:         {difference:.6f} seconds ({faster} was faster)")

print("Same results:", simple_primes == sieve_primes)