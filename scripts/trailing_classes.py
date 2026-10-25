"""Count residue classes of n (mod 4*5^(k-1)) for which the last k digits of 2^n avoid {1,2,4,8}.

Fact used: for n >= k, 2^n mod 10^k depends only on n mod 4*5^(k-1), because 2^n == 0 mod 2^k
and 2 has multiplicative order exactly 4*5^(k-1) mod 5^k (2 is a primitive root mod 5^k).
So a class is a set of exponents n >= k; class representatives here are taken >= BASE.
If S_k ever hit 0, that would prove no n >= k works. It does not.
"""
import sys

KMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 13
BASE = 64  # representatives n >= BASE >= KMAX
MOD = 10 ** KMAX
BAD = {1, 2, 4, 8}

P = 4  # period for k = 1
classes = [(n, pow(2, n, MOD)) for n in range(BASE, BASE + P) if pow(2, n, 10) not in BAD]
print(f"k=1  period={P}  surviving classes={len(classes)}  fraction={len(classes)/P:.4f}")
for k in range(2, KMAX + 1):
    newP = 5 * P
    step = pow(2, P, MOD)
    nxt = []
    for n0, r in classes:
        for j in range(5):
            if (r // 10 ** (k - 1)) % 10 not in BAD:
                nxt.append((n0 + j * P, r))
            r = r * step % MOD
    classes, P = nxt, newP
    print(f"k={k:<2} period={P}  surviving classes={len(classes)}  fraction={len(classes)/P:.3e}  ratio to k-1 = {len(classes)/prev if (prev:=globals().get('_p')) else float('nan'):.3f}")
    _p = len(classes)
