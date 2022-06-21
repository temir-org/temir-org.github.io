from .preprocessing import PreprocessorSpacy as Preprocessor
from .indexing_np import Index
from .models import Model


class RetrievalSystem:

    def __init__(self, corpus: list, model: Model):
        """
        Constructor
        :param corpus: document collection given as list of (doc_id, content) tuples
        :param model: retrieval model to calculate retrieval scores with
        """
        self.preprocessor = Preprocessor()
        self.index = Index(list(zip(
            [doc[0] for doc in corpus],
            map(self.preprocessor.preprocess, [doc[1] for doc in corpus])
        )))
        self.model = model

    def query(self, text, topK=-1):
        """
        Queries a given text against the index using a Dirichlet smoothed language model
        :param preprocessor: preprocessor instance to process the query with
        :param index: the index data to query against
        :param text: query text
        :param topK: number of top results to return
        :return: list of (doc_id, score) tuples descending by score for all documents in the vector space
        """
        query = self.preprocessor.preprocess(text)
        scores = {}
        topK = max(len(self.index.get_document_ids()), topK)
        for i, doc_id in enumerate(self.index.get_document_ids(), start=1):
            scores[doc_id] = self.model.score(self.index, query, doc_id)
        return sorted(scores.items(), key=lambda item: item[1], reverse=True)[:topK]

