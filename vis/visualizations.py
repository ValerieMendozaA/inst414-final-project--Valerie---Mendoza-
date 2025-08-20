import os
import logging
import pandas as pd
import matplotlib.pyplot as plt

logger = logging.getLogger("inst414.vis")


def generate_visuals(processed_csv: str, output_dir: str):
    os.makedirs(output_dir, exist_ok=True)
    df = pd.read_csv(processed_csv)

    target = "owners" if "owners" in df.columns else ("owner_estimate" if "owner_estimate" in df.columns else None)

    if target and "price" in df.columns:
        plt.figure(figsize=(8, 6))
        plt.scatter(df["price"], df[target], alpha=0.5)
        plt.title(f"Price vs {target.replace('_', ' ').title()}")
        plt.xlabel("Price")
        plt.ylabel(target.replace("_", " ").title())
        plt.grid(True)
        out = os.path.join(output_dir, "price_vs_target.png")
        plt.savefig(out, bbox_inches="tight")
        plt.close()
        logger.info(f"Wrote {out}")

    if "positive_ratings" in df.columns:
        plt.figure(figsize=(8, 6))
        df["positive_ratings"].dropna().plot(kind="hist", bins=30)
        plt.title("Distribution of Positive Ratings")
        plt.xlabel("Positive Ratings")
        plt.ylabel("Frequency")
        plt.grid(True)
        out = os.path.join(output_dir, "positive_ratings_hist.png")
        plt.savefig(out, bbox_inches="tight")
        plt.close()
        logger.info(f"Wrote {out}")


