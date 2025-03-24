import pandas as pd
import sys

def preprocess_data(input_file, output_file):
    try:
        # Load the dataset
        df = pd.read_csv(input_file)

        # ====== Data Cleaning ======
        df.dropna(inplace=True)  # Remove missing values

        # ====== Data Transformation ======
        # Convert 'Review' to lowercase for consistency
        if 'Review' in df.columns:
            df['Review'] = df['Review'].str.lower()

        # ====== Data Reduction ======
        # No unnecessary columns in your dataset, so nothing to drop

        # ====== Data Discretization ======
        # Create a new column categorizing scores
        if 'Score' in df.columns:
            df['Score_Category'] = pd.cut(df['Score'], bins=[0, 3, 5, 7, 9, 10], 
                                          labels=['Very Low', 'Low', 'Medium', 'High', 'Very High'])

        # Save the cleaned dataset
        df.to_csv(output_file, index=False)
        print("Preprocessing completed successfully!")

    except Exception as e:
        print(f"Error in preprocessing: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 dpre.py <input-file> <output-file>")
        sys.exit(1)

    preprocess_data(sys.argv[1], sys.argv[2])
