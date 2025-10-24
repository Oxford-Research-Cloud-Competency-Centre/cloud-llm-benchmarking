#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np

def create_feature_weights_plot():
    """Create a plot showing the weights of different features."""
    
    # Define feature weights (positive = good, negative = bad)
    feature_weights = {
        'Open Source': 8,
        'Self-hostable': 7,
        'LLM Agnostic': 6,
        'Tab Completion': 5,
        'Chat': 4,
        'Modify Files': 4,
        'Run Commands': 3,
        'Select Context': 3,
        'Multi-IDE': 2,
        'Data Retained': -5,
        'Data Re-used': -8
    }
    
    # Sort features by absolute weight value
    sorted_features = dict(sorted(feature_weights.items(), key=lambda x: abs(x[1]), reverse=True))
    
    # Prepare data
    features = list(sorted_features.keys())
    weights = list(sorted_features.values())
    
    # Create figure
    plt.figure(figsize=(10, 6))
    
    # Create horizontal bars - all extending to the right using absolute values
    y_pos = np.arange(len(features))
    abs_weights = [abs(w) for w in weights]
    bars = plt.barh(y_pos, abs_weights, height=0.5)
    
    # Color bars based on positive/negative values
    for bar, weight in zip(bars, weights):
        if weight > 0:
            bar.set_color('#666666')
        else:
            bar.set_color('#999999')
    
    # Customize plot
    plt.title('Feature Weights', fontsize=14, pad=20)
    plt.xlabel('Weight', fontsize=12)
    
    # Set y-axis labels
    plt.yticks(y_pos, features)
    
    # Add gridlines
    plt.grid(axis='x', alpha=0.1, linestyle='-')
    
    # Add value labels after the bars
    for i, weight in enumerate(weights):
        abs_weight = abs(weight)
        # Position label after the bar
        x_pos = abs_weight + 0.05
        plt.text(x_pos, i, f'{weight:+d}', 
                ha='left', va='center')
    
    # Set x-axis limits to accommodate labels
    max_weight = max(abs_weights)
    plt.xlim(0, max_weight + 1)
    
    # Adjust layout
    plt.tight_layout()
    
    # Save plot
    plt.savefig('feature_weights.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    
    print("\nFeature weights plot saved as 'feature_weights.png'")

def main():
    print("Generating feature weights plot...")
    create_feature_weights_plot()

if __name__ == "__main__":
    main() 