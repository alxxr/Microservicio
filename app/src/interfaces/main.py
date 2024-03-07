from fastapi import FastAPI
from application.sentiment_analysis_service import analyze_sentiment
from application.preprocessing_service import preprocess_text
from domain.models import Prospect, Request
from infrastructure.hugging_face import model, tokenizer

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to my REST API"}

@app.post("/analyze_sentiment/")
async def analyze_sentiment_endpoint(request: Request):
    texts = [message for prospect in request.prospects for message in prospect.messages]
    input_ids, attention_mask = preprocess_text(tokenizer, texts)
    probabilities = analyze_sentiment(model, tokenizer, texts)
    
    positive_results = []
    neutral_results = []
    
    for i, prospect in enumerate(request.prospects):
        positive_score = probabilities[i, 2].item()
        neutral_score = probabilities[i, 1].item()

        positive_results.append({"prospect": prospect.prospect, "score": positive_score})
        neutral_results.append({"prospect": prospect.prospect, "score": neutral_score})

    output = {"positive": positive_results, "neutral": neutral_results}
    return output

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

