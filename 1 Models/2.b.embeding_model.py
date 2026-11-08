from langchain_huggingface import HuggingFaceEmbeddings

embeding = HuggingFaceEmbeddings(model='sentence-transformers/all-MiniLM-L6-v2')


text = "My Name is Arpit Verma"

vector = embeding.embed_query(text)

print(vector)