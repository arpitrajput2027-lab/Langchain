# from transformers import AutoTokenizer

# tokenizer = AutoTokenizer.from_pretrained(
#     "sentence-transformers/all-MiniLM-L6-v2"
# )

# text = "My Name is Arpit Verma"

# tokens = tokenizer.tokenize(text)
# token_ids = tokenizer.encode(text)

# print(tokens)
# print(token_ids)
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained(
    "sentence-transformers/all-MiniLM-L6-v2"
)

text = "Nisha loves Aryan"

# Tokenization
tokens = tokenizer.tokenize(text)

# Token IDs
ids = tokenizer.encode(text)

# Convert IDs back into tokens
decoded_tokens = tokenizer.convert_ids_to_tokens(ids)

# Decode IDs into original readable text
decoded_text = tokenizer.decode(ids)

print("Original Text:", text)
print("Tokens:", tokens)
print("Token IDs:", ids)
print("Decoded Tokens:", decoded_tokens)
print("Decoded Text:", decoded_text)