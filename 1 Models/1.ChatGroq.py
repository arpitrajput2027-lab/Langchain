from langchain_groq import ChatGroq
from dotenv import load_dotenv
import time


load_dotenv()

model = ChatGroq(model='openai/gpt-oss-20b')
user_query = "What is AI ?"
response = model.invoke(user_query)



start_time = time.perf_counter()
response = model.invoke(user_query)
end_time = time.perf_counter()
print(response.content)

print("Response Time:", round(end_time - start_time, 2), "seconds")