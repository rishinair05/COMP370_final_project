import pandas as pd
import re

df = pd.read_csv('data/processed/topic1_for_subcategorization.csv')

# Better categorization with clearer boundaries
expected = []
actual_reports = []  # Weekend recaps, daily numbers, cumulative totals
actual_analysis = []  # Comparisons, milestones, drops, trends
geographic_focus = []  # International/overseas specific
other = []

for idx, row in df.iterrows():
    title = str(row['title']).lower()
    text = str(row['selftext']).lower()[:1000]
    combined = title + ' ' + text
    
    # Expected/Predicted
    if any(kw in combined for kw in ['forecast', 'predict', 'projection', 'tracking', 'presale', 
                                      'will it', 'could it', 'might', 'expected to', 'projected',
                                      'predicted', 'forecasted']):
        expected.append(idx)
        continue
    
    # Geographic focus (international/overseas specific discussions)
    if any(kw in combined for kw in ['overseas', 'international', 'foreign', 'china', 'uk', 
                                      'europe', 'japan', 'korea']) and 'domestic' not in combined[:300]:
        geographic_focus.append(idx)
        continue
    
    # Actual Reports (weekend recaps, daily numbers, cumulative totals)
    if any(kw in combined for kw in ['recap', 'weekend', 'friday', 'saturday', 'sunday', 
                                      'daily', 'total', 'cumulative', 'stands at', 'amassed']):
        actual_reports.append(idx)
        continue
    
    # Actual Analysis (comparisons, milestones, drops, trends)
    if any(kw in combined for kw in ['vs', 'versus', 'compared', 'comparison', 'behind', 
                                      'ahead', 'crossed', 'reached', 'hits', 'passes', 
                                      'milestone', 'record', 'drop', 'decline', 'fell', 
                                      'down', 'decrease', 'trend', 'pattern']):
        actual_analysis.append(idx)
        continue
    
    # Default: if it has box office numbers, it's a report
    if any(kw in combined for kw in ['box office', 'gross', 'million', 'billion', 'earned', 'made']):
        actual_reports.append(idx)
    else:
        other.append(idx)

print("=" * 70)
print("BETTER SUBDIVISION SUGGESTIONS FOR TOPIC 1")
print("=" * 70)
print()
print("Option 1: Simple 2-way split")
print("-" * 70)
print(f"  1a. Expected/Predicted Box Office: {len(expected)} posts")
print(f"  1b. Actual Box Office (all types): {len(actual_reports) + len(actual_analysis) + len(geographic_focus)} posts")
print()
print("Option 2: 3-way split (RECOMMENDED)")
print("-" * 70)
print(f"  1a. Expected/Predicted Box Office: {len(expected)} posts")
print(f"  1b. Actual Box Office - Reports (weekend recaps, daily numbers, totals): {len(actual_reports)} posts")
print(f"  1c. Actual Box Office - Analysis (comparisons, milestones, trends, drops): {len(actual_analysis)} posts")
print()
print("Option 3: 4-way split")
print("-" * 70)
print(f"  1a. Expected/Predicted Box Office: {len(expected)} posts")
print(f"  1b. Actual Box Office - Reports: {len(actual_reports)} posts")
print(f"  1c. Actual Box Office - Analysis: {len(actual_analysis)} posts")
print(f"  1d. Actual Box Office - International/Overseas Focus: {len(geographic_focus)} posts")
print()
print("Option 4: Geographic split")
print("-" * 70)
print(f"  1a. Expected/Predicted Box Office: {len(expected)} posts")
print(f"  1b. Domestic Box Office: {len([i for i in range(len(df)) if i not in expected and i not in geographic_focus])} posts")
print(f"  1c. International/Overseas Box Office: {len(geographic_focus)} posts")
print()
print("=" * 70)
print("RECOMMENDATION: Option 2 (3-way split)")
print("=" * 70)
print("This gives you:")
print(f"  - Balanced categories ({len(expected)}, {len(actual_reports)}, {len(actual_analysis)} posts)")
print("  - Clear distinction between reports (factual numbers) and analysis (interpretation)")
print("  - Expected vs Actual is still clear")
print()
print("Other posts not categorized: {len(other)}")


