"""
Text processing utilities for open coding and analysis.
"""
import pandas as pd


def get_opening_text(selftext, max_chars=500):
    """
    Get the opening text from selftext, limited to max_chars.
    Tries to end at sentence boundaries when possible.
    """
    if pd.isna(selftext) or selftext == '':
        return ''
    
    text = str(selftext)
    # Get first max_chars characters
    opening = text[:max_chars]
    
    # Try to end at a sentence boundary if possible
    if len(text) > max_chars:
        last_period = opening.rfind('.')
        last_newline = opening.rfind('\n')
        cutoff = max(last_period, last_newline)
        
        # Only use cutoff if we're not cutting off too much
        if cutoff > max_chars * 0.7:
            opening = opening[:cutoff + 1]
    
    return opening.strip()


def prepare_text_for_coding(title, opening_text):
    """Combine title and opening text for coding."""
    return f"{title}\n\n{opening_text}"

