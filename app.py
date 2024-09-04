from fastapi import FastAPI
from transformers import pipeline


## Create FastAPi instance

app = FastAPI()

# Init Text Generation pipeline

pipe = pipeline("text2text-generation", model="google/flan-t5-small")

@app.get('/')
def home():
    return {"a":"s"}

@app.get("/gen")
def generate(text:str):
    output=pipe(text)
    return {"output": output[0]["generated_text"]}