# Curve construction implementation walkthrough

## Chaikin corner cutting
For each segment from P to Q, create Q1 = 3P/4 + Q/4 and Q2 = P/4 + 3Q/4. Repeating the operation rounds the line. Open curves retain their endpoints; closed rings wrap the final segment back to the first vertex.

## Catmull–Rom interpolation
Each span is formed from four consecutive controls. The implementation uses a knot interval proportional to the Euclidean distance raised to alpha: alpha=0 gives uniform, 0.5 centripetal and 1 chordal parameterisation. It evaluates the nested interpolation form and samples each span without duplicating shared endpoints. Linear endpoint extrapolation supplies the missing controls at the ends.

## Bezier evaluation
De Casteljau repeatedly interpolates adjacent control points at parameter t until one point remains. Sampling t from zero to one includes both endpoints and works for any control-polygon degree.

## Scope and validation
Tests check endpoint behaviour, sample counts, interpolation of Catmull–Rom controls, closed-ring wrapping, linear Bezier special cases and invalid inputs. These functions do not fit curves to noisy observations, preserve polygon topology, or perform Kalman/RTS filtering.
