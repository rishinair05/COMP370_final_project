import pandas as pd
import re

df = pd.read_csv('data/processed/topic1_for_subcategorization.csv')

expected_keywords = ['forecast', 'predict', 'projection', 'tracking', 'presale', 'will it', 'could it', 
                     'might', 'estimate', 'expect', 'projected', 'predicted', 'forecasted', 'prediction',
                     'could make', 'will make', 'might make', 'expected to']
actual_keywords = ['earned', 'grossed', 'made', 'debuted', 'opened', 'recap', 'weekend', 'total', 
                   'reached', 'crossed', 'finished', 'closed', 'stands at', 'amassed', 'gross',
                   'million', 'billion', 'domestic', 'worldwide', 'overseas', 'international']

expected_count = 0
actual_count = 0

for _, row in df.iterrows():
    title = str(row['title']).lower()
    text = str(row['selftext']).lower()[:800]  # First 800 chars
    combined = title + ' ' + text
    
    has_expected = any(kw in combined for kw in expected_keywords)
    has_actual = any(kw in combined for kw in actual_keywords)
    
    # Check for dollar amounts which usually indicate actual numbers
    has_dollar_amounts = bool(re.search(r'\$\d+[\.\d]*[mMbBkK]', combined))
    
    # If it has dollar amounts and recap/weekend/total, it's likely actual
    if has_dollar_amounts and ('recap' in combined or 'weekend' in combined or 'total' in combined):
        actual_count += 1
    elif has_actual and not has_expected:
        actual_count += 1
    elif has_expected and not has_actual:
        expected_count += 1
    elif has_dollar_amounts:  # Dollar amounts without prediction words = actual
        actual_count += 1
    elif 'recap' in combined or 'weekend' in title.lower():  # Recaps are always actual
        actual_count += 1
    else:
        # Default to actual if it has box office related terms
        if any(word in combined for word in ['box office', 'gross', 'million', 'billion']):
            actual_count += 1
        else:
            expected_count += 1

print(f'Expected Box Office: {expected_count}')
print(f'Actual Box Office: {actual_count}')
print(f'Total: {len(df)}')


