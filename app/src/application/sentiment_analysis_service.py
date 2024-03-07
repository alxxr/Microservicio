import torch
from application.preprocessing_service import preprocess_text

def analyze_sentiment(model, tokenizer, texts):
    input_ids, attention_mask = preprocess_text(tokenizer, texts)
    with torch.no_grad():
        outputs = model(input_ids, attention_mask=attention_mask)
        probabilities = torch.nn.functional.softmax(outputs.logits, dim=-1)
    return probabilities