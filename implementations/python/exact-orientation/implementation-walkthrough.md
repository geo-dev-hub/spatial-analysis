# Implementation walkthrough: exact orientation

## 1. Start with the determinant

The orientation of three 2D points is the sign of the determinant formed by the two vectors from the first point:

[
D=(b_x-a_x)(c_y-a_y)-(b_y-a_y)(c_x-a_x).
]

Only the sign is required. The implementation returns +1, -1 or 0.

## 2. Convert values to rational numbers

Python's Fraction can represent integers and rational values exactly. For a float, Fraction.from_float captures the exact binary floating-point value stored by Python. It does not reconstruct the decimal number a person may have intended before conversion to float.

This distinction matters for interpreting tests. Exact arithmetic can give the exact answer for the represented inputs, but cannot undo earlier measurement or storage rounding.

## 3. Evaluate without floating-point cancellation

Once coordinates are rational, subtraction and multiplication remain exact. The determinant sign therefore cannot be changed by a later floating-point rounding step.

The cost is that numerator and denominator sizes can grow, making this slower than ordinary floating-point arithmetic.

## 4. Compare with a naive determinant

One regression fixture uses large coordinate values where the ordinary floating-point determinant rounds to zero, while exact rational evaluation of those represented values has a negative sign. The example is a warning about near-degenerate inputs, not a claim that every floating-point orientation calculation fails.

## 5. Reproduce the tests

```bash
python -m pytest implementations/python/exact-orientation/test_exact_orientation.py
```

The tests cover known turn directions, large integer coordinates, rational inputs, a near-degenerate float fixture, translation invariance, sign reversal and invalid inputs.

## Scope boundary

This package implements only the 2D orientation sign. It does not implement incircle, 3D orientation, adaptive floating-point expansions, exact line intersections or a complete geometry kernel.
