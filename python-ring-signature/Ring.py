import os, hashlib, random, Crypto.PublicKey.RSA, functools
from icecream import ic

class Ring:
    """RSA implementation."""
    def __init__(self, k, L: int = 1024) -> None:
        self.k = k
       
        self.l = L
        self.n = len(k)
        self.q = 1 << (L - 1)
        ic(self.n)

    def sign(self, m: str, z: int):
        """Sign a message."""
        self._permut(m)
        s = [None] * self.n
        u = random.randint(0, self.q)
        c = v = self._E(u)
        for i in [*range(z + 1, self.n), *range(z)]:
            s[i] = random.randint(0, self.q)
            k_i_e = self.k[i].e
            k_i_n = self.k[i].n
            e = self._g(s[i], k_i_e, k_i_n)
            v = self._E(v ^ e)
            if (i + 1) % self.n == 0:
                c = v
        s[z] = self._g(v ^ u, self.k[z].d, self.k[z].n)
        return [c] + s

    def verify(self, m: str, X) -> bool:
        """Verify a message."""
        self._permut(m)
        def _f(i):
            return self._g(X[i + 1], self.k[i].e, self.k[i].n)
        y = map(_f, range(len(X) - 1))
        y_list = list(y)
        def _g(x, i):
            return self._E(x ^ y_list[i])
        r = functools.reduce(_g, range(self.n), X[0])
        ic(r)
        ic(X)
        return r == X[0]

    def _permut(self, m):
        print(m)
        sah1 = hashlib.sha1( m.encode('utf-8') )
        hexdigest_ = sah1.hexdigest()
        print(hexdigest_)

        self.p = int(hexdigest_, 16)

    def _E(self, x):
        msg = "%s%s".format(x, self.p).encode('utf-8')
        return int(hashlib.sha1(msg).hexdigest(), 16)

    def _g(self, x, e, n):
        q, r = divmod(x, n)
        if ((q + 1) * n) <= ((1 << self.l) - 1):
            result = q * n + pow(r, e, n)
        else:
            result = x
        return result

#
# Main
#
size = 4
msg1, msg2 = "hello", "world!"

def _rn(_):
    return Crypto.PublicKey.RSA.generate(1024, os.urandom)

key = map(_rn, range(size))
key_list =  list(key)
r = Ring(key_list)
for i in range(size):
    s1 = r.sign(msg1, i)
    s2 = r.sign(msg2, i)
    ic(s1)
    ic(s2)
    assert ic(r.verify(msg1, s1)) and ic(r.verify(msg2, s2)) and not ic(r.verify(msg1, s2))

