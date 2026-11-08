from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-3.8-flash')

response = model.invoke("What is AI and it's definition?")
print(response.content[0]["text"])
