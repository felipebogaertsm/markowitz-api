from polygon import RESTClient


def fetch_historical_data(
    ticker: str, from_date: str, to_date: str
) -> list[dict]:
    """
    Fetches historical stock data for a given ticker within a specified date
    range using Polygon API.

    Args:
    ticker (str): The stock ticker symbol (e.g., "AAPL" for Apple Inc.).
    from_date (str): The start date for the data in "YYYY-MM-DD" format.
    to_date (str): The end date for the data in "YYYY-MM-DD" format.

    Returns:
    list[dict]: A list of dictionaries containing the historical data for
        each day within the specified range.
    """
    key = "YOUR_POLYGON_API_KEY"  # Replace with your actual API key

    with RESTClient(key) as client:
        response = client.stocks_equities_aggregates(
            ticker, 1, "day", from_date, to_date, unadjusted=False
        )
        return response.results
