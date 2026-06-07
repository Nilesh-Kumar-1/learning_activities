from azure.ai.inference import EmbeddingsClient

def generate_embedding(text: str, client: EmbeddingsClient):
    """sumary_line
    
    Keyword arguments:
    argument -- description
    Return: return_description
    """

    try:
        embedding = client.embed(input=[text])
        emb = embedding.data[0].embedding
    except Exception as e:
        print(f"Error ocuured while generating emebeding - {e}")
        raise
    return emb
    

