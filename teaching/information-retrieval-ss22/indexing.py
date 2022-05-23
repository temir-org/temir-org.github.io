from typing import List, Tuple, Hashable, AnyStr


class Index:
    def __init__(self, documents: List[Tuple[Hashable, List[AnyStr]]]):
        """
        Builds an index for a given (preprocessed) document collection
        :param documents: documents in the form of (doc_id, [terms])
        :return:
        """
        # Build the set of index terms
        self.document_ids = {doc[0] for doc in documents}
        self.index_terms = {term for doc in documents for term in doc[1]}

        # Build the term-document matrix
        td_matrix = {}
        for doc in documents:
            row = {}
            for term in self.index_terms:
                row[term] = doc[1].count(term)
            td_matrix[doc[0]] = row
        
        self.td_matrix = td_matrix
        
        # Build the inverted index based on the term-document matrix
        self.index = {}
        for term in self.index_terms:
            docs = {}
            for doc_id in self.document_ids:
                if td_matrix[doc_id][term] > 0:
                    docs[doc_id] = td_matrix[doc_id][term] 
            self.index[term] = (sum(docs.values()), docs)

    def get_term_frequency(self, term: AnyStr, doc_id: Hashable) -> int:
        """
        Returns the term frequency for a specified term and document
        :param term: term to return the frequency for
        :param doc_id: document to return the frequency for
        :return: term frequency
        """
        try:
            return self.index[term][1][doc_id]
        except KeyError:
            # If the term does not exist in this document, return 0
            return 0

    def get_total_term_frequency(self, term: AnyStr) -> int:
        """
        Returns the total number of occurrences of a term across all documents
        :param term: term to return the frequency for
        :return: total term frequency
        """
        try:
            return self.index[term][0]
        except KeyError:
            # If the term does not exist, return 0
            return 0
        
    def get_document_frequency(self, term: AnyStr) -> int:
        """
        Returns the number of documents that contain the given term at least once
        :param term: term to return the frequency for
        :return: document frequency
        """
        try:
            return len(self.index[term][1])
        except KeyError:
            # If the term does not exist, return 0
            return 0

    def get_document_count(self):
        """
        Returns the number of documents in the index
        :return: number of indexed documents
        """
        return len(self.document_ids)

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
        return self.document_ids

    def get_index_terms(self) -> List:
        """
        Returns a list of all indexed terms
        :return:
        """
        return self.index_terms
