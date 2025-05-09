import pandas as pd
from sklearn.cluster import KMeans
import sys

def apply_kmeans(input_file, output_file):
    try:
        # Load the dataset
        df = pd.read_csv(input_file)

        # Ensure 'Score' exists
        if 'Score' not in df.columns:
            print("Error: 'Score' column not found in dataset.")
            sys.exit(1)

        # Prepare the data for clustering (only using 'Score')
        X = df[['Score']]

        # Apply K-Means with k=3
        kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
        df['Cluster'] = kmeans.fit_predict(X)

        # Count records in each cluster
        cluster_counts = df['Cluster'].value_counts().to_dict()

        # Save cluster counts to a text file
        with open(output_file, "w") as f:
            for cluster, count in cluster_counts.items():
                f.write(f"Cluster {cluster}: {count} records\n")

        print("K-Means clustering completed successfully!")

    except Exception as e:
        print(f"Error in K-Means clustering: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 model.py <input-file> <output-file>")
        sys.exit(1)

    apply_kmeans(sys.argv[1], sys.argv[2])
