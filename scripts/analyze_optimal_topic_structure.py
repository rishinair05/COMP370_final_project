"""
分析最合理的topic结构，确保不超过8个topics
"""
import sys
from pathlib import Path
import pandas as pd

# Add src to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from src.data_utils import get_data_path


def identify_movie(row):
    """Identify which movie a post is about."""
    title = str(row['title']).lower()
    text = str(row['selftext']).lower()[:500]
    combined = title + ' ' + text
    
    if any(kw in combined for kw in ['superman', 'james gunn', 'gunn', 'dcu', 'dc cinematic']):
        return 'Superman'
    if any(kw in combined for kw in ['jurassic', 'jurassic world', 'rebirth']):
        return 'Jurassic World'
    if any(kw in combined for kw in ['fantastic four', 'fantastic 4', 'ff4', 'first steps']):
        return 'Fantastic Four'
    if any(kw in combined for kw in ['smurf', 'smurfs']):
        return 'Smurfs'
    return 'Other'


def analyze_optimal_structure():
    """分析最合理的topic结构"""
    df = pd.read_csv(get_data_path('processed') / 'annotated_data.csv')
    df = df[df['topics'].notna()].copy()
    df['topics'] = df['topics'].astype(int)
    df['movie'] = df.apply(identify_movie, axis=1)
    
    topic_names = {
        1: "Box Office and Financial Performance",
        2: "Audience Reception and Scores",
        3: "Marketing, Franchise Strategy and Distribution",
        4: "Film Quality, Creative Content and Characters",
        5: "Fandom, Rankings and Community Meta Discussion",
        6: "General News",
        7: "Other"
    }
    
    print("=" * 80)
    print("当前Topic分布 (7个topics)")
    print("=" * 80)
    for topic_id in sorted(df['topics'].unique()):
        count = len(df[df['topics'] == topic_id])
        print(f"Topic {topic_id}: {topic_names[topic_id]:50s} - {count:4d} posts")
    print()
    
    # 分析Topic 1的电影分布
    topic1_df = df[df['topics'] == 1]
    print("Topic 1 电影分布:")
    movie_counts = topic1_df['movie'].value_counts()
    for movie in ['Superman', 'Fantastic Four', 'Jurassic World', 'Smurfs', 'Other']:
        count = movie_counts.get(movie, 0)
        if count > 0:
            print(f"  {movie:20s}: {count:4d} posts")
    print()
    
    print("=" * 80)
    print("方案分析 (目标: 不超过8个topics)")
    print("=" * 80)
    print()
    
    print("方案1: Topic 1拆成2个 (Expected vs Actual)")
    print("-" * 80)
    print("  1a. Expected/Predicted Box Office")
    print("  1b. Actual Box Office")
    print("  2-7: 保持原样")
    print("  总计: 2 + 6 = 8个topics ✓")
    print("  优点: 简单，区分预测vs实际")
    print("  缺点: 无法直接回答Question 2 (相对覆盖度)")
    print()
    
    print("方案2: Topic 1拆成3个 (按电影)")
    print("-" * 80)
    print("  1a. Box Office - Superman")
    print("  1b. Box Office - Fantastic Four")
    print("  1c. Box Office - Jurassic World + Other")
    print("  2-5: 保持原样")
    print("  6-7: 合并为 'General News and Other'")
    print("  总计: 3 + 4 + 1 = 8个topics ✓")
    print("  优点: 直接回答Question 2，Superman和Fantastic Four分开")
    print("  缺点: Jurassic World和Other合并")
    print()
    
    print("方案3: Topic 1拆成2个 (Superman vs Others)")
    print("-" * 80)
    print("  1a. Box Office - Superman")
    print("  1b. Box Office - Other Movies (Fantastic Four, Jurassic World, etc.)")
    print("  2-7: 保持原样")
    print("  总计: 2 + 6 = 8个topics ✓")
    print("  优点: 突出Superman，简单")
    print("  缺点: 其他电影混在一起，无法比较Fantastic Four vs Jurassic World")
    print()
    
    print("方案4: 不拆分Topic 1，合并小topics")
    print("-" * 80)
    print("  1. Box Office and Financial Performance (不拆分)")
    print("  2-5: 保持原样")
    print("  6-7: 合并为 'General News and Other'")
    print("  总计: 6个topics ✓")
    print("  优点: 最简单")
    print("  缺点: 无法回答Question 2 (相对覆盖度)")
    print()
    
    print("=" * 80)
    print("推荐方案: 方案2 (Topic 1拆成3个 + 合并6-7)")
    print("=" * 80)
    print()
    print("理由:")
    print("1. 正好8个topics，符合要求")
    print("2. Topic 1按电影拆分，直接回答Question 2")
    print("3. Superman (208 posts) 和 Fantastic Four (123 posts) 分开，最重要")
    print("4. Jurassic World (75 posts) 和 Other (26 posts) 合并，数量较少")
    print("5. Topic 6 (22 posts) 和 Topic 7 (8 posts) 合并，都是小类别")
    print()
    print("最终结构:")
    print("  1a. Box Office - Superman (208 posts)")
    print("  1b. Box Office - Fantastic Four (123 posts)")
    print("  1c. Box Office - Jurassic World + Other (101 posts)")
    print("  2. Audience Reception and Scores (37 posts)")
    print("  3. Marketing, Franchise Strategy and Distribution (85 posts)")
    print("  4. Film Quality, Creative Content and Characters (31 posts)")
    print("  5. Fandom, Rankings and Community Meta Discussion (49 posts)")
    print("  6. General News and Other (30 posts)")
    print("  总计: 8个topics")


if __name__ == "__main__":
    analyze_optimal_structure()

