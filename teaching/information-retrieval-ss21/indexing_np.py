from typing import List, Tuple, Hashable, AnyStr
import numpy as np


class Index:
    def __init__(self, documents: List[Tuple[Hashable, List[AnyStr]]]):
        """
        Builds an index for a given (preprocessed) document collection
        :param documents: documents in the form of (doc_id, [terms])
        :return:
        """
        # Build the set of index terms
        self.document_ids = np.array([doc[0] for doc in documents])
        self.index_terms = np.array(list({term for doc in documents for term in doc[1]}))
        self.num_docs = self.document_ids.shape[0]
        self.num_terms = self.index_terms.shape[0]

        # Build the document-term matrix
        X = np.zeros(shape=(self.num_docs, self.num_terms), dtype=np.int32)
        for i in range(self.num_docs):
            for j in range(self.num_terms):
                X[i, j] = documents[i][1].count(self.index_terms[j])

        # Build the inverted index based on the document-term matrix
        # Note that since we dont do any compression or sparse matrices,
        # this is just the transposed document-term matrix
        self.index = X.transpose()

    def get_term_frequency(self, term: AnyStr, doc_id: Hashable) -> int:
        """
        Returns the term frequency for a specified term and document
        :param term: term to return the frequency for
        :param doc_id: document to return the frequency for
        :return: term frequency
        """
        i = np.where(self.index_terms == term)[0]
        j = np.where(self.document_ids == doc_id)[0]
        if i.shape != (1,) or j.shape != (1,):
            return 0
        else:
            return self.index[i, j]

    def get_total_term_frequency(self, term: AnyStr) -> int:
        """
        Returns the total number of occurrences of a term across all documents
        :param term: term to return the frequency for
        :return: total term frequency
        """
        i = np.where(self.index_terms == term)[0]
        if i.shape != (1,):
            return 0
        else:
            return np.sum(self.index[i])
        
    def get_document_frequency(self, term: AnyStr) -> int:
        """
        Returns the number of documents that contain the given term at least once
        :param term: term to return the frequency for
        :return: document frequency
        """
        i = np.where(self.index_terms == term)
        if i.shape != (1,):
            return 0
        else:
            return np.count_nonzero(self.index[i])

    def get_document_count(self):
        """
        Returns the number of documents in the index
        :return: number of indexed documents
        """
        return len(self.document_ids)

    def get_document_length(self, doc_id: Hashable):
        """
        Returns the number of tokens in a document (including multiple occurences of the same token)
        :param doc_id: document to count tokens for
        :return: total number of token occurences in the specified document
        """
        j = np.where(self.document_ids == doc_id)[0]
        if j.shape != (1,):
            return 0
        else:
            return np.sum(self.index[:, j])

    def get_total_document_length(self):
        """
        Returns the total number of tokens in the collection
        :return: total number of token occurences in the collection
        """
        return np.sum(self.index)

    def get_term_count(self):
        """
        Returns the number of terms in the index
        :return: number of indexed terms
        """
        return len(self.index_terms)

    def get_document_ids(self) -> List:
        """
        Returns a list of IDs for all documents in the index
        :return:
        """
        return list(self.document_ids)

    def get_index_terms(self) -> List:
        """
        Returns a list of all indexed terms
        :return:
        """
        return list(self.index_terms)
