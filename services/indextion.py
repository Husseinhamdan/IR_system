from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer


def get_matrix_term_frequency(documents):
    countvectorizer  = CountVectorizer()
    matrix = countvectorizer.fit_transform(documents)
    array = matrix.toarray()
    # df_countvect = pd.DataFrame(data=array, columns=countvectorizer .get_feature_names())
    return array

def get_matrix_tfIdf(documents):
    tfidfvectorizer = TfidfVectorizer()
    tfidf_matrix = tfidfvectorizer.fit_transform(documents)
    # df_tfidfvect = pd.DataFrame(data=tfidf_matrix, columns=tfidfvectorizer.get_feature_names())
    return tfidf_matrix

