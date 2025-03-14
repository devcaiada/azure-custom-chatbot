class Document:
    def __init__(self, document_id, content):
        self.document_id = document_id
        self.content = content
        self.embedding = None

    def set_embedding(self, embedding):
        self.embedding = embedding

    def to_dict(self):
        return {
            "id": self.document_id,
            "content": self.content,
            "embedding": self.embedding
        }