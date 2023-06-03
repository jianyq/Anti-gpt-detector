import torch
from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, AutoModelForSequenceClassification
# from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer1 = AutoTokenizer.from_pretrained("Hello-SimpleAI/chatgpt-detector-roberta")

model1 = AutoModelForSequenceClassification.from_pretrained("Hello-SimpleAI/chatgpt-detector-roberta")


app = FastAPI()
origins = [
    "http://localhost:5173",  # Vue.js app
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

tokenizer = AutoTokenizer.from_pretrained("t5-base")
model = AutoModelForSeq2SeqLM.from_pretrained("Vamsi/T5_Paraphrase_Paws")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

@app.get("/paraph/")
def read_root(q: Union[str, None] = None):
    text =  "paraphrase: " + q + " </s>"

    encoding = tokenizer.encode_plus(text,pad_to_max_length=True, return_tensors="pt")

    input_ids, attention_masks = encoding["input_ids"].to(device), encoding["attention_mask"].to(device)

    outputs = model.generate(
        input_ids=input_ids, attention_mask=attention_masks,
        max_length=256,
        do_sample=True,
        top_k=200,
        # top_p=0.95,
        temperature=1.2,
        early_stopping=True,
        num_return_sequences=5
    )

    lines = []
    for output in outputs:
        line = tokenizer.decode(output, skip_special_tokens=True,clean_up_tokenization_spaces=True)
        print(line)
        lines.append(line)
    return {"result": lines}

@app.get("/detect/")
def query1(q: Union[str, None] = None):
	inputs = tokenizer1(q, return_tensors="pt")
	with torch.no_grad():
		logits = model1(**inputs).logits
	predicted_class_id = logits.argmax().item()
	print(model1.config.id2label[predicted_class_id])
	return model1.config.id2label[predicted_class_id]