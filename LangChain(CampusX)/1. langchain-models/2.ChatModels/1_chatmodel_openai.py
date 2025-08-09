from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4', temperature=1.5, max_completion_tokens=10)   #Higher the temperature more creative is the response

result = model.invoke("Write a 5 line poem on cricket")   #result contains resulted output in content and metadata of that output

print(result.content)