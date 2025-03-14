import os


# Configurações do Azure Blob Storage
AZURE_BLOB_CONNECTION_STRING = os.getenv("AZURE_BLOB_CONNECTION_STRING", "<sua_connection_string>")

# Configurações do Azure Form Recognizer
AZURE_FORM_RECOGNIZER_ENDPOINT = os.getenv("AZURE_FORM_RECOGNIZER_ENDPOINT", "<seu_endpoint>")
AZURE_FORM_RECOGNIZER_KEY = os.getenv("AZURE_FORM_RECOGNIZER_KEY", "<sua_chave>")

# Configurações da API OpenAI
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "<sua_chave_openai>")

# Configurações do Azure Cognitive Search
AZURE_SEARCH_ENDPOINT = os.getenv("AZURE_SEARCH_ENDPOINT", "<seu_endpoint_search>")
AZURE_SEARCH_KEY = os.getenv("AZURE_SEARCH_KEY", "<sua_chave_search>")
AZURE_SEARCH_INDEX = os.getenv("AZURE_SEARCH_INDEX", "<seu_indice>")