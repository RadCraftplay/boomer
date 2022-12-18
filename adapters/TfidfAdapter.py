from typing import Callable
import nltk
import numpy as np
from ast import Tuple
from adapters.Adapter import Adapter
from sklearn.feature_extraction.text import TfidfVectorizer

from utils.MathUtils import cos_sim

class TfidfAdapter(Adapter):
    def __init__(self, conversation, threshold) -> None:
        self.conversation: list[tuple[str, Callable[[], str]]] = conversation
        self.threshold: float = threshold

        learnt_matches = [x[0] for x in conversation]
    
        corpus = [x.lower() for x in learnt_matches]
        stopwords = nltk.corpus.stopwords.words("english")

        self.corpus = corpus
        self.vectorizer = TfidfVectorizer(stop_words=stopwords)
        self.vectoriced_document = self.vectorizer.fit_transform(corpus)

    def can_parse(self, sentence: str):
        # TF-IDF for query
        Q = self.vectorizer.transform([sentence])
        # Make vectors
        Q_vec = np.array(Q.todense().copy())[0,:]
        X_vec = np.array(self.vectoriced_document.todense().copy())

        # make cos similarity
        best_question_rating = 0.0
        for i in range(len(self.corpus)):
            rating = cos_sim(Q_vec, X_vec[i])
            if rating > best_question_rating:
                best_question_rating = rating
        
        return best_question_rating > self.threshold, best_question_rating
        

    def get_response(self, sentence: str) -> Callable[[], str]:
        # TF-IDF for query
        Q = self.vectorizer.transform([sentence])
        # Make vectors
        Q_vec = np.array(Q.todense().copy())[0,:]
        X_vec = np.array(self.vectoriced_document.todense().copy())

        # make cos similarity
        best_question_id = -1
        best_question_rating = 0.0
        for i in range(len(self.corpus)):
            rating = cos_sim(Q_vec, X_vec[i])
            if rating > best_question_rating:
                best_question_id = i
                best_question_rating = rating
        
        if best_question_rating > self.threshold:
            return self.conversation[best_question_id][1]
        else:
            return lambda: "Error: Trying to process a statement, that can not be processed!"

    @staticmethod
    def with_single_response(threshold: float, response_parser: Callable[[], str], questions: set[str]):
        conversation = [{question: response_parser} for question in questions]
        return TfidfAdapter(conversation, threshold)