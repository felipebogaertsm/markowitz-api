from rest_framework import serializers


class PortfolioOptimizationSerializer(serializers.Serializer):
    tickers = serializers.CharField(
        help_text="Enter comma-separated ticker symbols."
    )
    target_return = serializers.FloatField()
