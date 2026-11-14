# Intern walkthrough: local Lucas–Kanade optical flow

For a small displacement (u,v), brightness constancy gives I_x u + I_y v + I_t = 0. One pixel supplies one equation for two unknowns, so Lucas–Kanade assumes a local window shares approximately the same flow and solves a least-squares system.

The local normal matrix is
[sum(Ix^2) sum(Ix Iy); sum(Ix Iy) sum(Iy^2)].
The right-hand side is -[sum(Ix It), sum(Iy It)].
A small determinant means the window lacks texture in two independent directions: the aperture problem. Such pixels are marked invalid rather than assigned an unstable flow.

This implementation uses a box-window average and one scale. It is suited to small motions and teaching the normal equations. Larger motion generally needs image pyramids and iterative warping; illumination change violates brightness constancy. The notebook uses a synthetic subpixel translation with periodic texture.
