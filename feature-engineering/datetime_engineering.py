import pandas as pd
from typing import Callable

def convert_datetime(df, Timestamp):
    df[Timestamp] = pd.to_datetime(df[Timestamp], infer_datetime_format=True)
    return df
    #"%Y %m %d %I:%M%p"
    
    """
    Convert the specified feature to a datetime object and return modified dataframe.

    Args:
        df (pd.DataFrame): The input DataFrame containing the feature to be converted.
        feature (str): The name of the feature to be converted.

    Returns:
        pd.DataFrame: The DataFrame with the specified feature converted to datetime.
    """

    # TODO: Implement this function
    pass

def create_month(df, feature, name):
    df[name] = pd.DatetimeIndex(df[feature]).month
    return df
    """
    Convert a "month" feature from the specified datetime feature and return modified dataframe.

    Args:
        df (pd.DataFrame): The input DataFrame containing the datetime feature.
        feature (str): The name of the datetime feature.
        name (str): The name of new "month" feature to be created.

    Returns:
        pd.DataFrame: The DataFrame including the "month" feature.
    """

    # TODO: Implement this function
    pass

def aggregate_months(df, group, agg_func):
    new_df = df.groupby(group).agg(agg_func)
    return new_df
    """
    Perform aggregation function on dataframe based on grouping feature.

    Args:
        df (pd.DataFrame): The input DataFrame containing features to be aggregated.
        group (str): The name of the feature by which to group.
        agg_func (str): The name of the aggregating function.

    Returns:
        pd.DataFrame: The aggregated dataframe.
    """

    # TODO: Implement this function
