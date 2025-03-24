import pandas as pd
import sys

def generate_insights(input_file):
    try:
        # Load the preprocessed dataset
        df = pd.read_csv(input_file)

        # Ensure there is data to analyze
        if df.empty:
            print("Error: The dataset is empty.")
            sys.exit(1)

        # Example Insight 1: Number of rows and columns
        insight_1 = f"Dataset contains {df.shape[0]} rows and {df.shape[1]} columns."

        # Example Insight 2: Most common review category (no need for NaN check)
        if 'Review' in df.columns:
            most_common_review = df['Review'].mode()[0]
            insight_2 = f"The most common review category is: {most_common_review}"
        else:
            insight_2 = "Review column not found."

        # Example Insight 3: Average score
        if 'Score' in df.columns:
            avg_score = df['Score'].mean()
            insight_3 = f"The average score is: {avg_score:.2f}"
        else:
            insight_3 = "Score column not found."

        # Save each insight to a separate file
        with open("/home/doc-bd-a1/eda-in-1.txt", "w") as f1:
            f1.write(insight_1 + "\n")
        with open("/home/doc-bd-a1/eda-in-2.txt", "w") as f2:
            f2.write(insight_2 + "\n")
        with open("/home/doc-bd-a1/eda-in-3.txt", "w") as f3:
            f3.write(insight_3 + "\n")

        print("EDA completed successfully!")

    except Exception as e:
        print(f"Error in EDA: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 eda.py <input-file>")
        sys.exit(1)

    generate_insights(sys.argv[1])
