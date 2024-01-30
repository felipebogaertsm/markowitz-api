from datetime import datetime, timedelta


def get_yesterday_date() -> str:
    """
    Returns the date of yesterday in 'YYYY-MM-DD' format.

    Returns:
        str: A string representing yesterday's date in 'YYYY-MM-DD' format.
    """
    yesterday = datetime.now() - timedelta(days=1)
    return yesterday.strftime("%Y-%m-%d")


def get_same_date_last_year() -> str:
    """
    Returns the date of the same day in the previous year in 'YYYY-MM-DD'
    format.

    Returns:
        str: A string representing the same date in the previous year in
            'YYYY-MM-DD' format.
    """
    last_year = datetime.now() - timedelta(days=365)
    return last_year.strftime("%Y-%m-%d")
