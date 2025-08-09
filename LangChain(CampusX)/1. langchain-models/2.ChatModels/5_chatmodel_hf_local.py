from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline    #To setup and use model locally we use pipeline
import os

os.environ['HF_HOME'] = 'D:/huggingface_cache'   #to change our current directory so that model downloads in specified path rather than in default C drive

llm = HuggingFacePipeline.from_model_id(
    model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    task='text-generation',
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=100
    )
)
model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of India")

print(result.content)