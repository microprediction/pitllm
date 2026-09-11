"""Reproduce mathematical checks in pitllm-paper-audit.html.

Python 3 standard library only. These are counterexamples to particular
claims; they do not reproduce the papers' model-training experiments.
"""
import math


def mean(xs):
    return sum(xs) / len(xs)


def softmax(xs):
    a = max(xs)
    exps = [math.exp(x - a) for x in xs]
    return [x / sum(exps) for x in exps]


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


# TEMPO, Appendix A.1: gradients with respect to output softmax logits.
c = [0.0, 1.0, 100.0]
p = [0.15, 0.83, 0.02]
f = [math.exp(-0.5 * x) for x in c]
vc, vf = dot(p, c), dot(p, f)
grad_c = [pi * (ci - vc) for pi, ci in zip(p, c)]
grad_f = [pi * (fi - vf) for pi, fi in zip(p, f)]
inner = dot(grad_c, grad_f)
updated_p = softmax([math.log(pi) + 1e-4 * gi for pi, gi in zip(p, grad_f)])
assert inner > 0
assert dot(updated_p, c) > vc
assert dot(updated_p, f) > vf
print('TEMPO gradient inner product:', inner)
print('TEMPO cost before / after:', vc, dot(updated_p, c))
print('TEMPO reward before / after:', vf, dot(updated_p, f))
print('P(12 clean samples | 1% policy leakage):', 0.99 ** 12)

# Geometry: two orthogonal readout directions, zero score covariance,
# yet the second score and drift label are known from the first score.
u = [-2.0, -1.0, 1.0, 2.0]
v = [x * x for x in u]
d = [int(x > 2) for x in v]
cov = mean([(x - mean(u)) * (y - mean(v)) for x, y in zip(u, v)])
accuracy = mean([int(int(abs(x) > 1.5) == y) for x, y in zip(u, d)])
assert dot([1, 0], [0, 1]) == 0
assert cov == 0 and accuracy == 1
print('Geometry score covariance / nonlinear accuracy:', cov, accuracy)

# Temporal Leakage in LLM Backtesting, prose after Corollary 10:
# no informative bridge (S=0), but a nonzero mean shift corrects bias.
y = [0.0, 1.0]  # Bernoulli(1/2), equally weighted.
clean, changed = 0.2, 0.5
improvement = mean([(clean - a)**2 - (changed - a)**2 for a in y])
mu_delta = changed - clean
r_clean = clean - 0.5
r_shift = mu_delta**2 + 2 * mu_delta * r_clean
assert math.isclose(improvement, 0.09)
assert math.isclose(improvement, -r_shift)
print('Bridge-free Brier improvement / R_shift:', improvement, r_shift)

# Fonseca: the displayed operational rules replace a stamp and project
# the value; they do not block a future value in the never-halting case.
def restamp_then_project(future_value, halted, epoch=0):
    stamp = epoch if halted else epoch + 1
    timestamped = (future_value, stamp)
    value = timestamped[0]
    return value  # g = identity. Adding an output stamp leaves it unchanged.

for halted in [False, True]:
    outputs = [restamp_then_project(b, halted) for b in [0, 1]]
    assert outputs == [0, 1]
    print('Fonseca future-bit dependence; halted =', halted, 'outputs =', outputs)

# This last check demonstrates the published reduction's missing gate.
# The separate undecidability argument for constant timestamps is a
# mathematical reduction described in the report, not a numerical test.
print('All counterexample checks passed.')
