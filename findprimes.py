k = input("Upper limit to finding primes? ")

primes = [2]
i = 3

while i < k:
    check = True
    for prime in primes:
        if i / 2 >= prime:
            if i % float(prime) == 0:
                check = False
                break
        else:
            break
    if check:
        primes.append(i)
    i += 1

print primes
