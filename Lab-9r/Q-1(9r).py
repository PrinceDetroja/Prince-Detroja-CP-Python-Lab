def prime_factors(n, i=2):
    if n < 2:
        return []
    if n % i == 0:
        return [i] + prime_factors(n // i, i)
    return prime_factors(n, i + 1)

print("Prime factors of 84:", prime_factors(84))