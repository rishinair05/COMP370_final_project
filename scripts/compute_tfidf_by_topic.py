"""
Script to compute TF-IDF scores for each topic category.
Extracts the top 10 words with highest TF-IDF scores for each topic.

Run from project root: python scripts/compute_tfidf_by_topic.py
"""
import sys
from pathlib import Path
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import re

# Add src to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from src.data_utils import get_data_path


def clean_text(text):
    """Clean and preprocess text."""
    if pd.isna(text):
        return ""
    # Convert to string
    text = str(text)
    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    # Remove markdown links
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
    # Remove extra whitespace
    text = ' '.join(text.split())
    return text


def combine_text(row):
    """Combine title and selftext into a single text field."""
    title = clean_text(row.get('title', ''))
    selftext = clean_text(row.get('selftext', ''))
    combined = f"{title} {selftext}".strip()
    return combined if combined else ""


def compute_tfidf_by_topic():
    """Compute TF-IDF scores for each topic and extract top 10 words."""
    # Load annotated data with new 8 topics structure
    print("Loading final_dataset.xlsx...")
    data_path = get_data_path('processed') / 'final_dataset.xlsx'
    df = pd.read_excel(data_path)
    
    # If Excel file doesn't have headers, assign them based on CSV structure
    if 'topic' not in df.columns and 'topics' not in df.columns:
        # Check if first column looks like IDs (strings starting with numbers/letters)
        if len(df.columns) == 10 and df.columns[0] not in ['id', 'title', 'selftext']:
            # Assign column names based on CSV structure
            df.columns = ['id', 'title', 'selftext', 'subreddit', 'created_utc', 
                         'author', 'permalink', 'url', 'score', 'topic']
            print("  Assigned column names based on CSV structure")
    
    # Check for both 'topic' and 'topics' column names
    topic_col = 'topic' if 'topic' in df.columns else 'topics'
    
    # Filter out rows with NaN topics
    df = df[df[topic_col].notna()].copy()
    
    # Convert topic column to string to handle mixed types (int and str like '1a', '1b', '1c')
    df[topic_col] = df[topic_col].astype(str)
    
    print(f"Total posts with topics: {len(df)}")
    print(f"Topic distribution:")
    # Sort by converting to string and using custom order
    topic_counts = df[topic_col].value_counts()
    topic_order = ['1a', '1b', '1c', '2', '3', '4', '5', '6']
    sorted_counts = {k: topic_counts.get(k, 0) for k in topic_order if k in topic_counts.index}
    for topic_id, count in sorted_counts.items():
        print(f"  {topic_id}: {count}")
    print()
    
    # Combine title and selftext
    print("Preprocessing text...")
    df['combined_text'] = df.apply(combine_text, axis=1)
    
    # Remove rows with empty text
    df = df[df['combined_text'].str.len() > 0].copy()
    # Reset index to ensure it matches TF-IDF matrix row positions
    df = df.reset_index(drop=True)
    print(f"Posts with non-empty text: {len(df)}")
    print()
    
    # Topic names from codebook (new 8 topics structure)
    topic_names = {
        '1a': "Box Office - Superman",
        '1b': "Box Office - Fantastic Four",
        '1c': "Box Office - Jurassic World and Other Movies",
        '2': "Audience Reception and Scores",
        '3': "Marketing, Franchise Strategy and Distribution",
        '4': "Film Quality, Creative Content and Characters",
        '5': "Fandom, Rankings and Community Meta Discussion",
        '6': "General News and Other"
    }
    
    # Compute TF-IDF across ALL documents first
    print("Computing TF-IDF scores across all documents...")
    print("=" * 80)
    
    # Create TF-IDF vectorizer for the entire corpus
    all_documents = df['combined_text'].tolist()
    vectorizer = TfidfVectorizer(
        max_features=5000,
        min_df=2,  # Word must appear in at least 2 documents
        max_df=0.95,  # Ignore words that appear in more than 95% of documents
        stop_words='english',
        ngram_range=(1, 2),  # Include unigrams and bigrams
        lowercase=True,
        strip_accents='unicode'
    )
    
    # Fit on all documents and transform
    print("Fitting TF-IDF vectorizer on all documents...")
    tfidf_matrix = vectorizer.fit_transform(all_documents)
    feature_names = vectorizer.get_feature_names_out()
    
    print(f"Vocabulary size: {len(feature_names)}")
    print()
    
    # Now compute top words for each topic
    results = {}
    
    # Sort topics in order: 1a, 1b, 1c, 2, 3, 4, 5, 6
    topic_order = ['1a', '1b', '1c', '2', '3', '4', '5', '6']
    
    for topic_id in topic_order:
        if topic_id not in df[topic_col].values:
            continue
            
        topic_name = topic_names.get(topic_id, f"Topic {topic_id}")
        topic_df = df[df[topic_col] == topic_id]
        
        if len(topic_df) == 0:
            continue
        
        print(f"\nTopic {topic_id}: {topic_name}")
        print(f"  Number of posts: {len(topic_df)}")
        
        # Get indices of documents in this topic
        topic_indices = topic_df.index.tolist()
        topic_tfidf = tfidf_matrix[topic_indices]
        
        # Calculate mean TF-IDF score for each word across all documents in this topic
        mean_scores = np.mean(topic_tfidf.toarray(), axis=0)
        
        # Get top 10 words
        top_indices = np.argsort(mean_scores)[::-1][:10]
        top_words = [(feature_names[i], mean_scores[i]) for i in top_indices]
        
        print(f"  Top 10 words by TF-IDF:")
        for rank, (word, score) in enumerate(top_words, 1):
            print(f"    {rank:2d}. {word:20s} (TF-IDF: {score:.4f})")
        
        results[topic_id] = {
            'name': topic_name,
            'count': len(topic_df),
            'top_words': top_words
        }
    
    print("\n" + "=" * 80)
    print("\nSummary:")
    print("-" * 80)
    
    # Save results to a file
    output_path = get_data_path('processed') / 'tfidf_top_words_by_topic.txt'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("Top 10 Words by TF-IDF Score for Each Topic (8 Topics Structure)\n")
        f.write("=" * 80 + "\n\n")
        
        for topic_id in topic_order:
            if topic_id not in results:
                continue
            result = results[topic_id]
            f.write(f"Topic {topic_id}: {result['name']}\n")
            f.write(f"Number of posts: {result['count']}\n")
            f.write(f"Top 10 words by TF-IDF:\n")
            
            if result['top_words']:
                for rank, (word, score) in enumerate(result['top_words'], 1):
                    f.write(f"  {rank:2d}. {word:20s} (TF-IDF: {score:.4f})\n")
            else:
                f.write("  (No words found - insufficient data)\n")
            
            f.write("\n" + "-" * 80 + "\n\n")
    
    print(f"\nResults saved to: {output_path}")
    
    # Also save as CSV for easier analysis
    csv_output_path = get_data_path('processed') / 'tfidf_top_words_by_topic.csv'
    csv_rows = []
    for topic_id in topic_order:
        if topic_id not in results:
            continue
        result = results[topic_id]
        for rank, (word, score) in enumerate(result['top_words'], 1):
            csv_rows.append({
                'topic_id': topic_id,
                'topic_name': result['name'],
                'rank': rank,
                'word': word,
                'tfidf_score': score,
                'post_count': result['count']
            })
    
    csv_df = pd.DataFrame(csv_rows)
    csv_df.to_csv(csv_output_path, index=False)
    print(f"CSV results saved to: {csv_output_path}")


if __name__ == "__main__":
    compute_tfidf_by_topic()

