class SearchResult:
    def __init__(self, result_id, document_id, score):
        self.result_id = result_id
        self.document_id = document_id
        self.score = score

    def to_dict(self):
        return {
            "result_id": self.result_id,
            "document_id": self.document_id,
            "score": self.score
        }