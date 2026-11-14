import math
import pytest

from mmc_queue import mmc_metrics


def test_single_server_matches_mm1_closed_form():
    result = mmc_metrics(arrival_rate=2, service_rate=3, servers=1)
    assert result["utilisation"] == pytest.approx(2 / 3)
    assert result["probability_wait"] == pytest.approx(2 / 3)
    assert result["expected_wait"] == pytest.approx(2 / 3)
    assert result["expected_system_time"] == pytest.approx(1.0)
    assert result["expected_queue_length"] == pytest.approx(4 / 3)
    assert result["expected_system_length"] == pytest.approx(2.0)


def test_more_servers_reduce_wait_for_same_rates():
    one = mmc_metrics(4, 5, 1)
    two = mmc_metrics(4, 5, 2)
    assert two["expected_wait"] < one["expected_wait"]
    assert two["probability_wait"] < one["probability_wait"]


def test_littles_law_is_satisfied():
    result = mmc_metrics(7, 4, 2)
    assert result["expected_queue_length"] == pytest.approx(7 * result["expected_wait"])
    assert result["expected_system_length"] == pytest.approx(7 * result["expected_system_time"])


def test_near_capacity_wait_rises_sharply():
    near = mmc_metrics(9.8, 5, 2)
    moderate = mmc_metrics(7, 5, 2)
    assert near["expected_wait"] > moderate["expected_wait"]


@pytest.mark.parametrize("arrival", [0, -1, float("inf"), float("nan")])
def test_invalid_arrival_rate(arrival):
    with pytest.raises(ValueError, match="arrival_rate"):
        mmc_metrics(arrival, 5, 2)


@pytest.mark.parametrize("service", [0, -1, float("inf"), float("nan")])
def test_invalid_service_rate(service):
    with pytest.raises(ValueError, match="service_rate"):
        mmc_metrics(2, service, 2)


@pytest.mark.parametrize("servers", [0, -1, 1.5, True])
def test_invalid_server_count(servers):
    with pytest.raises(ValueError, match="servers"):
        mmc_metrics(2, 5, servers)


@pytest.mark.parametrize(("arrival", "service", "servers"), [(5, 5, 1), (11, 5, 2), (12, 4, 3)])
def test_unstable_queue_is_rejected(arrival, service, servers):
    with pytest.raises(ValueError, match="unstable"):
        mmc_metrics(arrival, service, servers)
