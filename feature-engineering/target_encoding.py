from category_encoders import TargetEncoder
import pandas as pd
import numpy as np


def discretize_feature(df, feature):
    df_new = df.copy()
    df_new[feature] = df_new[feature].round().astype(int)
    return df_new

    """
    Discretizes a numerical feature in the DataFrame by rounding it to the nearest integer.

    Args:
        df (pd.DataFrame): The input DataFrame containing the feature to be discretized.
        feature (str): The name of the feature to be discretized.

    Returns:
        pd.DataFrame: The DataFrame with the specified feature discretized to integers.
    """

    # TODO: Implement this function


def target_encode(df, features_to_encode, target_col):
    target_encoder = TargetEncoder(cols=features_to_encode)
    df[features_to_encode] = target_encoder.fit_transform(df[features_to_encode], df[target_col])
    return df
    """
    Encodes categorical features in the DataFrame using target encoding based on the specified target column.

    Args:
        df (pd.DataFrame): The input DataFrame containing the features to be encoded.
        features_to_encode (list(str)): List of feature names to be target encoded.
        target_col (str): The name of the target column used for encoding.

    Returns:
        pd.DataFrame: The DataFrame with specified features target encoded.
    """

    # TODO: Implement this function
