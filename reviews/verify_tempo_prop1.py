"""Counterexample to Proposition 1 of TEMPO (arXiv:2605.18843), Appendix A.1.

Proposition 1 asserts <g_leak, grad V_c> <= -gamma ||grad V_c||^2 with gamma > 0
whenever Var_pi(c) > 0, i.e. the leakage-mode gradient descends the leakage cost.

The proof derives, correctly,

    S := <grad V_f, grad V_c> = sum_y pi(y)^2 (f(y) - fbar)(c(y) - cbar),     (8)

with f = exp(-0.5 c) and fbar, cbar the means under pi.  It then reads S as
Cov_Q(f, c) under the tilted law Q(y) ∝ pi(y)^2 and signs it with Chebyshev's
covariance inequality.  A covariance under Q must centre under Q.  Centring
under pi instead leaves

    S = Z * [ Cov_Q(f,c) + (E_Q f - E_pi f)(E_Q c - E_pi c) ],   Z = sum_y pi(y)^2,

and the second term is dropped.  It can outweigh the first, making S > 0.

Run:  python3 verify_tempo_prop1.py
"""
import numpy as np

def scores_inner(pi, c):
    """<grad V_f, grad V_c> computed directly from s(y) = e_y - pi. No algebra."""
    n = len(pi)
    f = np.exp(-0.5 * c)
    I = np.eye(n)
    gf = sum(pi[y] * (f[y] - pi @ f) * (I[y] - pi) for y in range(n))
    gc = sum(pi[y] * (c[y] - pi @ c) * (I[y] - pi) for y in range(n))
    return gf @ gc, gc @ gc

def eq8(pi, c):
    f = np.exp(-0.5 * c)
    return np.sum(pi**2 * (f - pi @ f) * (c - pi @ c))

def tilted(pi, c):
    w = pi**2
    Z = w.sum()
    Q = w / Z
    f = np.exp(-0.5 * c)
    cov = Q @ (f * c) - (Q @ f) * (Q @ c)
    corr = (Q @ f - pi @ f) * (Q @ c - pi @ c)
    return Z, cov, corr

def main():
    rng = np.random.default_rng(0)
    worst = max(abs(scores_inner(p, c)[0] - eq8(p, c))
                for p, c in ((rng.dirichlet(np.ones(n)), rng.integers(0, 12, n).astype(float))
                             for n in rng.integers(2, 6, 2000)))
    print(f"eq (8) reproduces the raw score computation to {worst:.1e}.  Equation (8) is correct.\n")

    c = np.array([0.0, 5.0, 39.0])
    pi = np.array([0.08, 0.82, 0.10])
    inner, gcsq = scores_inner(pi, c)
    Z, cov, corr = tilted(pi, c)

    print(f"leakage counts c   = {c}")
    print(f"policy        pi   = {pi}")
    print(f"Var_pi(c)          = {pi @ (c - pi @ c)**2:.4f}  > 0, the hypothesis of Proposition 1\n")
    print(f"Cov_Q(f, c)                        = {cov:+.6f}   negative, as Chebyshev gives")
    print(f"omitted term Z*(E_Q f - E_pi f)(E_Q c - E_pi c) = {Z * corr:+.6f}")
    print(f"Z * Cov_Q + omitted term           = {Z * (cov + corr):+.6f}")
    print(f"eq (8)                             = {eq8(pi, c):+.6f}")
    print(f"<grad V_f, grad V_c> from scores   = {inner:+.6f}\n")
    print(f"Proposition 1 requires this to be <= -gamma ||grad V_c||^2 with gamma > 0.")
    print(f"||grad V_c||^2 = {gcsq:.6f}, so the implied gamma = {-inner / gcsq:+.6f}.")
    assert inner > 0, "expected a positive inner product"
    print("\nThe inner product is positive: inequality (5) fails at this policy.")

if __name__ == "__main__":
    main()
