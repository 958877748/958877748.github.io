file_path = r'C:\Users\gl\GitHub\math3\repomix-output.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    all_code = file.read()

# huggingface
model = "Qwen/Qwen2.5-Coder-32B-Instruct"
base_url = "https://api-inference.huggingface.co/models/"+model+"/v1"
api_key = "hf_FZGHifwSLtbHMpb"
api_key += "zWmMktyjrBfXKMICbup"

# ollama
# base_url = "http://localhost:11434/v1"
# model = "llama3.2:1b"

# groq
# base_url = "https://api.groq.com/openai/v1"
# model = "llama-3.1-8b-instant"
# api_key = "gsk_TJXTeUuKEXQ7OdvrIkT1WGdy"
# api_key += "b3FYgdYYLstQGS0FeqLlhECkhqVu"

from openai import OpenAI

client = OpenAI(api_key=api_key, base_url=base_url)

stream = client.chat.completions.create(
    model=model, 
    messages=[
        {
            "role": "user",
            "content": all_code,
        }
    ],
    max_tokens=1000,
    stream=True
)
for chunk in stream:
    print(chunk.choices[0].delta.content, end="")