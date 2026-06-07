import tiktoken


# Text
#  → tokenize
#  → tokens list
#  → slice tokens [start:end]
#  → decode back to text

# Chunking method - Fixed length method
def fixed_length_chunk_text(body: dict, chunk_size: int, overlap: int):
    chunked_list = []

    required_keys = {"text", "source_blob", "page_number"}
    if not required_keys.issubset(body):
        raise ValueError("Invalid input format for chunking")

    encoder = tiktoken.encoding_for_model("gpt-4o-mini")
    tokens = encoder.encode(body["text"])
    tokens_len = len(tokens)

    start = 0
    idx = 0

    while start < tokens_len:
        end = start + chunk_size
        chunk_tokens = tokens[start:end]
        chunk_text = encoder.decode(chunk_tokens).strip()

        if chunk_text:
            chunked_list.append(
                {
                    "chunk_idx": idx,
                    "chunk_text": chunk_text,
                    "source_blob": body["source_blob"],
                    "page_no": body["page_number"]
                }
            )
            idx += 1

        start = end - overlap
        if start < 0:
            start = 0

    return chunked_list
