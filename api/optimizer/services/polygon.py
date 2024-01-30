from django.conf import settings

import pandas as pd
from polygon import RESTClient

from optimizer.services.date import get_same_date_last_year, get_yesterday_date

POLYGON_API_KEY = settings.POLYGON_API_KEY
SAFETY_LIMIT = 50000  # Limits response length


def polygon_client() -> RESTClient:
    """
    Returns the polygon REST client.

    Returns:
        RESTClient: The polygon REST client.
    """
    return RESTClient(api_key=POLYGON_API_KEY)


def fetch_historical_data(
    ticker: str,
    from_date: str,
    to_date: str,
    multiplier: int = 1,
    timespan: str = "day",
    limit: int = SAFETY_LIMIT,
) -> pd.DataFrame:
    """
    Fetches historical stock data for a given ticker within a specified date
    range using Polygon API and returns it as a Pandas DataFrame.

    Args:
        ticker (str): The stock ticker symbol (e.g., "AAPL" for Apple Inc.).
        from_date (str): The start date for the data in "YYYY-MM-DD" format.
        to_date (str): The end date for the data in "YYYY-MM-DD" format.
        multiplier (int): The size of the timespan multiplier.
        timespan (str): The timespan multiplier unit.
        limit (int): The maximum number of rows to fetch at a time.

    Returns:
        pd.DataFrame: A DataFrame containing the historical data for each day
                      within the specified range.
    """
    client = polygon_client()
    response = client.list_aggs(
        ticker=ticker,
        multiplier=multiplier,
        timespan=timespan,
        from_=from_date,
        to=to_date,
        limit=limit,
    )
    data = [{"timestamp": r.timestamp, "close": r.close} for r in response]
    return pd.DataFrame(data)


def fetch_close_price_for_tickers_1yr(tickers: list[str]) -> pd.DataFrame:
    """
    Fetches the close price for a list of tickers for the past year and returns
    it as a Pandas DataFrame.

    Args:
        tickers (list[str]): A list of stock tickers.

    Returns:
        pd.DataFrame: A DataFrame with closing prices for each ticker.

    Raises:
        ValueError: If the number of tickers is greater than 5.
    """
    if len(tickers) > 5:
        raise ValueError("Too many tickers. Maximum is 5.")

    dfs = []
    for ticker in tickers:
        df = fetch_historical_data(
            ticker,
            from_date=get_same_date_last_year(),
            to_date=get_yesterday_date(),
        )
        df["ticker"] = ticker
        dfs.append(df)

    return pd.concat(dfs, ignore_index=True)
