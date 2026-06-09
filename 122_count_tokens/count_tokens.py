import tiktoken

def count_tokens(text: str, model="gpt-4"):
    encoding = tiktoken.encoding_for_model(model)
    return len(encoding.encode(text))


print(count_tokens("Hello, how are you?", model="gpt-4"))