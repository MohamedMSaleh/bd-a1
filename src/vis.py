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
            # Aggregate the average score for each review category
            avg_scores = df.groupby('Review')['Score'].mean().reset_index()

            # Create the bar chart
            plt.figure(figsize=(10, 6))
            sns.barplot(x=avg_scores['Review'], y=avg_scores['Score'], palette="viridis")
            plt.xticks(rotation=45)
            plt.title("Average Score by Review Category")
            plt.xlabel("Review Category")
            plt.ylabel("Average Score")
            plt.ylim(0, 10)  # Scores range from 0 to 10
            plt.grid(axis='y', linestyle='--', alpha=0.7)

            # Save the figure
            plt.savefig("/home/doc-bd-a1/vis.png")
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
