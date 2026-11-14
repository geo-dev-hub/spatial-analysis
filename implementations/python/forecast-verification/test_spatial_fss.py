import pytest
from spatial_fss import fractions_skill_score


def test_exact_gridpoint_match_scores_one():
    field = [[0, 1, 0], [1, 1, 0], [0, 0, 1]]
    assert fractions_skill_score(field, field, 1, 1) == 1.0


def test_displacement_receives_more_credit_at_larger_scale():
    observed = [[0]*5, [0,1,0,0,0], [0]*5]
    forecast = [[0]*5, [0,0,1,0,0], [0]*5]
    assert fractions_skill_score(observed, forecast, 1, 1) == 0.0
    assert fractions_skill_score(observed, forecast, 1, 3) > 0.0


def test_symmetry_and_bounds():
    obs = [[0,1,0], [0,0,0], [1,0,0]]
    fcst = [[0,0,1], [0,0,0], [0,1,0]]
    score = fractions_skill_score(obs, fcst, 0.5, 3)
    assert score == pytest.approx(fractions_skill_score(fcst, obs, 0.5, 3))
    assert 0 <= score <= 1


def test_edge_policies_are_explicit():
    obs = [[1,0,0,0], [0,0,0,0], [0,0,0,1], [0,0,0,0]]
    fcst = [[0,1,0,0], [0,0,0,0], [0,0,1,0], [0,0,0,0]]
    a = fractions_skill_score(obs, fcst, 1, 3, "truncate")
    b = fractions_skill_score(obs, fcst, 1, 3, "valid")
    assert a is not None and b is not None and a != b


def test_no_event_denominator_is_undefined():
    zeros = [[0,0], [0,0]]
    assert fractions_skill_score(zeros, zeros, 1) is None


@pytest.mark.parametrize("bad", [[], [[]], [[1,0],[1]], [[1,float("nan")]]])
def test_invalid_observed_grids_are_rejected(bad):
    with pytest.raises(ValueError):
        fractions_skill_score(bad, [[0,0],[0,0]], 1)


def test_invalid_shapes_threshold_window_and_edge_policy():
    grid = [[0,1],[1,0]]
    with pytest.raises(ValueError): fractions_skill_score(grid, [[0]], 1)
    with pytest.raises(ValueError): fractions_skill_score(grid, grid, float("inf"))
    with pytest.raises(ValueError): fractions_skill_score(grid, grid, 2, 2)
    with pytest.raises(ValueError): fractions_skill_score(grid, grid, 1, 3, "reflect")
    with pytest.raises(ValueError): fractions_skill_score(grid, grid, 1, 3, "valid")
