import numpy as np
from scipy.optimize import minimize


def optimize_portfolio(
    returns: np.ndarray, risk_free_rate: float, target_return: float
) -> tuple[np.ndarray, float, float, float]:
    """
    Performs Markowitz portfolio optimization given historical returns.

    The optimization is performed in three steps:
    1. Defining constraints and bounds
    2. Optimizing portfolio
    3. Calculating statistics

    Args:
    returns (np.ndarray): A 2D array of historical returns for different
        assets.
    risk_free_rate (float): The risk-free rate of return, used in Sharpe
        ratio calculation.
    target_return (float): The target return for the optimized portfolio.

    Returns:
    tuple[np.ndarray, float, float, float]: A tuple containing the optimized
        portfolio weights, expected portfolio return, portfolio volatility,
        and Sharpe ratio.
    """

    def portfolio_statistics(weights: np.ndarray) -> tuple[float, float, float]:
        """
        Calculates portfolio statistics: return, volatility, and Sharpe ratio.

        Args:
        weights (np.ndarray): Asset weights in the portfolio.

        Returns:
        Tuple[float, float, float]: Portfolio return, volatility, and Sharpe ratio.
        """
        portfolio_return = np.sum(returns.mean() * weights) * 252
        portfolio_volatility = np.sqrt(
            np.dot(weights.T, np.dot(returns.cov() * 252, weights))
        )
        sharpe_ratio = (portfolio_return - risk_free_rate) / portfolio_volatility
        return portfolio_return, portfolio_volatility, sharpe_ratio

    num_assets = returns.shape[1]
    constraints = (
        {"type": "eq", "fun": lambda x: np.sum(x) - 1},
        {"type": "eq", "fun": lambda x: portfolio_statistics(x)[0] - target_return},
    )
    bounds = tuple((0, 1) for _ in range(num_assets))
    initial_guess = num_assets * [1.0 / num_assets]

    optimized = minimize(
        lambda x: portfolio_statistics(x)[1],
        initial_guess,
        method="SLSQP",
        bounds=bounds,
        constraints=constraints,
    )

    return optimized.x, *portfolio_statistics(optimized.x)
