import pandas as pd
import matplotlib.pyplot as plt
import os
def generate_visuals(data_path, output_dir):
    df = pd.read_csv(data_path)
    os.makedirs(output_dir, exist_ok=True)

    # Scatter plot: price vs owners
    if "price" in df.columns and "owners" in df.columns:
        plt.figure(figsize=(8, 6))
        plt.scatter(df["price"], df["owners"], alpha=0.5)
        plt.title("Price vs. Owners")
        plt.xlabel("Price")
        plt.ylabel("Estimated Owners")
        plt.grid(True)
        plt.savefig(os.path.join(output_dir, "price_vs_owners.png"))
        plt.close()

    # Histogram: positive ratings
    if "positive_ratings" in df.columns:
        plt.figure(figsize=(8, 6))
        plt.hist(df["positive_ratings"].dropna(), bins=30, color='skyblue')
        plt.title("Distribution of Positive Ratings")
        plt.xlabel("Positive Ratings")
        plt.ylabel("Frequency")
        plt.grid(True)
        plt.savefig(os.path.join(output_dir, "positive_ratings_hist.png"))
        plt.close()

    print("Visualizations saved to:", output_dir)

if __name__ == "__main__":
    cleaned_path = "inst414-final-project-valerie-mendoza/data/processed/steam_games_cleaned.csv"
    output_path = "inst414-final-project-valerie-mendoza/data/outputs"
    generate_visuals(cleaned_path, output_path)

