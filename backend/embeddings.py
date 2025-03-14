import openai
from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
from config import OPENAI_API_KEY, AZURE_SEARCH_ENDPOINT, AZURE_SEARCH_KEY, AZURE_SEARCH_INDEX

# Configurações da API OpenAI e Azure Cognitive Search
openai.api_key = OPENAI_API_KEY

search_client = SearchClient(
    endpoint=AZURE_SEARCH_ENDPOINT,
    index_name=AZURE_SEARCH_INDEX,
    credential=AzureKeyCredential(AZURE_SEARCH_KEY)
)

def generate_embedding(text):
    response = openai.Embedding.create(
        input=text,
        model="text-embedding-ada-002"
    )
    return response['data'][0]['embedding']

def index_document(document_id, text):
    embedding = generate_embedding(text)
    document = {
        "@search.action": "upload",
        "id": document_id,
        "content": text,
        "embedding": embedding
    }
    search_client.upload_documents(documents=[document])

if __name__ == "__main__":
    texto_exemplo = "Este é um exemplo de texto para gerar embeddings."
    index_document("doc1", texto_exemplo)
    print("Documento indexado com sucesso.")