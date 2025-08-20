import os
import logging
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

logger = logging.getLogger("inst414.vis")

def generate_visuals(processed_csv: str, output_dir: str):
    os.makedirs(output_dir, exist_ok=True)
    df = pd.read_csv(processed_csv)

    # --- Visualization 1: Ratio of owners/reviews bar chart ---
    if "owners" in df.columns and "reviews" in df.columns:
        df = df.copy()
        df = df[df["reviews"] > 0]  # avoid divide by zero
        df["ratio"] = df["owners"] / df["reviews"]

        # Bin the ratios into buckets of 10 (like 10, 20, 30…)
        df["ratio_bin"] = (df["ratio"] // 10 * 10).astype(int)
        ratio_counts = df["ratio_bin"].value_counts().sort_index()

        plt.figure(figsize=(12, 7))
        ratio_counts.plot(kind="bar", color="cornflowerblue")
        plt.title("Ratio of Owners to Reviews")
        plt.xlabel("Ratio of owners / reviews")
        plt.ylabel("Number of games")
        for i, val in enumerate(ratio_counts.values):
            plt.text(i, val + 5, str(val), ha="center", fontsize=8)
        out = os.path.join(output_dir, "owners_reviews_ratio.png")
        plt.savefig(out, bbox_inches="tight")
        plt.close()
        logger.info(f"Wrote {out}")

    # --- Visualization 2: Boxplot of ratings for free vs paid games ---
    if "positive_ratings" in df.columns and "negative_ratings" in df.columns:
        df = df.copy()
        df["rating"] = df["positive_ratings"] / (df["positive_ratings"] + df["negative_ratings"]) * 100
        df["type"] = df["price"].apply(lambda x: "Free" if x == 0 else "Paid")

        # Subset: games with 20k+ owners
        if "owners" in df.columns:
            dfa = df[df["owners"] >= 20000].copy()
            dfa["subset"] = "20,000+ Owners"
        else:
            dfa = pd.DataFrame()

        dfb = df.copy()
        dfb["subset"] = "All Data"

        combined = pd.concat([dfa, dfb]) if not dfa.empty else dfb

        plt.figure(figsize=(10, 6))
        sns.boxplot(x="subset", y="rating", hue="type", data=combined)
        plt.title("Game Ratings: Free vs Paid")
        plt.ylabel("Rating (%)")
        plt.xlabel("")
        out = os.path.join(output_dir, "ratings_boxplot.png")
        plt.savefig(out, bbox_inches="tight")
        plt.close()
        logger.info(f"Wrote {out}")
