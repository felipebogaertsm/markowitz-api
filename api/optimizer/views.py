import pandas as pd

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from optimizer.serializers import PortfolioOptimizationSerializer
from optimizer.services import optimize_portfolio
from optimizer.services.polygon import fetch_historical_data

RISK_FREE_RATE = 0.05


@api_view(["POST"])
def optimizer_api(request):
    """
    This is the API for the optimizer.

    """
    serializer = PortfolioOptimizationSerializer(data=request.data)
    if serializer.is_valid():
        tickers = serializer.validated_data["tickers"].split(",")
        from_date = serializer.validated_data["from_date"]
        to_date = serializer.validated_data["to_date"]
        target_return = serializer.validated_data["target_return"]

        # Fetch historical data
        historical_data = {
            ticker: fetch_historical_data(ticker, str(from_date), str(to_date))
            for ticker in tickers
        }

        # Convert historical data to a DataFrame
        data_frames = []
        for ticker, data in historical_data.items():
            df = pd.DataFrame(data)
            df.set_index(pd.to_datetime(df["timestamp"]), inplace=True)
            df[ticker] = df["close"]
            data_frames.append(df[[ticker]])

        # Combine all DataFrames
        combined_df = pd.concat(data_frames, axis=1)

        # Calculate daily returns
        returns = combined_df.pct_change().dropna()

        # Define risk-free rate
        risk_free_rate = 0.01  # This is an example value

        # Perform optimization
        (
            optimized_weights,
            expected_return,
            volatility,
            sharpe_ratio,
        ) = optimize_portfolio(returns.values, risk_free_rate, target_return)

        return Response(
            {
                "optimized_weights": optimized_weights.tolist(),  # Convert numpy array to list
                "expected_return": expected_return,
                "volatility": volatility,
                "sharpe_ratio": sharpe_ratio,
            }
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
