# Intern walkthrough: potential-field derivatives

A regular grid can be represented by its 2D discrete Fourier transform. Horizontal differentiation multiplies each Fourier coefficient by i kx or i ky. The first vertical derivative of a potential field uses the radial wavenumber k=sqrt(kx^2+ky^2) under the standard spectral potential-field convention.

## Upward continuation

For a harmonic potential field, upward continuation by height h attenuates each Fourier mode by exp(-kh), where k=sqrt(kx^2+ky^2). The zero-wavenumber mean is unchanged. A periodic cosine test checks the exact attenuation of a known mode. Height and grid spacing must use the same length unit. This operator is a smoothing continuation; it does not solve the unstable downward-continuation problem.

The analytic-signal amplitude combines all three directional derivatives:
A=sqrt((dT/dx)^2+(dT/dy)^2+(dT/dz)^2).
The tilt derivative is atan2(dT/dz, sqrt((dT/dx)^2+(dT/dy)^2)).

The FFT assumes periodic boundaries. A discontinuity between opposite grid edges creates ringing, so real survey grids need suitable padding, tapering and boundary checks. The tests compare spectral derivatives against an exact periodic cosine and check attribute ranges.


## Windowed Euler deconvolution

For a chosen structural index N, the homogeneity equation is

\[(x-x_0)T_x+(y-y_0)T_y+(z-z_0)T_z=N(B-T).\]

Rearranging gives a linear system in the unknown source coordinates and base level:

\[ [T_x,T_y,T_z,N]\,[x_0,y_0,z_0,B]^T=xT_x+yT_y+zT_z+NT.\]

The implementation solves this system by least squares for one supplied window and rejects rank-deficient designs. The synthetic test constructs a field that exactly satisfies the equation and checks recovery of all four unknowns. In practice, source estimates are sensitive to structural-index choice, window size, regional-field removal, noise, multiple sources and the assumption that the field is homogeneous over the window. A low residual is not proof that the geological model is correct.
