# from langchain_groq import ChatGroq
# from dotenv import load_dotenv
# load_dotenv()

# model = ChatGroq(model='openai/gpt-oss-20b')
# chat_history = []
# while True:
#     user_query = input("You :")
#     chat_history.append(user_query)
#     if user_query == "exit":
#         break
#     response = model.invoke(chat_history)
#     chat_history.append(response.content)
#     print("AI :",response.content)
# print(chat_history)


# With Message memory :
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage,SystemMessage,AIMessage
from dotenv import load_dotenv
load_dotenv()

model = ChatGroq(model='openai/gpt-oss-20b')

chat_history = [
    SystemMessage(content="You are a Helpful AI Assistant")
]
while True:
    user_query = input("You :")
    chat_history.append(HumanMessage(content=user_query))

    if user_query == "exit":
        break
    response = model.invoke(chat_history)
    chat_history.append(AIMessage(content=response.content))
    print("AI :",response.content)
print(chat_history)