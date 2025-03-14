import unittest
from models import Document

class TestDocumentModel(unittest.TestCase):

    def test_initialization(self):
        doc = Document(document_id="doc1", content="This is a test document.")
        self.assertEqual(doc.document_id, "doc1")
        self.assertEqual(doc.content, "This is a test document.")
        self.assertIsNone(doc.embedding)

    def test_set_embedding(self):
        doc = Document(document_id="doc1", content="This is a test document.")
        embedding = [0.1, 0.2, 0.3]
        doc.set_embedding(embedding)
        self.assertEqual(doc.embedding, embedding)

    def test_to_dict(self):
        doc = Document(document_id="doc1", content="This is a test document.")
        embedding = [0.1, 0.2, 0.3]
        doc.set_embedding(embedding)
        expected_dict = {
            "id": "doc1",
            "content": "This is a test document.",
            "embedding": embedding
        }
        self.assertEqual(doc.to_dict(), expected_dict)

if __name__ == "__main__":
    unittest.main()