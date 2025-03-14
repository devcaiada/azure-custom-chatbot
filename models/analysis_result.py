class AnalysisResult:
    def __init__(self, analysis_id, document_id, analysis_data):
        self.analysis_id = analysis_id
        self.document_id = document_id
        self.analysis_data = analysis_data

    def to_dict(self):
        return {
            "analysis_id": self.analysis_id,
            "document_id": self.document_id,
            "analysis_data": self.analysis_data
        }