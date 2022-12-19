from io import StringIO
import os
import re
from typing import Callable
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk

class SemanticSearch():
    def __init__(self, path) -> None:
        self.files = [os.path.join(path, file) for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]

        def readWhole(name):
            with open(name) as f:
                return f.read()

        corpus = [ readWhole(n) for n in self.files ]
        # Vectorize
        stopwords = nltk.corpus.stopwords.words("english")

        # Create TF-IDF vectors
        print("Fitting vectors...")
        self.vectorizer = TfidfVectorizer(stop_words=stopwords)
        X = self.vectorizer.fit_transform([l.lower() for l in corpus])
        self.X_vec = np.array(X.todense().copy())
        print("Vectors created...")

        print("Creating topic vectors...")
        from sklearn.decomposition import PCA
        pca = PCA(n_components=len(corpus))
        pca = pca.fit(X.toarray())
        pca_topic_vectors = pca.transform(X.toarray())

        print("Adding columns...")
        import pandas as pd
        columns = ['topic{}'.format(i) for i in range(pca.n_components)]
        pca_topic_vectors = pd.DataFrame(pca_topic_vectors, columns=columns)



    def search(self, query) -> list[tuple[float, str]]:
        Q = self.vectorizer.transform([query])
        Q_vec = np.array(Q.todense().copy())[0,:]

        def txt_len(v1, v2):
            result_vec = v1 - v2
            shape = result_vec.shape
            score = 0
            for i in range(shape[0]):
                score += abs(result_vec[i])
            return score

        # calculate similarity
        scores: list[tuple[float, str]] = []
        for i in range(len(self.files)):
            filename = self.files[i]
            score = txt_len(Q_vec, self.X_vec[i])
            scores.append((score, filename))
        scores.sort(key=lambda y: y[0])

        return scores
    
    def performQuery(self, match: re.Match) -> Callable[[], str]:
        def wrapper() -> str:
            builder = StringIO()
            builder.write("The best files matching the query are: ")
            index = 0
            for (_, name) in results:
                basename = os.path.basename(name)
                if index > 0:
                    builder.write(", ")
                builder.write(basename)
                index = index + 1
            return builder.getvalue()
        
        query = match.group(1)
        results = self.search(query)

        return wrapper