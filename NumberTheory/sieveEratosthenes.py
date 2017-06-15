def primes_sieve2(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False
    for (i, isprime) in enumerate(a):
        print ('i: {} and isprime: {}'.format(i, isprime))
        if isprime:
            yield i
            # print(i)
            for n in range(i*i, limit, i):     # Mark factors non-prime
                a[n] = False

a=primes_sieve2(25)
for i in a:
    print(i)
