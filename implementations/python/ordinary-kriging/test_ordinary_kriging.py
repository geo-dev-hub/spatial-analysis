import numpy as np
import pytest
from pykrige.ok import OrdinaryKriging


@pytest.fixture
def sample():
    return (
        np.array([0.3, 1.9, 1.1, 3.3, 4.7]),
        np.array([1.2, 0.6, 3.2, 4.4, 3.8]),
        np.array([0.47, 0.56, 0.74, 1.47, 1.74]),
    )


def test_point_prediction_and_variance_are_finite(sample):
    x, y, z = sample
    model = OrdinaryKriging(x, y, z, variogram_model="spherical",
                            verbose=False, enable_plotting=False)
    prediction, variance = model.execute("points", np.array([2.0]), np.array([2.0]))
    assert np.isfinite(float(prediction[0]))
    assert np.isfinite(float(variance[0]))
    assert float(variance[0]) >= -1e-10


def test_grid_prediction_shapes_match_grid(sample):
    x, y, z = sample
    model = OrdinaryKriging(x, y, z, variogram_model="exponential",
                            verbose=False, enable_plotting=False)
    prediction, variance = model.execute(
        "grid", np.array([0.0, 1.0, 2.0]), np.array([0.0, 1.0])
    )
    assert prediction.shape == (2, 3)
    assert variance.shape == (2, 3)
    assert np.isfinite(np.asarray(prediction)).all()
    assert np.isfinite(np.asarray(variance)).all()


def test_zero_nugget_reproduces_sampled_values(sample):
    x, y, z = sample
    model = OrdinaryKriging(
        x, y, z,
        variogram_model="spherical",
        variogram_parameters={"sill": 1.0, "range": 5.0, "nugget": 0.0},
        exact_values=True,
        verbose=False,
        enable_plotting=False,
    )
    prediction, _ = model.execute("points", x, y)
    assert np.asarray(prediction) == pytest.approx(z, abs=1e-6)
