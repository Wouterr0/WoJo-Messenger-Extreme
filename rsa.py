import numpy as np
from random import randint
from Crypto.Util import number


def egcd(b, n):
    (x0, x1, y0, y1) = (1, 0, 0, 1)
    while n != 0:
        (q, b, n) = (b // n, n, b % n)
        (x0, x1) = (x1, x0 - q * x1)
        (y0, y1) = (y1, y0 - q * y1)
    return (b, x0, y0)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def strtonum(msg):
    return (int.from_bytes(msg.encode(), "big"), len(msg))
def numtostr(num, length):
    return int.to_bytes(num, length, "big").decode()


def generate(p=number.getPrime(randint(660, 700)),
             q=number.getPrime(randint(660, 700))):
    n = p*q

    phi = (p-1) * (q-1)
    carm_func = np.lcm(p-1, q-1)

    while True:
        e = randint(2, carm_func)
        if np.gcd(e, carm_func) == 1: break
    d = int(modinv(e, phi))
    return (n, e, d, p, q)


def encrypt(m, e, n):
    if m > n:
        raise ValueError("m to big to encrypt with p and q")
    c = pow(m, e, n)
    return c

def decrypt(c, d, n):
    m = pow(c, d, n)
    return m



if __name__ == "__main__":
    while True:
        msg = input("msg: ")

        m, mlen = strtonum(msg)
        print(m, "<-- numberized")

        n, e, d = generate()
        c = encrypt(m, e, n)
        m = decrypt(c, d, n)
        print(str(c)[:6] + "...", "<-- encrypted")
        print(m, "<-- decrypted")
        print(numtostr(m, mlen), "<-- normalized")
