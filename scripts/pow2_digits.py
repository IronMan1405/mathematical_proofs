"""Search for n such that 2^n avoids the decimal digits {1,2,4,8}.

Method 1 (direct): compute 2^n exactly and inspect every digit, 0 <= n <= N1.
Method 2 (sieve + exact): track 2^n mod 10^K incrementally; only exponents whose
  last K digits avoid the forbidden set get a full exact check. Every exponent in
  0..N2 is either rejected by a genuine forbidden trailing digit or fully checked.
The two methods are compared on their common range.
"""
import sys
import time

FORBIDDEN = set("1248")
sys.set_int_max_str_digits(0)  # allow str() of huge ints (Python >= 3.11)


def ok(s: str) -> bool:
    return not (FORBIDDEN & set(s))


def direct(N):
    hits, x = [], 1
    for n in range(N + 1):
        if ok(str(x)):
            hits.append(n)
        x <<= 1
    return hits


def sieved(N, K=40):
    mod = 10 ** K
    hits, survivors, r = [], 0, 1
    for n in range(N + 1):
        # r == 2^n mod 10^K. If 2^n >= 10^K, str(r).zfill(K) is exactly its last K digits;
        # otherwise 2^n == r and the zero-padding adds only harmless 0s, so we full-check anyway.
        if ok(str(r)):
            survivors += 1
            if ok(str(pow(2, n))):  # exact, complete decimal representation
                hits.append(n)
        r = (r << 1) % mod
    return hits, survivors


if __name__ == "__main__":
    N1 = int(sys.argv[1]) if len(sys.argv) > 1 else 20_000
    N2 = int(sys.argv[2]) if len(sys.argv) > 2 else 2_000_000
    t = time.time()
    d = direct(N1)
    print(f"direct: n in [0,{N1}] ({N1+1} exponents): hits {d}  [{time.time()-t:.1f}s]")
    t = time.time()
    s, surv = sieved(N2)
    print(f"sieve:  n in [0,{N2}] ({N2+1} exponents): {surv} needed full check; hits {s}  [{time.time()-t:.1f}s]")
    assert [n for n in s if n <= N1] == d, "methods disagree"
    assert all(ok(str(2 ** n)) for n in s)
    print("cross-check passed; 2^16 =", 2 ** 16)
