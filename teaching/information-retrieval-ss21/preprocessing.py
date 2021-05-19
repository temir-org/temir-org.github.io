import re

class Preprocessor:
    def __init__(self, stopword_file="../data/stopwords.txt"):
        self.stopwords = self._get_stopwords_(stopword_file)

    @staticmethod
    def _get_stopwords_(path):
        """
        Reads a list of stopwords from the specified file
        :param path: path to the stopwords file
        :return: list of stopwords
        """
        with open(path, "r") as stopword_file:
            stopwords = stopword_file.readlines()
            stopwords = list(map(str.strip, stopwords))
        return stopwords

    @staticmethod
    def _tokenize_(document: str) -> list:
        """
        Tokenizes a string by splitting it at spaces (one or more). Retains punctuation and special characters.
        :param document: a string representation of a sentence.
        :return: A list of lowercase strings representing the sentence, including punctuation.
        """
        tokens = re.findall(r"\w+|[^\w\s]", document, re.UNICODE)
        tokens = list(map(str.lower, tokens))
        return tokens

    def _remove_stopwords_(self, tokens: list) -> list:
        """
        Removes stopwords from a list of tokens.
        :param tokens: list of tokens to remove stopwords from
        :return: list of tokens without stopwords
        """
        return list(filter(lambda t: t not in self.stopwords, tokens))

    def _stem_(self, tokens: list) -> list:
        """
        Stems each token in a list of tokens by applying rule-based suffix stemming.
        :param tokens: a list of string tokens
        :return: a list of stemmed string tokens
        """
        res = []
        for token in tokens:
            if token[-2:] == "ed":
                res.append(token[:-2])
            elif token[-3:] == "ing":
                res.append(token[:-3])
            elif token[-2:] == "ly":
                res.append(token[:-2])
            else:
                res.append(token)
        return res

    def preprocess(self, document: str) -> list:
        """
        Preprocesses a single document, returning a tokenized, lowercased, stemmed list of terms with stopwords removed.
        :param document: string representation of a document
        :return: processed list of terms for the document
        """
        tokens = self._tokenize_(document)
        stopped = self._remove_stopwords_(tokens)
        stemmed = self._stem_(stopped)
        return stemmed
    
    
class PreprocessorSpacy:
    
    def __init__(self):
        import spacy
        self.nlp = spacy.load("en_core_web_sm")
    
    def preprocess(self, document: str) -> list:
        """
        Converts a string into a list of segmented, stopped, and stemmed tokens.
        :param document: the input string
        :return: a list processed tokens
        """
        return [token.lemma_.lower() for token in self.nlp(document) if not (token.is_stop or token.is_punct)]