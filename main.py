from langchain.llms import OpenAI

#SECURE THIS KEY
api_key = ''

llm = OpenAI(
    openai_api_key = api_key
)

result = llm("Write a very very short poem")
print(result)