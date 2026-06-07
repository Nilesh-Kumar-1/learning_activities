# import tiktoken

# encoder = tiktoken.encoding_for_model("gpt-4o-mini") # here gpt-4o is a placeholder and no actual model is used.
# text = "Employees must apply for leave via the HR portal."

# tokens = encoder.encode(text)
# token_count = len(tokens)

# print(token_count)
# print(tokens[1:5])
# decode_tokens = encoder.decode(tokens=tokens)
# print(decode_tokens[1:5])

text = "Employees must apply for leave via the HR portal."

print(text.split())
