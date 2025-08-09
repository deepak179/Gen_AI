from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  #To load environment variables

llm = OpenAI(model='gpt-3.5-turbo-instruct')

result = llm.invoke("What is the capital of India")    #Will hit model with a query and model will return some response based on query

print(result)