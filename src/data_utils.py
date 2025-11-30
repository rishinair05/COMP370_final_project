"""
Utility functions for data processing.
"""
import pandas as pd
from pathlib import Path


def get_project_root():
    """Get the project root directory."""
    return Path(__file__).parent.parent


def get_data_path(subfolder=''):
    """Get path to data directory."""
    root = get_project_root()
    if subfolder:
        return root / 'data' / subfolder
    return root / 'data'


def load_reddit_posts(data_file='reddit_posts.csv', subfolder='raw'):
    """Load Reddit posts from CSV file."""
    data_path = get_data_path(subfolder) / data_file
    return pd.read_csv(data_path)


def save_dataframe(df, filename, subfolder='processed'):
    """Save dataframe to CSV in data directory."""
    data_path = get_data_path(subfolder) / filename
    df.to_csv(data_path, index=False)
    return data_path

