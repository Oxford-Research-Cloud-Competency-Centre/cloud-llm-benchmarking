#!/usr/bin/env python3
"""
Google Trends Data Visualization Script
Fetches data from Google Trends and creates a line plot showing search interest over time.
"""

import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, timedelta
import time
from pytrends.request import TrendReq

def fetch_google_trends_data(keywords, geo='', timeframe='today 5-y'):
    """
    Fetch Google Trends data using pytrends library with consistent scaling.
    
    Args:
        keywords (list): List of search terms
        geo (str): Geographic location (default: '' for worldwide)
        timeframe (str): Time range (default: 'today 5-y' for last 5 years)
    
    Returns:
        pd.DataFrame: Google Trends data
    """
    
    # Initialize pytrends
    pytrends = TrendReq(hl='en-US', tz=0)
    
    try:
        # Use "AI code" as a reference term since it's likely to have good data
        reference_term = "AI code"
        all_data = {}
        reference_data = None
        
        print(f"Using '{reference_term}' as reference term for consistent scaling...")
        
        # First, get the reference term data
        print(f"Fetching reference term: {reference_term}")
        pytrends.build_payload([reference_term], cat=0, timeframe=timeframe, geo=geo)
        ref_df = pytrends.interest_over_time()
        if not ref_df.empty and reference_term in ref_df.columns:
            all_data[reference_term] = ref_df[reference_term]
            reference_data = ref_df[reference_term]
            print(f"Reference term max value: {reference_data.max()}")
        
        # Then get all other terms compared to the reference
        for keyword in keywords:
            if keyword != reference_term:
                print(f"Fetching: {keyword} vs {reference_term}")
                pytrends.build_payload([keyword, reference_term], cat=0, timeframe=timeframe, geo=geo)
                comparison_df = pytrends.interest_over_time()
                
                if not comparison_df.empty and keyword in comparison_df.columns:
                    # Use the keyword data directly (Google Trends normalizes it)
                    all_data[keyword] = comparison_df[keyword]
                
                # Add a small delay between requests
                time.sleep(1)
        
        if not all_data:
            print("No data returned from Google Trends")
            return None
        
        # Combine all data into a single DataFrame
        combined_df = pd.DataFrame(all_data)
        if reference_data is not None:
            combined_df.index = reference_data.index  # Use the reference term's time index
        
        return combined_df
        
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

def create_trends_plot(df, keywords):
    """
    Create a line plot showing Google Trends data, sorted by current top trend, with visually distinct color palette and legend at upper right.
    
    Args:
        df (pd.DataFrame): DataFrame with dates and search interest values
        keywords (list): List of search terms
    """
    plt.figure(figsize=(14, 8))
    
    # Restore the original, visually distinct color palette
    color_palette = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2']
    
    # Get the most recent value for each keyword
    latest_values = {kw: df[kw].iloc[-1] for kw in keywords if kw in df.columns}
    # Sort keywords by latest value (descending)
    sorted_keywords = sorted(latest_values, key=latest_values.get, reverse=True)
    
    for i, keyword in enumerate(sorted_keywords):
        if keyword in df.columns:
            color = color_palette[i % len(color_palette)]
            plt.plot(df.index, df[keyword], label=keyword, linewidth=2.5, color=color)
    
    # Customize the plot
    plt.title('Google Trends: Search Interest Over Time (Worldwide)', 
              fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('Date', fontsize=12, fontweight='bold')
    plt.ylabel('Search Interest (0-100)', fontsize=12, fontweight='bold')
    plt.legend(fontsize=11, loc='upper left')
    plt.grid(True, alpha=0.3, linestyle='--')
    
    # Format x-axis dates
    plt.gcf().autofmt_xdate()
    
    # Set y-axis limits
    plt.ylim(0, 100)
    
    # Add some padding
    plt.tight_layout()
    
    # Save the plot
    plt.savefig('google_trends_plot.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print("Google Trends plot saved as 'google_trends_plot.png'")

def main():
    """Main function to execute the Google Trends analysis."""
    
    # Define the search terms from the URL
    keywords = [
        'vibe coding',
        'cursor ai', 
        'model context protocol',
        'github copilot',
        'AI code',
        'openai codex',
        'windsurf ai'
    ]
    
    print("Fetching Google Trends data...")
    print(f"Search terms: {', '.join(keywords)}")
    print("Geographic location: Worldwide")
    print("Time range: Last 5 years")
    print("-" * 50)
    
    # Fetch the data
    df = fetch_google_trends_data(keywords, geo='', timeframe='today 5-y')
    
    if df is None:
        print("Failed to fetch Google Trends data. Please try again later.")
        return
    
    print(f"Successfully fetched data for {len(df)} time points")
    print(f"Date range: {df.index.min().strftime('%Y-%m-%d')} to {df.index.max().strftime('%Y-%m-%d')}")
    
    # Create the plot
    create_trends_plot(df, keywords)
    
    # Display some statistics
    print("\nSearch Interest Statistics:")
    print("-" * 30)
    for keyword in keywords:
        if keyword in df.columns:
            max_interest = df[keyword].max()
            avg_interest = df[keyword].mean()
            print(f"{keyword}:")
            print(f"  Max interest: {max_interest:.1f}")
            print(f"  Average interest: {avg_interest:.1f}")

if __name__ == "__main__":
    main() 