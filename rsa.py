import numpy as np
from random import randint
from egcd import egcd


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


p = 46596819448382121528543993602166937859790681826228787290215278549306040186429954016289495405797367970633912738395422476766414007960033612236967483117581519241632909632385739856338602566387077652052439
q = 8912415057377793721392143562801506106552469994282571523683575110438475980455175691024188269911341280568534105901762591911340612278434650445018659361480170403453079084543443195785479314147664610073737616917231

def generate(p=p, q=q):
	n = p*q

	phi = (p-1) * (q-1)
	carm_func = np.lcm(p-1, q-1)

	while True:
		e = randint(2, carm_func)
		if np.gcd(e, carm_func) == 1: break
	d = int(modinv(e, phi))
	return (n, e, d)


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
