# Example taken from https://huggingface.co/docs/transformers/main/model_doc/mistral#usage-tips
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("TheBloke/Mistral-7B-Instruct-v0.1-AWQ", device_map="auto")
tokenizer = AutoTokenizer.from_pretrained("TheBloke/Mistral-7B-Instruct-v0.1-AWQ")

prompt = "My favorite animal is"

model_inputs = tokenizer([prompt], return_tensors="pt").to("cuda")
model.to("cuda")

generated_ids = model.generate(**model_inputs, max_new_tokens=100, do_sample=True)

print("==========================================================")
print(tokenizer.batch_decode(generated_ids)[0])