# Rasterisation implementation walkthrough

1. **Choose the output contract.** Thin display lines, every touched cell and anti-aliased intensities are different outputs; separate functions prevent accidental substitution.
2. **DDA.** Sample along the dominant axis using equal increments in x and y, round each sample to a cell and remove consecutive duplicates.
3. **Bresenham.** Track the error between the ideal line and selected raster path. Conditional error updates handle all octants without floating-point stepping.
4. **Wu.** Split display intensity between adjacent pixels according to the fractional line position; transpose steep lines and treat endpoints separately.
5. **Supercover.** Advance to the next grid boundary. At exact corner crossings include both side cells and the diagonal cell under the closed-cell convention.
6. **Scanline fill.** Intersect each row-centre with non-horizontal edges. A half-open vertical test avoids double-counting vertices; sorted crossings are paired under the even-odd rule.
7. **Validate.** Run `python -m unittest -v`. Extend with independent geometric oracles, affine-grid tests, holes and fractional coverage as separately named operations.
