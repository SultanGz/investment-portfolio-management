"""Tests for portfolio return helpers."""

import pytest

from investment_portfolio.returns import cumulative_return, simple_returns


def test_simple_returns_basic() -> None:
    prices = [100.0, 110.0, 121.0]
    assert simple_returns(prices) == [0.1, 0.1]


def test_simple_returns_insufficient_data() -> None:
    with pytest.raises(ValueError):
        simple_returns([100.0])


def test_cumulative_return() -> None:
    assert cumulative_return([100.0, 110.0, 121.0]) == pytest.approx(0.21)
