from nltk import word_tokenize
from model.Collection import Collection
from nltk.corpus import stopwords
from model.query import Query
from model.query_collection import Query_Collection
from services.matcher import Matcher

#    query
# query_file="dataset/cacm/query.text"
# query_rel="dataset/cacm/qrels.text"
# query_collection=Query_Collection(query_file,query_rel)
# # queries=query_collection.parser()
# # for i,query in queries.items():
# #     print(query.ID +query.Name)
# #     print(query.Relation)
# q="I am interessted in artitcles written eiter by Prieve or Udo Pooch"
# corrected=query_collection.Spell_check_query(q)
# print(corrected)

# doc + collection

collection_cacm="dataset/cacm/cacm.all"
stopWord_cacm="dataset/cacm/common_words"
collection=Collection(collection_cacm,stopWord_cacm)


stopwords=collection._get_stop_word()
q="I am interested in articles written either by Prieve or Udo Pooch"
query=Query()
query.read_query(q)
q_process=query.processing_query(stopwords)
matcher=Matcher(collection,q_process)
matcher.get_result(20)



