import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sys

def generate_visualization(input_file):
    try:
        # Load the preprocessed dataset
        df = pd.read_csv(input_file)

        # Check if required columns exist
        if 'Review' in df.columns and 'Score' in df.columns:
            plt.figure(figsize=(10, 6))
            sns.boxplot(x=df['Review'], y=df['Score'])
            plt.xticks(rotation=45)
            plt.title("Boxplot of Scores by Review Category")
            plt.xlabel("Review Category")
            plt.ylabel("Score")
            plt.savefig("/home/doc-bd-a1/vis.png")  # Save the figure
            print("Visualization saved as vis.png")
        else:
            print("Required columns for visualization not found.")

    except Exception as e:
        print(f"Error in visualization: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 vis.py <input-file>")
        sys.exit(1)

    generate_visualization(sys.argv[1])
