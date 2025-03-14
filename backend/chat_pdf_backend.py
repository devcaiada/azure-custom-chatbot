import os
from azure.storage.blob import BlobServiceClient
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential

# Configurações do Azure
AZURE_BLOB_CONNECTION_STRING = "<sua_connection_string>"
AZURE_FORM_RECOGNIZER_ENDPOINT = "<seu_endpoint>"
AZURE_FORM_RECOGNIZER_KEY = "<sua_chave>"

# Inicialização dos clientes
blob_service_client = BlobServiceClient.from_connection_string(AZURE_BLOB_CONNECTION_STRING)
document_analysis_client = DocumentAnalysisClient(
    endpoint=AZURE_FORM_RECOGNIZER_ENDPOINT,
    credential=AzureKeyCredential(AZURE_FORM_RECOGNIZER_KEY)
)


def upload_to_blob(file_path, container_name):
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=os.path.basename(file_path))
    with open(file_path, "rb") as data:
        blob_client.upload_blob(data, overwrite=True)
    return blob_client.url


def analyze_pdf(blob_url):
    poller = document_analysis_client.begin_analyze_document_from_url("prebuilt-document", blob_url)
    result = poller.result()
    extracted_text = " ".join([line.content for page in result.pages for line in page.lines])
    return extracted_text


if __name__ == "__main__":
    # Exemplo de uso
    file_path = "sample.pdf"
    container_name = "pdf-container"

    # Upload do PDF
    blob_url = upload_to_blob(file_path, container_name)
    print("Arquivo carregado no Azure Blob Storage:", blob_url)

    # Extração de texto
    text = analyze_pdf(blob_url)
    print("Texto extraído:", text)
