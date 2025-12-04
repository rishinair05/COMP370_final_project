"""
Script to generate representative summaries for each topic category using LLM.
Uses OpenAI API (ChatGPT) to produce summaries based on sample posts and TF-IDF words.

Run from project root: python scripts/generate_topic_summaries.py

Requires OPENAI_API_KEY environment variable or .env file with OPENAI_API_KEY
"""
import sys
from pathlib import Path
import pandas as pd
import json
import os

# Add src to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from src.data_utils import get_data_path

# Try to import openai
try:
    from openai import OpenAI
except ImportError:
    print("ERROR: openai package not installed.")
    print("Please install it with: pip install openai")
    sys.exit(1)

# Try to load from .env file
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass


def get_sample_posts(df, topic_id, n_samples=5):
    """Get sample posts from a topic category."""
    topic_df = df[df['topic'] == topic_id]
    if len(topic_df) == 0:
        return []
    
    # Sample posts
    sample_df = topic_df.sample(n=min(n_samples, len(topic_df)), random_state=42)
    
    samples = []
    for _, row in sample_df.iterrows():
        title = str(row.get('title', ''))[:200]
        selftext = str(row.get('selftext', ''))[:400]
        samples.append({
            'title': title,
            'text': selftext
        })
    return samples


def get_top_words(topic_id):
    """Get top TF-IDF words for a topic."""
    tfidf_path = get_data_path('processed') / 'tfidf_top_words_by_topic.csv'
    if not tfidf_path.exists():
        return []
    
    tfidf_df = pd.read_csv(tfidf_path)
    topic_tfidf = tfidf_df[tfidf_df['topic_id'] == topic_id].sort_values('rank')
    top_words = [(row['word'], row['tfidf_score']) for _, row in topic_tfidf.head(10).iterrows()]
    return top_words


def generate_topic_summary(topic_id, topic_name, top_words, sample_posts, client):
    """Generate a summary for a topic using ChatGPT."""
    
    # Format top words
    words_list = [f"{word} (TF-IDF: {score:.4f})" for word, score in top_words]
    words_text = "\n".join([f"  {i+1}. {w}" for i, w in enumerate(words_list)])
    
    # Format sample posts
    posts_text = ""
    for i, post in enumerate(sample_posts, 1):
        posts_text += f"\nExample {i}:\n"
        posts_text += f"Title: {post['title']}\n"
        if post['text']:
            posts_text += f"Text: {post['text'][:400]}...\n"
    
    # Create the prompt
    prompt = f"""You are analyzing a dataset of Reddit posts about movies. Based on the following information, provide a concise, representative summary (2-3 sentences) that characterizes this topic category.

Topic Category: {topic_name}
Topic ID: {topic_id}

Top 10 words with highest TF-IDF scores (words that are distinctive to this category):
{words_text}

Sample posts from this category:
{posts_text}

Please provide a 2-3 sentence summary that:
1. Describes what this topic category is about
2. Explains what makes it distinctive based on the top words
3. Captures the essence of the posts in this category

Summary:"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that analyzes and summarizes text categorization topics."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=200
        )
        
        summary = response.choices[0].message.content.strip()
        return summary
        
    except Exception as e:
        print(f"  Error generating summary: {e}")
        return f"Error: Could not generate summary - {str(e)}"


def generate_all_summaries():
    """Generate LLM summaries for all topics."""
    
    # Check for API key
    api_key = os.getenv('OPENAI_API_KEY') or os.getenv('OPENAI_KEY')
    if not api_key:
        print("ERROR: OPENAI_API_KEY or OPENAI_KEY environment variable not set.")
        print("Please set it using one of these methods:")
        print("  1. Set environment variable: export OPENAI_API_KEY='your-key-here'")
        print("  2. Create a .env file with: OPENAI_API_KEY=your-key-here")
        sys.exit(1)
    
    # Initialize OpenAI client
    client = OpenAI(api_key=api_key)
    
    # Load annotated data
    print("Loading reddit_posts_annotated_8topics.csv...")
    data_path = get_data_path('processed') / 'reddit_posts_annotated_8topics.csv'
    df = pd.read_csv(data_path)
    
    # Topic names
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
    
    print("\nGenerating summaries using ChatGPT...")
    print("=" * 80)
    
    results = {}
    topic_order = ['1a', '1b', '1c', '2', '3', '4', '5', '6']
    
    for topic_id in topic_order:
        topic_name = topic_names.get(topic_id, f"Topic {topic_id}")
        topic_df = df[df['topic'] == topic_id]
        
        if len(topic_df) == 0:
            continue
        
        # Get top words
        top_words = get_top_words(topic_id)
        
        # Get sample posts
        sample_posts = get_sample_posts(df, topic_id, n_samples=5)
        
        print(f"\nTopic {topic_id}: {topic_name}")
        print(f"  Number of posts: {len(topic_df)}")
        print(f"  Generating summary...")
        
        summary = generate_topic_summary(topic_id, topic_name, top_words, sample_posts, client)
        
        print(f"  Summary: {summary[:100]}...")
        
        results[topic_id] = {
            'topic_id': topic_id,
            'topic_name': topic_name,
            'summary': summary,
            'top_words': top_words,
            'post_count': len(topic_df)
        }
    
    print("\n" + "=" * 80)
    print("\nAll summaries generated!")
    
    # Save results to text file
    output_path = get_data_path('processed') / 'topic_summaries.txt'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("LLM-Generated Topic Summaries (8 Topics Structure)\n")
        f.write("=" * 80 + "\n\n")
        
        for topic_id in topic_order:
            if topic_id not in results:
                continue
            result = results[topic_id]
            f.write(f"Topic {topic_id}: {result['topic_name']}\n")
            f.write(f"Number of posts: {result['post_count']}\n\n")
            f.write(f"Summary:\n{result['summary']}\n\n")
            f.write("Top 10 words by TF-IDF:\n")
            for rank, (word, score) in enumerate(result['top_words'], 1):
                f.write(f"  {rank:2d}. {word:20s} (TF-IDF: {score:.4f})\n")
            f.write("\n" + "-" * 80 + "\n\n")
    
    print(f"\nResults saved to: {output_path}")
    
    # Also save as JSON
    json_output_path = get_data_path('processed') / 'topic_summaries.json'
    with open(json_output_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    print(f"JSON results saved to: {json_output_path}")
    
    # Print all summaries
    print("\n" + "=" * 80)
    print("ALL TOPIC SUMMARIES")
    print("=" * 80 + "\n")
    for topic_id in topic_order:
        if topic_id in results:
            result = results[topic_id]
            print(f"Topic {topic_id}: {result['topic_name']}")
            print(f"{result['summary']}\n")
            print("-" * 80 + "\n")


if __name__ == "__main__":
    generate_all_summaries()

