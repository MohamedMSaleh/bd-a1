import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sys

def generate_visualization(input_file):
    try:
        # Load the preprocessed dataset
        df = pd.read_csv(input_file)

        # Ensure 'Console' and 'Score' exist
        if 'Console' in df.columns and 'Score' in df.columns:
            # Normalize Console column (split multi-platform entries and expand them)
            df = df.assign(Console=df['Console'].str.split(', ')).explode('Console')

            # Aggregate the average score per console
            avg_scores = df.groupby('Console')['Score'].mean().reset_index()

            # Create a bar chart
            plt.figure(figsize=(12, 6))
            sns.barplot(x=avg_scores['Console'], y=avg_scores['Score'], palette="viridis")

            plt.xticks(rotation=45)
            plt.title("Average Score by Console")
            plt.xlabel("Console")
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
