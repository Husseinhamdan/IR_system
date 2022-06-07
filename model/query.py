from services.text_processing import *

class Query:
    def __init__(self):
        self._query_id = ""
        self._query_name = ""
        self._query_rel =[]


    def read_query(self,query):
        self._query_name=query

    def processing_query(self,stopWord):
            lower = lower_text(self._query_name)
            token = text_to_wordtoken(lower)
            filter = filter_stopWord(token, stopWord)
            stem = stemWord(filter)
            lemm = lemmWord(stem)
            return " ".join(lemm)

    def _set_query_id(self,query_id):
        self._query_id=query_id

    def _set_query_name(self,query_name):
        self._query_name=query_name

    def _set_query_rel(self,query_rel):
        self._query_rel=query_rel

    def _get_query_id(self):
        return self._query_id

    def _get_query_name(self):
        return self._query_name

    def _get_query_rel(self):
        return self._query_rel

    ID = property(_get_query_id,_set_query_id)
    Name = property(_get_query_name,_set_query_name)
    Relation=property(_get_query_rel,_set_query_rel)