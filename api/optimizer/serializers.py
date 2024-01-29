from rest_framework import serializers


class PortfolioOptimizationSerializer(serializers.Serializer):
    tickers = serializers.CharField(help_text="Enter comma-separated ticker symbols.")
    from_date = serializers.DateField()
    to_date = serializers.DateField()
    target_return = serializers.FloatField()
