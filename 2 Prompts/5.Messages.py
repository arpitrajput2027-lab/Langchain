from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

model = ChatGroq(model='openai/gpt-oss-20b')

message = [
    SystemMessage(content="You are a Helpfull AI Assistant."),
    HumanMessage(content="Tell me about India")
]
response = model.invoke(message)
message.append(AIMessage(content=response.content))
print(message)
