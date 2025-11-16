"""
Simple inference example using Hugging Face.
"""
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

def summarize(text, model_name='google/pegasus-large'):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    inputs = tokenizer([text], max_length=1024, truncation=True, return_tensors='pt')
    outputs = model.generate(**inputs, max_new_tokens=150)

    return tokenizer.batch_decode(outputs, skip_special_tokens=True)[0]

if __name__ == '__main__':
    text = """Background: Hypertension is a major risk factor. Methods: We studied drug X in 200 adults. Results: Drug X reduced systolic BP by 8 mmHg."""
    print(summarize(text))
