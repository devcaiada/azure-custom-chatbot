import openai

# Configurações da API OpenAI
OPENAI_API_KEY = "<sua_chave_openai>"
openai.api_key = OPENAI_API_KEY

def generate_embedding(text):
    response = openai.Embedding.create(
        input=text,
        model="text-embedding-ada-002"
    )
    return response['data'][0]['embedding']

if __name__ == "__main__":
    texto_exemplo = "Este é um exemplo de texto para gerar embeddings."
    embedding = generate_embedding(texto_exemplo)
    print("Embedding gerado:", embedding)
