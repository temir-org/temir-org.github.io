from math import sqrt, pow, log
import numpy as np


class Model:
    def __init__(self):
        """
        Constructor
        """
        pass

    def score(self, index, query, doc_id):
        """
        Calculates the relevance score for a document (given by index and doc_id) and query (give ans query term list)
        :param index: index to get relevance data from
        :param query: query to calculate the relevance for
        :param doc_id: document to calculate the relevance for
        :return: relevance score
        """
        return 1


class TfIdf(Model):
    def __init__(self):
        """
        Constructor
        """
        super().__init__()

    def score(self, index, query, doc_id):
        """
        Calculates the relevance of a document given a query using cosine similarity of TFIDF vectors
        :param index: index to get relevance data from
        :param query: query to calculate the relevance for
        :param doc_id: document to calculate the relevance for
        :return: TFIDF relevance score
        """
        query_vec = self._get_query_representation(query, index)
        doc_vec = self._get_document_representation(doc_id, index)
        return self._similarity(query_vec, doc_vec)

    @staticmethod
    def _tfidf(term_frequency: int, document_frequency: int, document_count: int) -> float:
        """
        Term-frequency-inverted-document-frequency, which calculates the tfidf for a given term frequency,
        document frequency and document count.
        :param term_frequency: The frequency of the term in the document.
        :param document_frequency: :param document_count: :returns: tfidf for the word and the argument,
        0 if not present.
        """
        if term_frequency == 0:
            return 0
        else:
            tf = 1 + np.log(term_frequency)
            idf = np.log(document_count / document_frequency)
            return tf * idf

    def _get_document_representation(self, doc_id, index):
        """
        Returns the tfidf vector for a given doc_id and index
        :param doc_id: doc_id to construct the vector for
        :param index: index to construct the vector from
        :return: the tfidf vector for this document
        """
        vec = np.zeros(shape=(index.num_terms,), dtype=np.float64)
        for i, term in enumerate(sorted(index.get_index_terms())):
            vec[i] = self._tfidf(
                index.get_term_frequency(term, doc_id),
                index.get_document_frequency(term),
                index.get_document_count()
            )
        return vec

    def _get_query_representation(self, query, index):
        """
        Returns the tfidf vector for an arbitrary string.
        :param query: query term list to construct the vector for
        :param index: index to construct the vector from
        :return: the tfidf vector for the string
        """
        term_frequencies = {term: query.count(term) for term in query}
        vec = np.zeros(shape=(index.num_terms,), dtype=np.float64)
        for i, term in enumerate(sorted(index.get_index_terms())):
            vec[i] = self._tfidf(
                term_frequencies.get(term, 0),
                index.get_document_frequency(term),
                index.get_document_count()
            )
        return vec

    @staticmethod
    def _similarity(vec_a, vec_b):
        try:
            return np.dot(vec_a, vec_b) / (np.linalg.norm(vec_a) * np.linalg.norm(vec_b))
        except ZeroDivisionError:
            return 0


class JelinekMercerLM(Model):
    def __init__(self, omega=0.1):
        """
        Constructor
        :param omega: omega parameter for Jelinek-Mercer smoothing
        """
        super().__init__()
        self.omega = omega

    def score(self, index, query, doc_id):
        """
        Calculates the relevance of a document given a query using Jelinek-Mercer smoothing.
        :param index: index to get relevance data from
        :param query: query to calculate the relevance for
        :param doc_id: document to calculate the relevance for
        :return: relevance score
        """
        rho = 1
        doc_length = index.get_document_length(doc_id)
        total_doc_length = index.get_total_document_length()
        for term in query:
            frequency = index.get_term_frequency(term, doc_id)
            total_frequency = index.get_total_term_frequency(term)
            try:
                rho += np.log(self._term_probability(frequency, total_frequency, doc_length, total_doc_length))
            except ValueError:
                rho += 0
        return float(rho)

    def _term_probability(self, frequency, total_frequency, doc_length, total_doc_length):
        """
        Calculates the conditional probability of a term give a document using Jelinek-Mercer smoothing.
        :param frequency: term frequency of the current term and document
        :param total_frequency: total term frequency of the current term
        :param doc_length: length of the document to calculate the probability for
        :param total_doc_length: cumulative length of all documents in the collection
        """
        if doc_length == 0:
            p1 = 0
        else:
            p1 = frequency / doc_length
        if total_doc_length == 0:
            p2 = 0
        else:
            p2 = total_frequency / total_doc_length
        return (1-self.omega) * p1 + self.omega * p2


class DirichletLM(Model):
    def __init__(self, alpha=1000):
        """
        Constructor
        :param alpha: alpha parameter for Dirichlet smoothing
        """
        super().__init__()
        self.alpha = alpha

    def score(self, index, query, doc_id):
        """
        Calculates the relevance of a document given a query using Dirichlet smoothing.
        :param index: index to get relevance data from
        :param query: query to calculate the relevance for
        :param doc_id: document to calculate the relevance for
        :return: relevance score
        """
        rho = 1
        doc_length = index.get_document_length(doc_id)
        total_doc_length = index.get_total_document_length()
        for term in query:
            frequency = index.get_term_frequency(term, doc_id)
            total_frequency = index.get_total_term_frequency(term)
            try:
                rho += np.log(self._term_probability(frequency, total_frequency, doc_length, total_doc_length))
            except ValueError:
                rho += 0
        return float(rho)

    def _term_probability(self, frequency, total_frequency, doc_length, total_doc_length):
        """
        Calculates the conditional probability of a term give a document using Dirichlet smoothing.
        :param frequency: term frequency of the current term and document
        :param total_frequency: total term frequency of the current term
        :param doc_length: length of the document to calculate the probability for
        :param total_doc_length: cumulative length of all documents in the collection
        """
        omega = self.alpha / (doc_length + self.alpha)
        if doc_length == 0:
            p1 = 0
        else:
            p1 = frequency / doc_length
        if total_doc_length == 0:
            p2 = 0
        else:
            p2 = total_frequency / total_doc_length
        return (1-omega) * p1 + omega * p2
