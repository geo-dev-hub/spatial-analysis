# Intern walkthrough: Kalman filter and RTS smoother

The state-space model is x_t = F x_(t-1) + w_t and y_t = H x_t + v_t, with zero-mean Gaussian process and observation errors having covariances Q and R.

The forward pass predicts x and P, then conditions on available observation components using the innovation covariance and Kalman gain. Missing measurements skip the update but retain the prediction. The covariance update uses Joseph form for numerical stability.

The backward RTS pass uses the filtered covariance at t and predicted covariance at t+1 to calculate the smoothing gain J_t = P_(t|t) F' P_(t+1|t)^(-1). It revises each earlier filtered state using information from later observations.

Tests cover scalar and constant-velocity state models, missing observations, covariance validation and the effect of future observations. The model is linear and Gaussian; nonlinear motion requires an extended/unscented filter or another estimator.
