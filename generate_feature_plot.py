#!/usr/bin/env python3
import matplotlib.pyplot as plt
import pandas as pd
from assistant_mapping import TECHNICAL_TO_DISPLAY, DISPLAY_TO_COLOR


def create_feature_plot():
    """Create a plot based on feature scores from features.txt using shared mapping and color legend."""
    try:
        # Read the features.txt file
        df = pd.read_csv('features.txt', sep='\t')
        
        # Define base feature weights (positive = good, negative features are bad)
        # We'll normalize absolute weights so the total available points = 100
        base_feature_weights = {
            'Open Source': 8,
            'Self-hostable': 7,
            'LLM Agnostic': 6,
            'Tab Completion': 5,
            'Chat': 4,
            'Modify Files': 4,
            'Run Commands': 3,
            'Select Context': 3,
            'Backend/SDK': 3,
            'Multi-IDE': 2,
            'Data Retained': -5,   # awarded when "No"
            'Data Re-used': -8,    # awarded when "No"
            'IP Checks': 4
        }

        # Normalize to 100 total points using absolute values
        total_abs = sum(abs(w) for w in base_feature_weights.values())
        scaled = {k: abs(v) * (100.0 / total_abs) for k, v in base_feature_weights.items()}

        # Round while preserving total = 100
        items = sorted(scaled.items(), key=lambda kv: kv[1], reverse=True)
        rounded = {k: int(v) for k, v in items}
        remainder = 100 - sum(rounded.values())
        if remainder != 0:
            # Distribute remainder by fractional parts (largest fractions first)
            fractions = sorted(((k, scaled[k] - int(scaled[k])) for k, _ in items), key=lambda kv: kv[1], reverse=True)
            idx = 0
            step = 1 if remainder > 0 else -1
            while remainder != 0 and idx < len(fractions):
                k = fractions[idx][0]
                new_val = rounded[k] + step
                if new_val >= 0:
                    rounded[k] = new_val
                    remainder -= step
                idx = (idx + 1) % len(fractions)

        # Final integer weights used for scoring
        feature_weights = rounded
        
        # Calculate scores for each tool
        tool_scores = {}
        
        for _, row in df.iterrows():
            tool_name = row['Tool']
            if tool_name not in TECHNICAL_TO_DISPLAY:
                continue
            score = 0
            for feature, weight in feature_weights.items():
                if feature in row:
                    if feature in ['Data Retained', 'Data Re-used']:
                        # Award points when negative features are absent
                        if row[feature] == 'No':
                            score += weight
                    else:
                        # Award points when positive features are present
                        if row[feature] == 'Yes':
                            score += weight
            # Minimum score is zero
            score = max(score, 0)
            tool_scores[TECHNICAL_TO_DISPLAY[tool_name]] = score
        
        # Sort by score (descending)
        sorted_scores = dict(sorted(tool_scores.items(), key=lambda x: x[1], reverse=True))
        
        # Get color for each assistant
        colors = [DISPLAY_TO_COLOR[name] for name in sorted_scores.keys()]
        
        # Create the plot
        plt.figure(figsize=(14, 8))
        tools = list(sorted_scores.keys())
        scores = list(sorted_scores.values())
        bars = plt.bar(tools, scores, color=colors, alpha=0.8)
        
        # Customize the plot
        plt.title('Comparative Analysis', fontsize=16, fontweight='bold')
        plt.xlabel('')
        plt.ylabel('Feature Score', fontsize=12, fontweight='bold')
        plt.xticks(range(len(tools)), tools, rotation=45, ha='right')
        plt.grid(axis='y', alpha=0.3, linestyle='--')
        
        # Add value labels on top of bars
        for bar, score in zip(bars, scores):
            plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5, 
                    f"{score}", ha='center', va='bottom', 
                    fontweight='bold', fontsize=10)
        
        # Add legend
        legend_handles = [plt.Rectangle((0,0),1,1, color=DISPLAY_TO_COLOR[name]) for name in tools]
        plt.legend(legend_handles, tools, title="Assistant", bbox_to_anchor=(1.05, 1), loc='upper left',
                  handleheight=2.5, handlelength=3, borderaxespad=0.)
        
        # Adjust layout and save
        plt.tight_layout()
        plt.savefig('feature_scores.png', dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"Feature-based plot saved as 'feature_scores.png'")
        
        # Print the scores
        print("\nFeature-based scores:")
        for tool, score in sorted_scores.items():
            print(f"{tool}: {score}")
        
        # Print feature weights for reference
        print("\nFeature weights used:")
        for feature, weight in feature_weights.items():
            # Show sign for clarity: negative-weight features are awarded when "No"
            sign = '-' if feature in ['Data Retained', 'Data Re-used'] else '+'
            print(f"{feature}: {sign}{weight}")
        
    except Exception as e:
        print(f"Error creating feature plot: {e}")

def main():
    print("Generating feature-based scoring plot...")
    print("="*60)
    create_feature_plot()

if __name__ == "__main__":
    main() 