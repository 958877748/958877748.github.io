from smolagents import CodeAgent, HfApiModel

model_id = "meta-llama/Llama-3.3-70B-Instruct" 

hf_api_token = "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"

model = HfApiModel(model_id=model_id, token=hf_api_token) # You can choose to not pass any model_id to HfApiModel to use a default free model
# you can also specify a particular provider e.g. provider="together" or provider="sambanova"
agent = CodeAgent(tools=[], model=model, add_base_tools=True)

agent.run(
    "Could you give me the 118th number in the Fibonacci sequence?",
)