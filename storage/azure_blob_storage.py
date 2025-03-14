from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import os

class AzureBlobStorage:
    def __init__(self, connection_string, container_name):
        self.blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        self.container_client = self.blob_service_client.get_container_client(container_name)

    def upload_blob(self, blob_name, file_path):
        blob_client = self.container_client.get_blob_client(blob_name)
        with open(file_path, "rb") as data:
            blob_client.upload_blob(data)
        return blob_client.url

    def download_blob(self, blob_name, download_path):
        blob_client = self.container_client.get_blob_client(blob_name)
        with open(download_path, "wb") as download_file:
            download_file.write(blob_client.download_blob().readall())

    def list_blobs(self):
        return [blob.name for blob in self.container_client.list_blobs()]