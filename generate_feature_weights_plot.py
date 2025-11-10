#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np

def create_feature_weights_plot():
    """Create a plot showing normalized weights (total = 100) for features."""

    # Base weights aligned with generate_feature_plot.py (positives vs negatives)
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
        'IP Checks': 4         # awarded when "Yes"
    }

    # Normalize absolute weights to sum to 100 and round preserving total
    total_abs = sum(abs(w) for w in base_feature_weights.values())
    scaled = {k: abs(v) * (100.0 / total_abs) for k, v in base_feature_weights.items()}

    items = sorted(scaled.items(), key=lambda kv: kv[1], reverse=True)
    rounded_abs = {k: int(v) for k, v in items}
    remainder = 100 - sum(rounded_abs.values())
    if remainder != 0:
        fractions = sorted(((k, scaled[k] - int(scaled[k])) for k, _ in items), key=lambda kv: kv[1], reverse=True)
        idx = 0
        step = 1 if remainder > 0 else -1
        while remainder != 0 and idx < len(fractions):
            k = fractions[idx][0]
            new_val = rounded_abs[k] + step
            if new_val >= 0:
                rounded_abs[k] = new_val
                remainder -= step
            idx = (idx + 1) % len(fractions)

    # Apply original signs to the rounded magnitudes for labeling
    signed_weights = {k: (rounded_abs[k] if base_feature_weights[k] > 0 else -rounded_abs[k]) for k in rounded_abs}

    # Sort by absolute value for display
    sorted_features = dict(sorted(signed_weights.items(), key=lambda x: abs(x[1]), reverse=True))

    # Prepare data
    features = list(sorted_features.keys())
    weights_signed = list(sorted_features.values())
    abs_weights = [abs(w) for w in weights_signed]

    # Create figure
    plt.figure(figsize=(10, 6))

    # Create horizontal bars with absolute values
    y_pos = np.arange(len(features))
    bars = plt.barh(y_pos, abs_weights, height=0.5)

    # Color bars based on positive/negative values
    for bar, w in zip(bars, weights_signed):
        bar.set_color('#777777' if w > 0 else '#999999')

    # Customize plot
    plt.title('Feature Weights', fontsize=14, pad=20)
    plt.xlabel('Weight', fontsize=12)

    # Set y-axis labels
    plt.yticks(y_pos, features)

    # Add gridlines
    plt.grid(axis='x', alpha=0.1, linestyle='-')

    # Add value labels after the bars
    for i, w in enumerate(weights_signed):
        x_pos = abs(w) + 0.05
        plt.text(x_pos, i, f'{w:+d}', ha='left', va='center')

    # Set x-axis limits to accommodate labels
    max_weight = max(abs_weights) if abs_weights else 0
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