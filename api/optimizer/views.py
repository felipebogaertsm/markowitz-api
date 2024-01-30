import pandas as pd

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from optimizer.serializers import PortfolioOptimizationSerializer
from optimizer.services import optimize_portfolio
from optimizer.services.polygon import fetch_close_price_for_tickers_1yr

RISK_FREE_RATE = 0.05
TARGET_RETURN = 0.1


@api_view(["GET"])
def optimizer_api(request):
    """
    API view for the optimizer.
    """
    serializer = PortfolioOptimizationSerializer(data=request.query_params)

    if serializer.is_valid():
        tickers = serializer.validated_data["tickers"].split(",")
        target_return = serializer.validated_data["target_return"]

        # Fetch historical data
        historical_data = fetch_close_price_for_tickers_1yr(tickers=tickers)

        # Calculate daily returns
        historical_data.set_index("timestamp", inplace=True)
        returns = (
            historical_data.pivot(columns="ticker")["close"]
            .pct_change()
            .dropna()
        )

        # Perform optimization
        (
            optimized_weights,
            expected_return,
            volatility,
            sharpe_ratio,
        ) = optimize_portfolio(returns.values, RISK_FREE_RATE, target_return)

        return Response(
            {
                "optimized_weights": optimized_weights.tolist(),  # Convert numpy array to list
                "expected_return": expected_return,
                "volatility": volatility,
                "sharpe_ratio": sharpe_ratio,
            }
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
