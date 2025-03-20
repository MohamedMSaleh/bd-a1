import pandas as pd
import sys

def preprocess_data(input_file, output_file):
    try:
        # Load the dataset
        df = pd.read_csv(input_file)

        # ====== Data Cleaning ======
        df.dropna(inplace=True)  # Remove missing values

        # ====== Data Transformation ======
        if 'price' in df.columns:  # Example: Convert 'price' column to numeric
            df['price'] = pd.to_numeric(df['price'], errors='coerce').fillna(0)

        # ====== Data Reduction ======
        if 'id' in df.columns:  # Drop an unnecessary column if exists
            df.drop(columns=['id'], inplace=True)

        # ====== Data Discretization ======
        if 'rating' in df.columns:
            df['rating_category'] = pd.cut(df['rating'], bins=[0, 2, 4, 6, 8, 10], 
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
