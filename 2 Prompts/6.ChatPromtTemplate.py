from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
load_dotenv()

model = ChatGroq(model='openai/gpt-oss-20b')
chatPrompt = ChatPromptTemplate([
    ('system',"You are a Helpful {domain} expert AI Assistant"),
    ('human',"Explaiun {topic} in Simple")
])

prompt = chatPrompt.invoke({'domain':'Maths','topic':'e raise to the power i*pi'})
response = model.invoke(prompt)
print(prompt,"\n\n\n\n\n\n\n\n")
print(response.content)
