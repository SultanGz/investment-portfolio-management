"""Small, pure-Python helpers for portfolio return calculations."""

from __future__ import annotations


def simple_returns(prices: list[float]) -> list[float]:
    """Calculate period-over-period simple returns from a price series.

    Args:
        prices: A non-empty sequence of prices in chronological order.

    Returns:
        A list of simple returns, one shorter than the input.

    Raises:
        ValueError: If fewer than two prices are provided.
    """
    if len(prices) < 2:
        raise ValueError("At least two prices are required to compute returns.")
    return [(prices[i] - prices[i - 1]) / prices[i - 1] for i in range(1, len(prices))]


def cumulative_return(prices: list[float]) -> float:
    """Calculate total cumulative return from the first to the last price.

    Args:
        prices: A non-empty sequence of prices in chronological order.

    Returns:
        The cumulative return as a fraction, e.g. 0.21 for a 21% gain.

    Raises:
        ValueError: If fewer than two prices are provided.
    """
    if len(prices) < 2:
        raise ValueError("At least two prices are required to compute cumulative return.")
    return (prices[-1] - prices[0]) / prices[0]
