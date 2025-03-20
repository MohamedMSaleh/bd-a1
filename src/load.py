import sys
import pandas as pd

def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print("Dataset loaded successfully!")
        df.to_csv("/home/doc-bd-a1/res_load.csv", index=False)  # Save for next step
        return df
    except Exception as e:
        print(f"Error loading dataset: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 load.py <dataset-path>")
        sys.exit(1)

    dataset_path = sys.argv[1]
    load_data(dataset_path)
