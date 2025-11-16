import argparse
import json
from pathlib import Path
import pandas as pd

def preprocess(input_csv, output_jsonl):
    df = pd.read_csv(input_csv)
    out = []
    for _, r in df.iterrows():
        out.append({
            "id": int(r["id"]),
            "title": r.get("title", ""),
            "abstract": r.get("abstract", "")
        })
    with open(output_jsonl, "w", encoding="utf-8") as f:
        for item in out:
            f.write(json.dumps(item) + "\n")

def run_full_demo(args):
    print("Running preprocessing...")
    preprocess(args.input_csv, args.output_jsonl)
    print("Saved:", args.output_jsonl)

    output_summaries = Path(args.output_summary_jsonl)
    print(f"\nGenerating summaries for all entries...")

    with open(args.output_jsonl, "r", encoding="utf-8") as f_in, \
         open(output_summaries, "w", encoding="utf-8") as f_out:
        for line in f_in:
            doc = json.loads(line)
            # You can adjust the slicing as needed or remove it to keep full abstract
            summary = doc["abstract"][:200]  
            f_out.write(json.dumps({"id": doc["id"], "summary": summary}) + "\n")

    print(f"All summaries saved to: {output_summaries}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_csv', default='dataset/pubmed_large.csv')
    parser.add_argument('--output_jsonl', default='dataset/pubmed_large.jsonl')
    parser.add_argument('--output_summary_jsonl', default='dataset/pubmed_summaries.jsonl')
    args = parser.parse_args()
    run_full_demo(args)





