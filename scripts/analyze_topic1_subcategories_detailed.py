import pandas as pd
import re

df = pd.read_csv('data/processed/topic1_for_subcategorization.csv')

# Categorize posts
categories = {
    'expected': [],
    'weekend_recap': [],
    'daily_numbers': [],
    'cumulative_total': [],
    'international': [],
    'domestic': [],
    'comparison': [],
    'milestone': [],
    'drop_decline': [],
    'other': []
}

for idx, row in df.iterrows():
    title = str(row['title']).lower()
    text = str(row['selftext']).lower()[:1000]
    combined = title + ' ' + text
    
    # Expected box office
    if any(kw in combined for kw in ['forecast', 'predict', 'projection', 'tracking', 'presale', 
                                      'will it', 'could it', 'might', 'expected to', 'projected']):
        categories['expected'].append(idx)
        continue
    
    # Weekend recap
    if 'recap' in combined or ('weekend' in title and 'box office' in combined):
        categories['weekend_recap'].append(idx)
        continue
    
    # Daily numbers
    if any(kw in combined for kw in ['friday', 'saturday', 'sunday', 'monday', 'tuesday', 
                                      'wednesday', 'thursday', 'daily']):
        categories['daily_numbers'].append(idx)
        continue
    
    # International/overseas focus
    if any(kw in combined for kw in ['overseas', 'international', 'foreign', 'china', 'uk', 
                                      'europe', 'japan', 'korea', 'global']):
        categories['international'].append(idx)
        continue
    
    # Domestic focus
    if 'domestic' in combined and not 'international' in combined[:500]:
        categories['domestic'].append(idx)
        continue
    
    # Comparisons
    if any(kw in combined for kw in ['vs', 'versus', 'compared', 'comparison', 'behind', 
                                      'ahead', 'versus', 'better than', 'worse than']):
        categories['comparison'].append(idx)
        continue
    
    # Milestones
    if any(kw in combined for kw in ['crossed', 'reached', 'hits', 'passes', 'surpasses', 
                                      'milestone', 'record']):
        categories['milestone'].append(idx)
        continue
    
    # Drops/declines
    if any(kw in combined for kw in ['drop', 'decline', 'fell', 'down', 'decrease', 'plunge']):
        categories['drop_decline'].append(idx)
        continue
    
    # Cumulative totals
    if any(kw in combined for kw in ['total', 'cumulative', 'stands at', 'amassed', 'grossed']):
        categories['cumulative_total'].append(idx)
        continue
    
    # Other
    categories['other'].append(idx)

print("Topic 1 Subcategory Analysis:")
print("=" * 60)
for cat, indices in categories.items():
    if indices:
        print(f"{cat.replace('_', ' ').title()}: {len(indices)} posts")

print("\n" + "=" * 60)
print("Suggested Subcategories:")
print("=" * 60)
print(f"1. Expected/Predicted Box Office: {len(categories['expected'])} posts")
print(f"2. Actual Box Office - Weekend Recaps: {len(categories['weekend_recap'])} posts")
print(f"3. Actual Box Office - Daily Numbers: {len(categories['daily_numbers'])} posts")
print(f"4. Actual Box Office - Cumulative Totals: {len(categories['cumulative_total'])} posts")
print(f"5. Actual Box Office - International/Overseas: {len(categories['international'])} posts")
print(f"6. Actual Box Office - Comparisons: {len(categories['comparison'])} posts")
print(f"7. Actual Box Office - Milestones/Records: {len(categories['milestone'])} posts")
print(f"8. Actual Box Office - Drops/Declines: {len(categories['drop_decline'])} posts")
print(f"9. Other: {len(categories['other'])} posts")

# Show some examples
print("\n" + "=" * 60)
print("Sample posts from each category:")
print("=" * 60)
for cat, indices in list(categories.items())[:5]:
    if indices:
        sample_idx = indices[0]
        sample_row = df.iloc[sample_idx]
        print(f"\n{cat.replace('_', ' ').title()}:")
        print(f"  Title: {str(sample_row['title'])[:80]}...")


