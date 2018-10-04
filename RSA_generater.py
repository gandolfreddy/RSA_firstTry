def gcd(num_a, num_b):
    if (num_b > num_a):
        tmp = num_a
        num_a = num_b
        num_b = tmp
    
    if (num_a % num_b) == 0:
        return num_b
    else:
        return gcd(num_b, (num_a % num_b))

def rsa_generater(p, q):
    N = p * q
    FI = (p - 1) * (q - 1)
    
    E = 2
    while (gcd(FI, E) != 1):
        E += 1
    # Public key = (N ,E)

    k = 1
    while ((((FI * k) + 1) % E) != 0):
        k += 1
    D = ((FI * k) + 1) // E
    # Private key = D

    return [N, E], D


if (__name__ == "__main__"):
    public_key, private_key = rsa_generater(17, 19)
    print("Public key: {}".format(public_key))
    print("Private key: {}".format(private_key))
