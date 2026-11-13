# Exact orientation — rational reference predicate

A small Python reference implementation of the 2D orientation sign using exact rational arithmetic.

## Install and test

```bash
python -m pip install -r implementations/python/exact-orientation/requirements.txt
python -m pytest implementations/python/exact-orientation/test_exact_orientation.py
```

## Contract

- Each point contains exactly two real coordinates.
- Integers and Fraction values are represented exactly.
- Python float values are interpreted as their exact binary floating-point values.
- The result is +1 (counter-clockwise), -1 (clockwise) or 0 (collinear).
- Non-finite and non-real coordinates are rejected.

This is a correctness-oriented reference implementation for teaching and differential testing. It is not Shewchuk's adaptive expansion arithmetic and is not intended as a high-performance geometry kernel.
