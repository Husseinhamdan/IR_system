import json
from builtins import reversed

from services.indextion import  *
from sklearn.metrics.pairwise import cosine_similarity

class Matcher:
    def __init__(self,Collection,query):
        self._collection=Collection
        self._documents =Collection.get_process_collection()
        self._query= query


    def calculate_similarity(self):
        similarity=[]
        documents=[self._query] + self._documents
        Tfidf=get_matrix_tfIdf(documents)
        cosine_similarities = cosine_similarity(Tfidf[0:1],Tfidf)
        for i, sim in enumerate(cosine_similarities[0]):
            similarity.append(sim)
        return self.sorted_similarity(similarity)


    def sorted_similarity(self,similarity):
        sim= []
        for i in range(len(similarity)):
            sim.append([similarity[i], i])
        sim.sort(reverse=True)
        sort_index=[]
        for x in sim:
            sort_index.append([x[0],x[1]])
        k=0
        for s in sim:
            if s[1]==2434:
                print(k)
            if s[1]==2863:
                print(k)
            if s[1]==3078:
                print(k)
            k+=1
        return sort_index


    def get_result(self,k):
        AllDoc=self._collection.parser().values()
        sim=self.calculate_similarity()
        results=[]
        docs=list(AllDoc)
        for s in sim[1:k]:
            results.append(docs[s[1]-1])
        for result in results:
            print(result.I)
        result= [obj.to_dict() for obj in results]
        jsdata = json.dumps({"results": result})
        # print(jsdata)
        return jsdata



