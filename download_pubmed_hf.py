from datasets import load_dataset
import pandas as pd

print("Downloading PubMed QA dataset...")
dataset = load_dataset("pubmed_qa", "pqa_labeled")

rows = []
for item in dataset["train"]:
    rows.append({
        "id": item["pubid"],
        "title": item["question"],
        "abstract": item["context"]
    })

df = pd.DataFrame(rows)
df.to_csv("dataset/pubmed_large.csv", index=False)

print("Saved dataset/pubmed_large.csv")
